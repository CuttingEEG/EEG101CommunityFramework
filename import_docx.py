import re
import os
import pypandoc

# Configuration
DOCS_DIR = 'docs'
INPUT_DOCX = 'manifesto.docx'
FILES = [
    'introduction.md',
    'validity.md',
    'democratization.md',
    'responsibility.md',
    'conclusion.md',
    'references.md'
]

def build_anchor_map(content):
    """
    Scans the content to map anchors to filenames.
    (Kept for reference, though link restoration now uses encoding)
    """
    anchor_map = {}
    current_file = None
    
    # Regex for file marker
    file_marker_pattern = re.compile(r'\*\*=== FILE: ([\w\.-]+) ===\*\*')
    
    # Regex for headers with attributes: ## Header {#anchor}
    # Pandoc output: ## Header {#anchor}
    # Or just {#anchor} at end of line
    anchor_pattern = re.compile(r'\{#([\w\.-]+)\}')
    
    lines = content.split('\n')
    for line in lines:
        # Check for file marker
        m_file = file_marker_pattern.search(line)
        if m_file:
            current_file = m_file.group(1)
            continue
            
        if current_file:
            # Check for anchors
            anchors = anchor_pattern.findall(line)
            for anchor in anchors:
                anchor_map[anchor] = current_file
                
    return anchor_map

def process_content(content, anchor_map):
    """
    Splits content into files, re-indents blocks, restores links and HTML.
    """
    files_content = {}
    current_file = None
    current_buffer = []
    
    # Stack for indentation
    # We push the expected indentation level (in spaces)
    # But we also need to know the block type to decide whether to indent content.
    # Stack items: (indent_level, block_type)
    indent_stack = [(0, None)] 
    
    # Regex for file marker
    file_marker_pattern = re.compile(r'\*\*=== FILE: ([\w\.-]+) ===\*\*')
    
    # Regex for /// blocks
    # We need to handle escaped pipe \|
    # block_start: /// details ... or /// html ...
    # Capture the type (group 1) and the rest of the line (group 2)
    block_start_pattern = re.compile(r'^\s*///\s+(\w+)(.*)')
    block_end_pattern = re.compile(r'^\s*///\s*$')
    
    # Pre-process to split trailing /// that might have been merged by pypandoc
    split_lines = []
    for line in content.split('\n'):
        stripped = line.strip()
        if stripped.endswith('///') and stripped != '///':
            # Check if it's really a tag (preceded by space)
            if re.search(r'\s///\s*$', line):
                idx = line.rfind('///')
                split_lines.append(line[:idx])
                split_lines.append(line[idx:])
            else:
                split_lines.append(line)
        else:
            split_lines.append(line)
            
    lines = split_lines
    
    for line in lines:
        # 1. Check for file marker
        m_file = file_marker_pattern.search(line)
        if m_file:
            # Save previous buffer
            if current_file:
                files_content[current_file] = clean_buffer(current_buffer)
            
            current_file = m_file.group(1)
            current_buffer = []
            indent_stack = [(0, None)] # Reset stack for new file
            continue
            
        if current_file is None:
            continue # Skip preamble if any
            
        # 2. Unescape characters
        line = line.replace(r'\|', '|')
        line = line.replace(r'\<', '<')
        line = line.replace(r'\>', '>')
        line = line.replace(r'\_', '_')
        line = line.replace(r'\[', '[')
        line = line.replace(r'\]', ']')
        line = line.replace('\u00A0', ' ') # Replace non-breaking space
        
        # Remove trailing backslash (hard break from pandoc)
        if line.endswith('\\'):
            line = line[:-1]
        
        # 3. Handle Indentation Logic
        # Check if it's a block start/end
        is_start = block_start_pattern.match(line)
        is_end = block_end_pattern.match(line)
        
        current_indent, current_block_type = indent_stack[-1]
        
        if is_start:
            # It's a start tag. Print with current indent.
            # Then increase indent for NEXT lines.
            block_type = is_start.group(1)
            rest_of_tag = is_start.group(2)
            
            # Determine indentation for the start tag itself
            # Logic:
            # If parent is 'details', child indent is 0 relative to parent.
            # If parent is 'html' (ul.tasklist), child indent is 2 relative to parent.
            # If parent is None (root), indent is 0.
            
            tag_indent = current_indent
            
            indented_line = (' ' * tag_indent) + line
            current_buffer.append(indented_line)
            
            # Calculate indent for content inside this new block
            new_indent = tag_indent
            if block_type == 'html':
                if 'ul.tasklist' in rest_of_tag:
                    new_indent += 2 # ul.tasklist indents children by 2
                elif 'li' in rest_of_tag: # Assuming /// html | li
                    new_indent += 2 # li indents content by 2 (relative to its own indent)
                else:
                    new_indent += 4 # Default html indent
            elif block_type == 'details':
                new_indent += 0 # details blocks DO NOT indent their content (except metadata)
            else:
                new_indent += 4 # Default to indenting
                
            indent_stack.append((new_indent, block_type))
            
        elif is_end:
            # It's an end tag.
            # Pop stack first (return to previous indent level)
            if len(indent_stack) > 1:
                indent_stack.pop()
            
            # The end tag should match the indent of the start tag
            # Which is the indent level of the PARENT
            parent_indent, _ = indent_stack[-1]
            
            indented_line = (' ' * parent_indent) + line
            current_buffer.append(indented_line)
        else:
            # Normal line. Apply current indent?
            
            # Special handling for metadata lines in 'details' blocks
            # type: ... and open: ... should be indented 4 spaces
            if current_block_type == 'details':
                stripped = line.strip()
                if stripped.startswith('type:') or stripped.startswith('open:'):
                    # Indent 4 spaces
                    indented_line = (' ' * (current_indent + 4)) + line
                else:
                    # Normal content in details -> No indent (current_indent is 0 relative to block)
                    indented_line = (' ' * current_indent) + line
            else:
                # Normal content in other blocks (html) -> Apply indent
                if line.strip() == '':
                    current_buffer.append('')
                    continue
                else:
                    # Strip leading whitespace from the line to avoid double indentation
                    stripped_line = line.lstrip()
                    
                    # Special handling for metadata in details blocks
                    # They must be indented even if the block content is 0-indented
                    if current_block_type == 'details' and (stripped_line.startswith('type:') or stripped_line.startswith('open:')):
                        indented_line = (' ' * (current_indent + 4)) + stripped_line
                    else:
                        indented_line = (' ' * current_indent) + stripped_line
            
            current_buffer.append(indented_line)
                
    # Save last file
    if current_file:
        files_content[current_file] = clean_buffer(current_buffer)
        
    return files_content

