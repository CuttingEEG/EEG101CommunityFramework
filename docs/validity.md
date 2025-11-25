## Validity and scientific integrity in times of rapidly evolving practices

Increased computational power and technology-assisted data mining allows massively testing data on each and every possible time x electrode x frequency (...) combination. The availability of increasingly flexible tools that allow for the easy redefinition of statistical tests with a mouse click makes it a real challenge to maintain valid standards, compromising the soundness and reproducibility of research. As human neuroscience increasingly integrates AI and machine learning approaches for data processing and analyses ([DuPre & Poldrack, 2024](references.md#DuPre2024)) we must be critical about the epistemological assumptions underlying these technologies. Below, we advocate agreed-upon standard practices using open science tools and resources grounded in theoretically elaborated research.

### Research practices and reproducible[^1] science

Research practices are fundamental to scientific inquiry, and their proper application ensures reliable, reproducible, and openly extensible science.

/// details | 1.1. Reproducible EEG science
    type: info
    
Over the last 15 years, neuroscience has reckoned with how questionable research and publication practices inflate false positive rates and erode trust in scientific findings [(Nosek et al., 2012)](references.md#Nosek2012). Community-driven efforts have highlighted specific challenges and offered some solutions ([Niso, Botvinik-Nezer, et al., 2022](references.md#Niso2022a); [Niso, Krol, et al., 2022](references.md#Niso2022b); [Pernet et al., 2020](references.md#Pernet2020); [Simmons et al., 2012](references.md#Simmons2012)), general  manifestos [(Munafò et al., 2017)](references.md#Munafo2017) and pledges ([Schönbrodt et al. 2015](references.md#Shönbrodt2015)). Despite the creation of national and international networks to initiate and support relevant communities (e.g. [UK Reproducibility Network](https://www.ukrn.org/){:target="_blank"}; [ARIADNE](https://igor-biodgps.github.io/ARIADNE/contentpages/intro.html){:target="_blank"}; [the Turing Way](https://book.the-turing-way.org/index.html){:target="_blank"}) fully reproducible science is far from being the norm in empirical science in general [(Lakens et al., 2024)](references.md#Lakens2024) or EEG research in particular. 

To make progress, adopting standardized protocols for data collection, processing, and statistical analysis is essential for ensuring robust, replicable findings in EEG. At the same time, keeping high standards and re-shaping publication practices—supporting non-profit and scientifically sound publishing initiatives (e.g. open access nonprofit platforms like [Peer Community In](https://rr.peercommunityin.org/){:target="_blank"}), while avoiding opaque or predatory outlets—is critical to maintain the overall quality and credibility of EEG science.

///

/// details | Pledges
    type: pledge
    open: True

<input type='checkbox' checked id="cb-1-1" class="cb-sa" onchange="toggleCheckboxes(event)"/>
I commit to increasing robustness, replication, and standardization at each stage of my EEG work—from data collection to analysis to publishing results and data (see [https://oreoni.github.io/](https://oreoni.github.io/){:target="_blank"}). In doing so, I will consider:

/// html | ul.tasklist

  /// html | li

    <input type='checkbox' checked name="pledge_1_1_1" class="data-input" />
    pre-registering my EEG studies, using dedicated platforms (e.g. OSF, Aspredicted, ClinicalTrials) and reporting templates ([Govaart et al., 2022](references.md#Govaart2022); [Paul et al., 2021](references.md#Paul2021)) where appropriate.
  ///
  /// html | li

    <input type='checkbox' checked name="pledge_1_1_2" class="data-input" />
    clearly and systematically communicating all decisions made during data processing—adhering to guidelines such as [COBIDAS](https://www.humanbrainmapping.org/i4a/pages/index.cfm?pageID=3728){:target="_blank"} and [ARTEM-IS](https://artemis.incf.org/){:target="_blank"}, recognizing that transparent reporting is critical to the integrity and interpretability of EEG research.  
  ///
  /// html | li

    <input type='checkbox' checked name="pledge_1_1_3" class="data-input" />
    sharing the code and analysis pipelines that can straightforwardly reproduce my original results.  
  ///
  /// html | li

    <input type='checkbox' checked name="pledge_1_1_4" class="data-input" />
    publicly releasing negative results.  
  ///
  /// html | li

    <input type='checkbox' checked name="pledge_1_1_5" class="data-input" />
    sharing raw data, employing general purpose solutions (e.g. gin.g-node, datalad for datasets) and EEG specific tools and standards (e.g., BIDS-EEG, ARTEM-IS see [Niso, Krol, et al., 2022](references.md#Niso2022b)). See also Section 1.2: Standardization and Documentation of Data.
  ///
///

<input type='checkbox' checked id="cb-1-1" class="cb-sa" onchange="toggleCheckboxes(event)"/>
I commit to improving systemic reproducibility by: 

/// html | ul.tasklist

  /// html | li

    <input type='checkbox' checked name="pledge_1_1_6" class="data-input" />
    supporting initiatives focused on reproducing results from published articles (e.g. through initiatives like [\#EEGManyLabs](https://osf.io/yb3pq/){:target="_blank"}, [EEGManyPipelines](https://eegmanypipelines.github.io/){:target="_blank"}, [EEGManyAnalysts](https://www.coscience-personality.com/manyanalysts){:target="_blank"}, [TMS-EEG T4TE](https://www.t4te.org/){:target="_blank"}) either by participating in replication efforts or by supporting and communicating with researchers who are working to replicate my published results.  
  ///
  /// html | li

    <input type='checkbox' checked name="pledge_1_1_7" class="data-input" />
    improving the reproducibility and robustness of my work by testing the effects of different recording setups and analysis pipelines (e.g. through specialist scripts, for example ([Es et al., 2024](references.md#Es2024)) including “multiverse analysis” ([Aczel et al., 2021](references.md#Aczel2021); [Del Giudice & Gangestad, 2021](references.md#DelGiudice2021); [Steegen et al., 2016](references.md#Steegen2016)), see example tools; [boba](https://github.com/uwdata/boba), [multiverse](https://github.com/MUCollective/multiverse){:target="_blank"}, [multifear](https://github.com/AngelosPsy/multifear){:target="_blank"}, [multitool](https://ethan-young.github.io/multitool/){:target="_blank"}, [comet](https://github.com/mibur1/comet){:target="_blank"}, [nipype](https://nipype.readthedocs.io/en/latest/){:target="_blank"}, [shiny app](https://meteor-eeg-oldenburg.shinyapps.io/preprocessing/){:target="_blank"}, Gorgolewski et al., 2011\) and/or by validating findings across multiple recording devices and environments.  
  ///
  /// html | li

    <input type='checkbox' checked name="pledge_1_1_8" class="data-input" />
    supporting non-profit, scientifically rigorous publishing initiatives, and to refrain from participating in opaque or predatory publishing practices, whether as an author, reviewer, or editor.  
  ///
  /// html | li

    <input type='checkbox' checked name="pledge_1_1_9" class="data-input" />
    when acting as a reviewer, requesting that (where appropriate) authors follow standard, robust and replicable research protocols and make any pre-registered hypotheses, datasets and analysis scripts publicly available during the submission process to avoid access issues post-publication 
  ///

///

///

/// details | 1.2. Standardization and Documentation of Data
    type: info

Generating large, annotated, and openly accessible EEG data repositories, including clinical and neuroimaging data, is crucial for advancing basic and applied neuroscience. This facilitates discovery science, improves diagnostic applications, industry applications and educational settings, promoting learning and skill development among students and early-career researchers. By pooling resources and sharing data, we enable researchers to perform large-scale analyses that are otherwise impractical for individual laboratories. Standardising datasets, using the Brain Imaging Data Structure ([BIDS](https://bids-specification.readthedocs.io){:target="_blank"}), is a crucial stage that fosters FAIR science ([Wilkinson et al., 2016](references.md#Wilkinson2016)). To promote transparency, we suggest sharing not only raw data but also analysis scripts and detailed metadata. Platforms such as [OpenNeuro](https://openneuro.org/){:target="_blank"}, [g-node GIN](https://gin.g-node.org/){:target="_blank"}, [OSF](https://osf.io/){:target="_blank"}, or [Zenodo](https://zenodo.org/){:target="_blank"} can be used to facilitate this process while ensuring adherence to FAIR principles. Such repositories provide diverse datasets that can help uncover new patterns, validate findings across different populations, and improve the generalizability of results. 

Moreover, open data repositories are invaluable for developing and refining diagnostic applications. They provide the necessary volume and variety of data to train machine learning algorithms and develop robust biomarkers for neurological and psychiatric conditions.
///

/// details | Pledges
    type: pledge
    open: True

<input type='checkbox' checked id="cb-1-2" class="cb-sa" onchange="toggleCheckboxes(event)"/>
I commit to making sure that the data I collect and work with uses best practices in data standardization and documentation. I will do so by:

/// html | ul.tasklist

/// html | li

    <input type='checkbox' checked name="pledge_1_2_1" class="data-input" />
    sharing curated EEG data as openly as possible (i.e. as institute agreements allow) along with detailed metadata, annotations, and tags, using well-established open repositories.  
///
/// html | li

    <input type='checkbox' checked name="pledge_1_2_2" class="data-input" />
    using the FAIR principles for sharing data ([Wilkinson et al., 2016](references.md#Wilkinson2016), data should be Findable, Accessible, Interoperable, and Reusable).   
///
/// html | li

    <input type='checkbox' checked name="pledge_1_2_3" class="data-input" />
    using standards such as the Brain Imaging Data Structure (BIDS) for my data to ensure interoperability and ease of use, and sharing it as openly as institute agreements or institutional repositories allow.  
///
/// html | li

    <input type='checkbox' checked name="pledge_1_2_4" class="data-input" />
    regularly update and enhance my shared data based on user feedback.
///

///

///

/// details | 1.3. Open Science and Open Source
    type: info

Using transparent approaches, making sure that results and data are accessible is an essential feature of science. Open science is a broad movement in contemporary science that promotes open access to all aspects of the scientific process. Provided that participants' privacy is protected, we generally advocate for open science practices.

Of particular interest to the EEG community, it is important to consider that EEG data requires elaborate software to perform increasingly complex analyses. Open-source (OS) software and hardware are vital in advancing EEG research. By supporting and contributing to Free and Open-Source Software (FOSS) and Open-Source Hardware (OSH), we encourage community transparency, collaboration, and innovation. Open-source tools allow researchers to inspect, modify, and improve code and designs, leading to more robust and reliable scientific instruments and analyses. At the same time, OS fosters the development and sharing of cutting-edge methods and makes it easy to attribute developers for their contributions. This collective effort enhances the reproducibility of our work, accelerates scientific progress, and promotes a culture of openness and mutual support in the EEG community. Furthermore, open-source and open-sciences initiatives lower barriers to entry for researchers worldwide, especially those in resource-limited settings. By making software, hardware and knowledge freely available, we democratize access to cutting-edge tools, promoting inclusivity and diversity in EEG science (also see Democratization section below).

At the same time, high standards and best practice in developing and using OS scientific software must be maintained to harvest its full potential (see [Westner et al., 2024](references.md#Westner2024))

///

/// details | Pledges
    type: pledge
    open: True

<input type='checkbox' checked id="cb-1-3" class="cb-sa" onchange="toggleCheckboxes(event)"/>
I commit to supporting open scientific practices to promote transparency, collaboration, and innovation about source code. I will do so by:

/// html | ul.tasklist

/// html | li

    <input type='checkbox' checked name="pledge_1_3_1" class="data-input" />
    integrating open-source tools, data management practices, and transparent workflows into my research whenever possible.  
///
/// html | li

    <input type='checkbox' checked name="pledge_1_3_2" class="data-input" />
    citing open-source software properly, including specific version tags or DOIs, to 1\) give full credit to *all* developers’ contributions and 2\) enable full replication of analysis pipelines.  
///
/// html | li

    <input type='checkbox' checked name="pledge_1_3_3" class="data-input" />
    following best practices in software use—such as version control, clear documentation, and code review—to enhance reliability and reproducibility.  
///
/// html | li

    <input type='checkbox' checked name="pledge_1_3_4" class="data-input" />
    using open licenses for code and tools that I develop (e.g., BSD, MIT, GPL), creating readable documentation, and publishing my code on accessible platforms (e.g., GitHub, GitLab, OSF).  
///
/// html | li

    <input type='checkbox' checked name="pledge_1_3_5" class="data-input" />
    contributing back, when I benefit from others’ tools, if I have the skills or resources—whether through bug reports, testing, documentation, tutorials, or feature development.  
///
/// html | li

    <input type='checkbox' checked name="pledge_1_3_6" class="data-input" />
    recognizing and valuing software development as a genuine scientific contribution; where possible, I will encourage formal acknowledgment of developers’ work (e.g., in publications and grants).  
///
/// html | li

    <input type='checkbox' checked name="pledge_1_3_7" class="data-input" />
    promoting open-source solutions in my institution, professional networks, and collaborations by highlighting their benefits for transparency, reproducibility, and inclusivity.  
///
/// html | li

    <input type='checkbox' checked name="pledge_1_3_8" class="data-input" />
    encouraging administrators, funding bodies, and reviewers to recognize and reward open-science practices and open-source development as key indicators of scientific excellence.   
///
/// html | li

    <input type='checkbox' checked name="pledge_1_3_9" class="data-input" />
    supporting, where relevant, mentor colleagues or trainees in adopting open-source tools and methods, lowering barriers to entry for all researchers—including those in resource-limited settings.
///

///

///

### Interpretable and theoretically well-grounded research

For EEG research to drive meaningful progress, it must be grounded in current theories and integrate insights from multiple disciplines. This is especially crucial as AI tools and models become increasingly prominent in the field.

/// details | 1.4. Theory-driven and data-driven research
    type: info 

Recent years have seen an increasing emphasis on ever-larger datasets ([Frégnac, 2017](references.md#Fregnac2017)) with insufficient attention to the theoretical underpinnings that might explain brain activity and its emergent properties ([Borsboom et al., 2021](references.md#Borsboom2021); [Eronen & Bringmann, 2021](references.md#Eronen2021); [Gerstner et al., 2012](references.md#Gerstner2012)). 

From a philosophical or epistemological standpoint, it is vital to recognize the limits of any single perspective, emphasizing instead frameworks that integrate dynamic, second-person interaction as central to cognition ([Hinrichs et al., 2025](references.md#Hinrichs2025)). A purely data-driven understanding of neuroscience—particularly one focused on individual-brain analysis—can be limited in scope (Forest, 2016). We therefore advocate for cultivating strong theoretical neuroscience foundations and for interdisciplinary exchanges that draw insights from fields such as philosophy, anthropology, psychology, the arts, and the humanities. These cross-pollinations could yield innovative frameworks that enrich our uses and interpretations of EEG data.

In addition, the considerations outlined here link closely with our broader calls for epistemological rigor (see also Section 3 - Responsibility). Effective science requires the “how” of sound methods and robust protocols, and the “why”: the political, social, and ethical relevance behind our research questions.

By grounding EEG research in a well-articulated theoretical framework and seeking contributions from diverse disciplines, we can enhance the explanatory power of our findings, enrich interpretation, and promote more meaningful progress in understanding the human brain.

///

/// details | Pledges
    type: pledge
    open: True

<input type='checkbox' checked id="cb-1-4" class="cb-sa" onchange="toggleCheckboxes(event)"/>
I commit to balancing theory-driven and data-driven approaches in my research. I do so by:

/// html | ul.tasklist

/// html | li

    <input type='checkbox' checked name="pledge_1_4_1" class="data-input" />
    engaging in the development of strong preliminary theoretical reflections on the neurophysiological basis of the expected EEG results.  
///
/// html | li

    <input type='checkbox' checked name="pledge_1_4_2" class="data-input" />
    adapting my experimental practices when performing data-driven experiments. I systematically adapt thresholds for multiple comparison correction, and validate conclusions with sound methodology.  
///
/// html | li

    <input type='checkbox' checked name="pledge_1_4_3" class="data-input" />
    refraining from using theory-blind approaches to scientific investigation prone to questionable research practices—especially those consuming large computational resources—without a prior theoretical rationale (cf. pledges 3.4 on environmental responsibility).  
///
/// html | li

    <input type='checkbox' checked name="pledge_1_4_4" class="data-input" />
    reading synthesis texts from other disciplines (e.g., philosophy, anthropology, history, political science). This investment is worthwhile, helping align my research objectives with societal realities.  
///
/// html | li

    <input type='checkbox' checked name="pledge_1_4_5" class="data-input" />
    embracing diverse perspectives e.g. integrating insights from the arts and humanities into my research and actively collaborating in interdisciplinary teams and consortia to foster innovation, cross-pollination of ideas, and a deeper theoretical grounding for EEG science.  
///
/// html | li

    <input type='checkbox' checked name="pledge_1_4_6" class="data-input" />
    training students to engage with theoretical reflections involving interdisciplinary approaches.
///
///

///

/// details | 1.5. Transparent, interpretable, and explainable modeling 
    type: info 

A key challenge emerging for complex computational models—particularly those applied to data analysis and clinical decision-making—is ensuring their transparency, interpretability, and explainability. Modern ML/AI architectures often surpass our theoretical grasp [(Holzinger et al., 2022)](references.md#Holzinger2022), creating an epistemic gap where we rely on tools we cannot fully comprehend [(Cichy & Kaiser, 2019)](references.md#Cichy2019). To address this, the EEG community must dedicate basic research and advanced computational tools (see the Local Interpretable Model-Agnostic or LIME approach as one such framework [(Ribeiro et al., 2016)](references.md#Ribeiro2016) to uncovering how these models operate, while simultaneously leveraging their potential to advance knowledge and applications.

Fostering interpretability and explainability requires a solid theoretical foundation and active collaboration across disciplines. The application of cross-validation with independent and diverse datasets will help mitigate overfitting and bias, increasing the likelihood that conclusions drawn from ML/AI models are reliable. We hence advocate for i) **diverse and open datasets** that will make sure AI models will be trained on neurophysiological data acquired from a wide range of population, cognitive states, and environmental contexts; ii) **interpretable AI models** that prioritise explainable AI/ML approaches rather than using black boxes; iii) **integrative validation methods** to acknowledge and incorporate in our models the fact that cognition cannot be meaningfully reduced to algorithmic patterns without considering the broader, complex organism-environment system.

Thus, by openly sharing parameters, feature-selection methods, and decision-making processes, we can build stronger trust within our community, mitigate algorithmic reductionism, and accelerate meaningful progress in ML/AI-driven EEG research.

///

/// details | Pledges
    type: pledge
    open: True

<input type='checkbox' checked id="cb-1-5" class="cb-sa" onchange="toggleCheckboxes(event)"/>
I commit to using transparent, interpretable and explainable modeling. I will do so by:

/// html | ul.tasklist

  /// html | li

    <input type='checkbox' checked name="pledge_1_5_1" class="data-input" />
    supporting the development of more transparent, explainable, and interoperable computational models and tools (e.g., LIME), including the use of independent databases for cross-validation.  
  ///
  /// html | li

    <input type='checkbox' checked name="pledge_1_5_2" class="data-input" />
    publicly disclosing ML/AI scripts and documenting all relevant decisions in my model designs—including feature-selection methods, parameter settings, and validation steps—to foster transparency and interpretability in ML/AI-driven neuroscience.  
  ///
  /// html | li

    <input type='checkbox' checked name="pledge_1_5_3" class="data-input" />
    promoting best practices for AI transparency when training students and early career researchers, reviewing grants and evaluating manuscripts.  
  ///
  /// html | li

    <input type='checkbox' checked name="pledge_1_5_4" class="data-input" />
    contributing to counteracting the risks of algorithmic reductionism, which mistakenly reduces cognition to an isolated signal that can be decoded. 
  ///

///

///

[^1]: ‘Reproducible’ is used here as an umbrella term, encompassing all aspects of recreating scientific results (aka replicable, generalisable, robust, ..) as described in [Niso, Botvinik-Nezer, et al., 2022](references.md#Niso2022a); [Niso, Krol, et al., 2022b](references.md#Niso2022b)
