import re
import os
import pypandoc

# Configuration
DOCS_DIR = 'docs'
FILES = [
    'introduction.md',
    'validity.md',
    'democratization.md',
    'responsibility.md',
    'conclusion.md',
    'references.md'
]
OUTPUT_DOCX = 'manifesto.docx'

def process_links(content, current_file):
    """
    Converts cross-file links to internal links.
    [Text](other.md#anchor) -> [Text](#anchor)
    [Text](other.md) -> [Text](#file-anchor)
    """
    def replace_link(match):
        text = match.group(1)
        url = match.group(2)
        attr = match.group(3) # Optional attributes like { #id }
        
        # If attributes exist, append them to text so they survive DOCX roundtrip
        if attr:
            text = f"{text} {attr.strip()}"
        
        # Check if it's a local markdown file link
        if '.md' in url and not url.startswith('http'):
            parts = url.split('#')
            filename = parts[0]
            anchor = parts[1] if len(parts) > 1 else None
            
            # If it links to one of our files
            if filename in FILES:
                if filename == current_file:
                    # Internal link to same file
                    if anchor:
                        return f'[{text}](#{anchor})'
                    else:
                        # Link to top of same file?
                        # Usually [Text](file.md) means top.
                        # We can just leave it as #file-anchor (the one we added)
                        file_anchor = filename.replace('.', '-').lower()
                        return f'[{text}](#{file_anchor})'
                else:
                    # Cross-file link
                    # Encode filename in anchor to preserve it for import
                    # file.md -> file_md
                    safe_filename = filename.replace('.', '_')
                    if anchor:
                        return f'[{text}](#{safe_filename}__{anchor})'
                    else:
                        return f'[{text}](#{safe_filename})'
        
        # If we modified text (because of attr) or just want to return the link
        if attr:
            return f'[{text}]({url})'

        return match.group(0)

    # Regex for markdown links: [text](url){ #id } or [text](url)
    # We capture the optional attribute part
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)(\s*\{ *#[^}]+\})?', replace_link, content)

def process_checkboxes(content):
    """
    Replaces <input ...> with [id] or [name] for cleaner DOCX.
    """
    # Replace id-based checkboxes: [cb-X-Y]
    # <input type='checkbox' checked id="cb-1-1" class="cb-sa" onchange="toggleCheckboxes(event)"/>
    content = re.sub(r'<input[^>]+id="(cb-[^"]+)"[^>]*>', r'[\1]', content)
    
    # Replace name-based checkboxes: [pledge_X_Y_Z]
    # <input type='checkbox' checked name="pledge_1_1_1" class="data-input" />
    content = re.sub(r'<input[^>]+name="(pledge_[^"]+)"[^>]*>', r'[\1]', content)
    
    return content

def escape_html(content):
    """
    Escapes HTML tags so they appear as text in DOCX.
    """
    content = content.replace('<', '&lt;')
    content = content.replace('>', '&gt;')
    return content

def unindent_blocks(content):
    """
    Flattens indentation for /// blocks while preserving logical structure.
    """
    lines = content.split('\n')
    new_lines = []
    stack_depth = 0
    
    # Regex to detect block start/end
    # Starts with optional whitespace, then /// then space then something
    block_start_pattern = re.compile(r'^\s*///\s+\w+')
    # Starts with optional whitespace, then /// and nothing else (except whitespace)
    block_end_pattern = re.compile(r'^\s*///\s*$')
    
    for i, line in enumerate(lines):
        # Calculate current indentation (spaces)
        current_indent = len(line) - len(line.lstrip(' '))
        
        is_start = block_start_pattern.match(line)
        is_end = block_end_pattern.match(line)
        
        if is_start:
            # It's a start tag. 
            # We strip its indentation.
            new_lines.append(line.strip())
            # Add a blank line to prevent merging with next line in DOCX
            new_lines.append('') 
            stack_depth += 1
        elif is_end:
            # It's an end tag.
            stack_depth -= 1
            if stack_depth < 0: stack_depth = 0 # Safety
            new_lines.append(line.strip())
            # Add a blank line to prevent merging
            new_lines.append('')
        else:
            # It's content.
            # We remove indentation corresponding to the stack depth.
            # Assuming 4 spaces per level.
            indent_to_remove = stack_depth * 4
            
            processed_line = ""
            # Only remove if the line actually has that much indentation
            if current_indent >= indent_to_remove:
                processed_line = line[indent_to_remove:]
            else:
                if line.strip() == '':
                    processed_line = ''
                else:
                    processed_line = line.lstrip()
            
            # Special handling for metadata lines and inputs to prevent merging
            stripped_line = processed_line.strip()
            if stripped_line.startswith('type:') or stripped_line.startswith('open:') or stripped_line.startswith('<input') or stripped_line.startswith('[cb-') or stripped_line.startswith('[pledge_'):
                new_lines.append(processed_line)
                new_lines.append('') # Add blank line to force separate paragraph
            else:
                new_lines.append(processed_line)
            
            # If the NEXT line is a /// tag, we should ensure we have a blank line here too?
            # Or if THIS line is the last line of a paragraph?
            # To be safe, we could add blank lines between everything, but that makes the doc huge.
            # The issue was mainly /// tags merging with content.
            # By adding a blank line AFTER /// tags, we solve:
            # /// details
            # type: info
            # ->
            # /// details
            # 
            # type: info
            
            # And:
            # ///
            # /// html
            # ->
            # ///
            # 
            # /// html
            
            # This should be sufficient.

    return '\n'.join(new_lines)

def main():
    full_content = []
    
    for filename in FILES:
        filepath = os.path.join(DOCS_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        print(f"Processing {filename}...")
        
        # 1. Add File Marker
        file_anchor = filename.replace('.', '-').lower()
        # We add a visible marker for the file start, and an anchor
        # Using HTML comment for the marker to be hidden in DOCX? 
        # No, we need it to split back. 
        # Let's use a special string that looks like a header or comment.
        # But user wants "readily editable".
        # Let's use a custom XML-like tag that we can hide or just leave visible.
        # "<!-- FILE: filename.md -->" might be stripped by Pandoc or Word.
        # Let's use a bold text line.
        header = f"\n\n**=== FILE: {filename} ===** {{#{file_anchor}}}\n\n"
        
        # 2. Process Links
        content = process_links(content, filename)
        
        # 3. Process Checkboxes
        content = process_checkboxes(content)
        
        # 4. Unindent Blocks
        content = unindent_blocks(content)
        
        # 5. Escape HTML
        # We do this AFTER unindenting, because unindenting relies on spaces.
        # But wait, unindenting doesn't care about content.
        content = escape_html(content)
        
        # 5. Process Checkboxes
        content = process_checkboxes(content)
        
        full_content.append(header + content)

    combined_markdown = "".join(full_content)
    
    # Save intermediate markdown for debugging
    with open('debug_combined.md', 'w', encoding='utf-8') as f:
        f.write(combined_markdown)
        
    print("Converting to DOCX...")
    # Convert to DOCX
    # We use 'markdown' format. 
    # We might need extensions. 'markdown+raw_html' might be needed if we didn't escape.
    # Since we escaped, standard markdown should treat &lt; as literal <.
    pypandoc.convert_text(
        combined_markdown, 
        'docx', 
        format='markdown', 
        outputfile=OUTPUT_DOCX
    )
    print(f"Created {OUTPUT_DOCX}")

if __name__ == "__main__":
    main()