def restore_links(content_lines, anchor_map, current_file):
    """
    Restores cross-file links using encoded anchors.
    [Text](#file_md__anchor) -> [Text](file.md#anchor)
    [Text](#file_md) -> [Text](file.md)
    """
    new_lines = []
    link_pattern = re.compile(r'\[([^\]]+)\]\(#([\w\.-]+)\)')
    
    def replace_link(match):
        text = match.group(1)
        anchor = match.group(2)
        
        # Check for encoded filename
        # Pattern: filename_md__anchor OR filename_md
        
        # Try to find a matching file prefix
        target_file = None
        real_anchor = None
        
        for filename in FILES:
            safe_filename = filename.replace('.', '_')
            
            if anchor == safe_filename:
                target_file = filename
                real_anchor = None
                break
            elif anchor.startswith(safe_filename + '__'):
                target_file = filename
                real_anchor = anchor[len(safe_filename) + 2:]
                break
        
        if target_file:
            if target_file == current_file:
                # Should be internal link
                if real_anchor:
                    return f'[{text}](#{real_anchor})'
                else:
                    # Link to top of current file
                    return f'[{text}](#)' # Or just remove link?
            else:
                # Cross-file link
                if real_anchor:
                    return f'[{text}]({target_file}#{real_anchor})'
                else:
                    return f'[{text}]({target_file})'
        
        # If not encoded, it's a regular internal link
        return match.group(0)

    for line in content_lines:
        new_line = link_pattern.sub(replace_link, line)
        new_lines.append(new_line)
        
    return new_lines

def restore_attributes(lines):
    """
    Restores attributes hidden in link text.
    [Text { #id }](url) -> [Text](url){ #id }
    """
    new_lines = []
    # Regex: [Text { #id }](url)
    # We need to be careful about the text part.
    # It ends with { #id }.
    pattern = re.compile(r'\[(.*?) \{ *(#[^}]+) *\}\]\(([^)]+)\)')
    
    def replace(match):
        text = match.group(1)
        attr = match.group(2).strip()
        url = match.group(3)
        return f'[{text}]({url}){{ {attr} }}'

    for line in lines:
        new_line = pattern.sub(replace, line)
        new_lines.append(new_line)
    return new_lines

def restore_checkboxes(lines):
    """
    Restores [id] or [name] to <input ...> tags.
    """
    new_lines = []
    # Regex for [cb-...]
    cb_pattern = re.compile(r'\[(cb-[^\]]+)\]')
    # Regex for [pledge_...]
    pledge_pattern = re.compile(r'\[(pledge_[^\]]+)\]')
    
    for line in lines:
        # Check for cb- ID
        if cb_pattern.search(line):
            def replace_cb(match):
                cb_id = match.group(1)
                return f"<input type='checkbox' checked id=\"{cb_id}\" class=\"cb-sa\" onchange=\"toggleCheckboxes(event)\"/>"
            line = cb_pattern.sub(replace_cb, line)
            
        # Check for pledge_ NAME
        if pledge_pattern.search(line):
            def replace_pledge(match):
                pledge_name = match.group(1)
                return f"<input type='checkbox' checked name=\"{pledge_name}\" class=\"data-input\" />"
            line = pledge_pattern.sub(replace_pledge, line)
            
        new_lines.append(line)
    return new_lines

def clean_buffer(lines):
    """
    Post-process lines to merge metadata and inputs that were split by blank lines.
    Also removes leading blank lines.
    """
    # Remove leading blank lines
    while lines and lines[0].strip() == '':
        lines.pop(0)
        
    cleaned = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Helper to look ahead skipping blanks
        def find_next_non_blank(start_idx):
            k = start_idx
            while k < len(lines) and lines[k].strip() == '':
                k += 1
            if k < len(lines):
                return k, lines[k]
            return None, None

        next_idx, next_line = find_next_non_blank(i + 1)
        
        if next_idx:
            # Merge /// details and type:
            if '/// details' in line and 'type:' in next_line:
                cleaned.append(line)
                # Don't append next_line yet, let it be processed in next iteration
                # so it can be merged with open: if needed
                i = next_idx
                continue

            # Merge type: and open:
            if 'type:' in line and 'open:' in next_line:
                cleaned.append(line)
                cleaned.append(next_line)
                i = next_idx + 1
                continue

            # Ensure blank line after metadata if followed by text
            if ('type:' in line or 'open:' in line) and next_line.strip() != '' and not next_line.strip().startswith('open:') and not next_line.strip().startswith('///'):
                 cleaned.append(line)
                 cleaned.append('') # Force blank line
                 cleaned.append(next_line)
                 i = next_idx + 1
                 continue
                
            # Ensure blank line after /// html | li
            if '/// html' in line and 'li' in line:
                 cleaned.append(line)
                 if i + 1 < len(lines) and lines[i+1].strip() != '':
                     cleaned.append('')
                 i += 1
                 continue
                 
            # Merge <input> or [cb-...] or [pledge_...] and following text
            # Only if it is on its own line (which it is if we split it)
            is_input = '<input' in line or '[cb-' in line or '[pledge_' in line
            if is_input and next_line.strip() != '':
                 # Check if it was split by us (i.e. there was a blank line)
                 # If next_idx > i + 1, there was a blank line.
                 if next_idx > i + 1:
                     cleaned.append(line)
                     cleaned.append(next_line)
                     i = next_idx + 1
                     continue
        
        cleaned.append(line)
        i += 1
    return cleaned

def main():
    print("Converting DOCX to Markdown...")
    # Convert DOCX to Markdown
    # We use 'markdown' format (pandoc's markdown)
    # We enable 'raw_html' to ensure HTML tags are preserved if they exist?
    # Actually, we want to process the text representation.
    content = pypandoc.convert_file(INPUT_DOCX, 'markdown', format='docx', extra_args=['--wrap=none'])
    
    # Save debug
    with open('debug_import_full.md', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Building anchor map...")
    anchor_map = build_anchor_map(content)
    # print("Anchor map:", anchor_map)
    
    print("Processing content...")
    files_content = process_content(content, anchor_map)
    
    for filename, lines in files_content.items():
        print(f"Restoring {filename}...")
        
        # Restore links
        lines = restore_links(lines, anchor_map, filename)
        
        # Restore attributes
        lines = restore_attributes(lines)
        
        # Restore checkboxes
        lines = restore_checkboxes(lines)
        
        # Join lines
        file_content = '\n'.join(lines)
        
        # Clean up multiple blank lines?
        # The export process added blank lines.
        # We might want to reduce 3+ newlines to 2.
        file_content = re.sub(r'\n{3,}', '\n\n', file_content)
        
        # Write to file
        filepath = os.path.join(DOCS_DIR, filename)
        # We might want to backup original files first?
        # For now, overwrite.
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(file_content)
            
    print("Import complete.")

if __name__ == "__main__":
    main()
