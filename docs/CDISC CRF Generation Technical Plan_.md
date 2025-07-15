# **Technical and Requirements Specification for an Automated, CDISC-Compliant CRF Generation System**

## **Executive Summary**

This document provides a comprehensive technical and requirements specification for the development of an advanced software system designed to automate the generation of CDISC-compliant Case Report Forms (CRFs). By ingesting clinical study protocols in various formats, the system will employ a sophisticated Natural Language Processing (NLP) pipeline to extract key data collection requirements, semantically map them to established CDISC standards, and produce validated, human-readable, and machine-readable CRF artefacts.

The primary strategic value of this system lies in its potential to dramatically accelerate clinical trial setup, reduce manual errors in CRF design, and ensure regulatory compliance from the earliest stages of data definition. The core architecture is designed around a modular, Python-based ecosystem, leveraging best-in-class libraries for NLP (spaCy, medspaCy), data validation (Pydantic), and web services (FastAPI). This approach ensures high performance, maintainability, and extensibility.

A foundational principle of the system's design is its adherence to regulatory requirements, specifically 21 CFR Part 11\. This is achieved through a robust framework of security controls, immutable audit trails for all data transformations, and a design that supports formal system validation. The entire development and deployment lifecycle will be managed via a rigorous Continuous Integration and Continuous Deployment (CI/CD) pipeline, which not only ensures software quality but also serves as a key compliance asset.

The system will be delivered as a hybrid solution, featuring a containerized REST API for enterprise integration, a command-line interface (CLI) for power users, and an optional web-based user interface for simplified access. Key outputs include version-controlled Markdown CRFs for human review and CDISC ODM-XML/JSON 2.0 files for seamless integration with Electronic Data Capture (EDC) systems.

To foster transparency and community collaboration in a standards-driven industry, the core engine is proposed to be open-source, governed by a clear framework for contributions and future standards adoption. This specification document serves as the definitive technical blueprint for the project, outlining all key decisions, architectural patterns, and implementation strategies required to achieve its objectives.

## **Section 1: Foundational Framework and Project Scope**

This section establishes the foundational parameters of the project, defining what is being built, for whom, and under what constraints. These decisions are paramount as they influence every subsequent architectural and technical choice.

### **1.1. Deliverable Format and Target User Personas**

The project will be delivered as a hybrid system comprising three primary components to cater to a diverse user base with varying technical expertise and integration needs. This multi-faceted approach ensures maximum utility and adoption across different roles within the clinical trial ecosystem.

**Deliverable Components:**

1. **A Git Repository:** The core deliverable will be a version-controlled Git repository. This repository will contain the complete source code, CI/CD workflow definitions, Docker containerization scripts, comprehensive documentation, and all versioned project artefacts. This aligns with modern software development and DevOps best practices, ensuring transparency, reproducibility, and facilitating collaborative development.  
2. **A Containerized Web Service (REST API):** This will be the primary interface for programmatic and system-to-system integration. It will allow other clinical trial management systems (CTMS), electronic data capture (EDC) systems, and automated workflows to consume the tool's functionality. The API will be the main entry point for CROs and large sponsors seeking to integrate CRF generation into their existing infrastructure.1  
3. **A Command-Line Interface (CLI) Tool:** A powerful CLI will be provided to serve technical users, such as data managers and statistical programmers. This interface enables scripting, batch processing of multiple protocols, and integration into local development and data processing pipelines.  
4. **An Optional Single-Page Application (SPA) Web UI:** To lower the barrier to entry for non-technical users, an optional, self-contained web UI will be developed. This SPA will provide a simple "front door" allowing users like study designers or principal investigators to upload a protocol document and download a ZIP archive containing the generated CRF artefacts, without needing to interact with the API or CLI directly.3

**Target User Personas:**

The system is designed to serve three key user personas, each with distinct goals and technical requirements:

* **Data Manager (Persona: "Maria"):** Maria is a technical professional at a Contract Research Organization (CRO) responsible for end-to-end clinical data management, including eCRF design, database builds, and managing data from central labs.1  
  * **Primary Interaction:** Maria will primarily use the REST API to integrate the CRF generation tool into her organization's automated study start-up workflow. She will also use the CLI for specific batch tasks.  
  * **Key Needs:** Maria values accuracy, standards compliance, and traceability above all. She requires detailed validation logs, clear mapping documentation, and outputs (ODM-XML) that can be seamlessly imported into her EDC system. She is responsible for ensuring the final database is robust and audit-ready.  
* **Study Designer (Persona: "Dr. Chen"):** Dr. Chen is a Principal Investigator (PI) or clinical scientist who designs the study protocol.3 His expertise is in the clinical and scientific aspects of the trial, with limited technical programming skills.  
  * **Primary Interaction:** Dr. Chen will be the primary user of the optional SPA Web UI.  
  * **Key Needs:** He requires a tool that is intuitive and provides rapid feedback. His goal is to upload a draft protocol (e.g., a DOCX file) and quickly see how the specified procedures and assessments translate into a structured CRF, allowing for fast iteration on the protocol design itself.  
* **CRO Technical Lead (Persona: "David"):** David is responsible for deploying, validating, and maintaining software systems within the CRO's regulated GxP environment.  
  * **Primary Interaction:** David will work with the Git repository, Docker images, and CI/CD pipeline definitions.  
  * **Key Needs:** His primary concerns are security, scalability, maintainability, and auditable compliance with regulatory requirements like 21 CFR Part 11\.2 He needs the system to be deployable in a controlled environment, with clear documentation for validation and operation.

### **1.2. Define the CDISC Artefacts you must support on Day 1**

To ensure immediate utility and regulatory alignment upon launch, the system will provide robust, standards-compliant support for a specific set of foundational CDISC artefacts. These have been selected to create a complete and traceable data definition pipeline from collection to submission-readiness.

**Day 1 Supported Artefacts:**

1. **CDASHIG v2.1:** The system's core mapping logic will target the Clinical Data Acquisition Standards Harmonization Implementation Guide (CDASHIG) v2.1. All extracted protocol requirements will be mapped to CDASH v2.1 variables, utilizing the official metadata table for variable names, prompts, definitions, and core designations.5 CDASH is the appropriate foundational standard as it is explicitly designed for standardizing the  
   *collection* of clinical trial data, ensuring that the generated CRFs are semantically aligned with downstream data tabulation models from the very beginning.7  
2. **CDISC Controlled Terminology (CT) \- Release 28 Mar 2025:** The system will be initialized with the latest available CT release package, which, based on the current release schedule, will be the 28 March 2025 version.9 All terminology lookups, value-level validations, and permissible value sets generated in the ODM will be explicitly tagged with this version. This strict versioning is critical for reproducibility and auditability, as regulatory bodies expect studies to use the most recent terminology available at the time of study start.12 A critical non-functional requirement is the implementation of an automated process to ingest future quarterly CT releases, as detailed in Section 3.4.  
3. **Operational Data Model (ODM) v2.0 (XML & JSON):** The system will generate its primary machine-readable output in accordance with the ODM v2.0 standard. It will produce both ODM-XML and ODM-JSON serializations to provide maximum flexibility for consuming systems.13 All generated ODM documents will be structurally validated against the official ODM 2.0 XSD and JSON Schemas as a final step in the generation process, ensuring syntactic correctness.13

### **1.3. Agree on the study-protocol inputs you will accept**

The system will be engineered with a modular importer architecture capable of processing study protocols from a variety of common file formats. The development will be prioritized based on the prevalence of the format in the industry and the reliability of data extraction from it.

**Supported Input Formats (Prioritized):**

1. **Priority 1: Microsoft Word (DOCX):** As the de facto standard for authoring clinical protocols, robust support for the DOCX format is the highest priority. The importer will leverage the python-docx library to extract not only paragraph text but also, critically, the content of tables, which frequently contain the Schedule of Assessments or other structured data elements.16  
2. **Priority 2: Structured XML:** For organizations with more advanced authoring systems capable of exporting protocols in a structured XML format, this will be the most reliable ingestion pathway. An importer based on the lxml library will use XPath expressions to precisely extract content, bypassing the ambiguities inherent in natural language parsing.18 While a standardized format like the CDISC Unified Study Definition Model (USDM) is the ideal future state, the initial implementation will support a generic structured XML.  
3. **Priority 3: Portable Document Format (PDF):** Given its widespread use for document distribution, PDF will be a supported input format. However, it will be treated as a "best-effort" format. PDF is fundamentally a presentation format, not a data interchange format. While text extraction is achievable using libraries like pdfminer-six, reliably extracting tabular data is notoriously difficult and may require complex heuristics or even fallback to optical character recognition (OCR) and computer vision techniques.20 The system's documentation will clearly state the limitations and potential for reduced accuracy when processing PDF inputs compared to DOCX or XML.  
4. **Future Consideration: FHIR ResearchStudy:** The architecture will be designed with the foresight to accommodate future importers for emerging healthcare interoperability standards. Specifically, the system will be extensible to support the HL7 Fast Healthcare Interoperability Resources (FHIR) ResearchStudy resource. This aligns with the long-term industry vision of a more integrated, digital data flow from healthcare into research.14

### **1.4. List non-functional requirements**

Beyond the core functionality, a set of critical non-functional requirements will govern the system's architecture, design, and operation. These requirements ensure the system is secure, compliant, maintainable, and strategically aligned with both regulatory and business objectives.

**Core Non-Functional Requirements:**

1. **21 CFR Part 11 Compliance:** The system must be designed to be deployable within a GxP-validated environment and to support customer compliance with 21 CFR Part 11\. This is not an optional feature but a core architectural driver, mandating the following:  
   * **Traceability & Audit Trails:** Every significant action that creates or modifies a data record (e.g., protocol ingestion, a mapping decision, CRF generation) must be recorded in a secure, computer-generated, time-stamped audit trail. This trail must be unalterable and must capture the "who, what, when, and why" of the change, including the user ID, timestamp, the action performed, original and new values (or their hashes), and a reason for the change where applicable.23 This ensures complete traceability from the source protocol to the final CRF, a key tenet of data integrity (ALCOA+).26  
   * **Security Controls:** System access must be strictly controlled. For deployed instances, this will be achieved through role-based access control (RBAC) integrated with the host organization's authentication system. For any "open system" components, such as a public-facing web UI, additional measures including encryption of data in transit (TLS 1.2+) and at rest are mandatory to ensure data integrity and confidentiality.28  
   * **Electronic Signatures:** While the tool itself will not implement e-signature workflows, its outputs must be suitable for use in such workflows. The system will generate a cryptographic hash (e.g., SHA-256) for every input and output artefact. These hashes can be included in a manifest file that is then electronically signed within a compliant e-signature system, ensuring the integrity of the signed records.  
   * **System Validation:** The entire system must be designed for validation. This includes comprehensive documentation (requirements, design specifications), a full suite of automated tests (unit, integration, regression), and a clear separation of development, testing, and production environments enforced by the CI/CD pipeline.23  
2. **Licensing Model:** A **dual-licensing model** is the recommended strategy to balance the benefits of community collaboration with the need for sustainable funding.  
   * **Core Engine (Open Source):** The central engine—comprising the protocol parsers, NLP pipeline, mapping logic, and artefact generators—will be released under a permissive open-source license, such as **MIT or Apache 2.0**. This approach fosters transparency and trust, which are vital in a regulated industry. It allows stakeholders to inspect, validate, and even contribute to the core logic, preventing vendor lock-in and encouraging broad adoption.30  
   * **Enterprise/Hosted Version (Proprietary):** A commercial version will be offered, likely as a managed, hosted service or an enterprise-deployable package. This version will build upon the open-source core, adding value-added features such as the pre-configured web UI, managed 21 CFR Part 11 compliant hosting environments, enterprise-grade support, service level agreements (SLAs), and hands-on integration services. This model provides a clear business case and revenue stream to fund the professional development and maintenance of the open-source foundation.  
3. **Deployment Constraints:** The system must be architected for portability across diverse environments. **Containerization with Docker is mandatory.** This ensures that the application and all its dependencies can be packaged into a single, immutable artefact that runs consistently on a developer's laptop, in a CI/CD pipeline, and in a validated cloud production environment.33 This approach dramatically simplifies deployment and mitigates the risk of environment-specific issues.

The interplay between these non-functional requirements is significant. For instance, the choice of a dual-licensing model directly influences the governance strategy (Section 11.3), as it necessitates a public framework for managing community contributions to the open-source core. Similarly, the stringent requirements of 21 CFR Part 11 dictate the need for a highly automated and auditable CI/CD pipeline (Section 2.3), transforming it from a mere developer convenience into a critical compliance mechanism.

To formally track and verify compliance, a detailed traceability matrix will be maintained throughout the project lifecycle.

| Regulatory Requirement | CFR Citation | System Feature | Implementation Details | Validation Method |
| :---- | :---- | :---- | :---- | :---- |
| Secure, time-stamped audit trails | 21 CFR 11.10(e) | Audit Log Service | All create, modify, or delete actions on key data entities (e.g., StudyRequirementsJSON, ODM) are logged to an immutable, append-only table in a dedicated database. Each entry records user ID, timestamp, action type, a link to the record, and hashes of before/after states. | Unit tests for log creation on every audited action. Integration tests to verify log integrity and prevent unauthorized modification. Manual inspection during validation. |
| Limited system access | 21 CFR 11.10(d) | Role-Based Access Control (RBAC) | The REST API and Web UI will integrate with an external identity provider (e.g., LDAP, OAuth 2.0). Access to specific endpoints and functions will be restricted based on user roles (e.g., Admin, User, Reviewer). | Integration tests simulating access attempts with different roles. Penetration testing to identify authorization bypass vulnerabilities. |
| System validation | 21 CFR 11.10(a) | Comprehensive Test Suite & CI/CD | A full test suite (unit, integration, regression) with \>90% code coverage. All code changes are automatically tested in a CI/CD pipeline before deployment. Formal validation documentation (URS, FRS, IQ/OQ/PQ) will be produced. | Code coverage reports. CI/CD pipeline logs serve as evidence of consistent testing. Execution of formal OQ/PQ test scripts in a validated environment. |
| Accurate and complete record copies | 21 CFR 11.10(b) | Artefact Generation and Export | The system generates human-readable (Markdown, HTML) and electronic (ODM-XML, ODM-JSON) copies of CRFs. A ZIP archive containing all outputs can be downloaded. | Regression tests compare generated outputs against a "golden" corpus. Manual review of generated files to confirm readability and completeness. |

## **Section 2: System Architecture and Technology Stack**

This section outlines the pivotal technology choices that form the system's architectural foundation. The selections prioritize performance, a rich and relevant library ecosystem, developer productivity, and long-term maintainability, all while adhering to the project's stringent functional and non-functional requirements.

### **2.1. Core Programming Language and Library Ecosystem**

A cohesive, powerful, and modern technology stack is essential for tackling the complex challenges of NLP, schema validation, and regulated data handling.

* **Decision:** The system will be built exclusively in **Python**. The core library ecosystem is defined as follows:  
  * **Web Framework:** **FastAPI** will be used to build the REST API, providing a high-performance, asynchronous foundation for the service.34  
  * **Data Validation & Serialization:** **Pydantic** will be used for all data modeling, validation, and serialization tasks. It will define the schemas for our internal data representations and API contracts.37  
  * **Natural Language Processing (NLP):** **spaCy** will be the primary NLP library, augmented by **medspaCy** for its specialized clinical text processing capabilities.40  
  * **XML Processing:** **lxml** will be used for all low-level XML parsing, generation, and validation, particularly for handling CDISC ODM-XML and XSD schemas.42  
* **Rationale and Analysis:**  
  * **Python** is the unequivocal choice due to its dominance in the data science and NLP fields. Its vast ecosystem of mature, high-quality libraries is unmatched, and its clear syntax promotes the development of maintainable code, which is critical for a long-lived project in a regulated domain.  
  * **FastAPI** is selected over alternatives like Django and Flask for several key reasons. Its native support for asyncio is crucial for building a responsive service that can handle I/O-bound operations (like reading large protocol files) without blocking. Its most compelling feature is the seamless integration with Pydantic, which automatically generates OpenAPI-compliant API documentation from Python type hints, directly fulfilling task 10.1 and dramatically improving developer productivity.34 Django is a full-stack framework with many features (e.g., ORM, admin panel) that are unnecessary for this microservice-oriented architecture, while Flask, though lightweight, would require more boilerplate code to achieve the same level of validation and documentation as FastAPI.35  
  * **Pydantic** is the cornerstone of the system's data integrity. By enforcing type hints at runtime, it ensures that all data flowing through the system—from NLP extraction to API serialization—conforms to a defined schema.37 This strict validation is not just a convenience; it is a critical feature for a system handling regulated clinical data. Its ability to produce user-friendly error messages when validation fails is also a significant benefit for debugging.38  
  * For NLP, **spaCy** is chosen over NLTK for its production-oriented design. While NLTK is a powerful research toolkit, spaCy is engineered for speed and efficiency, using an object-oriented approach and a highly optimized core written in Cython.40 The availability of  
    **medspaCy**, a dedicated extension for clinical NLP, is a decisive advantage. It provides pre-built, rule-based components for domain-specific challenges like handling clinical abbreviations, segmenting clinical sentences (which often defy standard punctuation rules), and detecting section headers, significantly accelerating development.41  
  * For XML processing, **lxml** is the only production-grade choice. The standard library's xml.etree.ElementTree lacks essential features required for this project, most notably robust and performant **XML Schema (XSD) validation**.42  
    lxml's C-based implementation provides the necessary performance for parsing and validating potentially large ODM-XML files, and its superior handling of XML namespaces is critical for correctly interpreting CDISC standards.51

The selection of this specific stack creates a powerful synergy. A single Pydantic model can define a data structure that is used as the output target for the spaCy NLP pipeline, serves as the validated internal representation for business logic, and is automatically exposed as a request/response model in the FastAPI API, complete with documentation. This tight integration minimizes code duplication and reduces the risk of data-schema mismatches between different layers of the application.

### **2.2. Selection of Templating and Static-Site Generation Tooling**

The system must generate human-readable outputs, including HTML previews of CRFs and project documentation. The tooling for these tasks should be efficient, maintainable, and aligned with the primary technology stack.

* **Decision:**  
  * **Templating Engine:** **Jinja2** is the definitive choice for all templating tasks.52  
  * **Static-Site Generator (SSG):** **MkDocs**, in combination with the **Material for MkDocs** theme, will be used to generate all HTML content, including CRF previews and the main project documentation site.53  
* **Rationale and Analysis:**  
  * **Jinja2** is the industry standard for templating in Python. It is powerful, mature, and its syntax is well-documented and widely understood by Python developers. Its features, such as template inheritance, macros, and control structures (e.g., loops, conditionals), are perfectly suited for programmatically generating structured Markdown files from the system's internal JSON representation.52 Nunjucks, being a JavaScript port, would introduce an unnecessary Node.js dependency into the backend and is a subset of Jinja2's full capabilities in a Python context.55  
  * **MkDocs** is selected over more complex, JavaScript-based alternatives like Docusaurus for its simplicity and alignment with our Python-centric stack. MkDocs is configured with a single, straightforward YAML file and generates clean, static HTML sites directly from Markdown files, which is precisely the requirement.57 While Docusaurus offers powerful React-based features like interactive components and superior versioning support, this comes with a significantly higher learning curve and maintenance overhead associated with the JavaScript ecosystem.54 For the primary goal of generating clear, readable documentation and CRF previews, the simplicity and speed of MkDocs are a better fit. The  
    **Material for MkDocs** theme provides a modern, responsive design and a rich set of features for technical documentation (e.g., excellent search, code highlighting, admonitions) out of the box, minimizing the need for custom frontend development.54

### **2.3. CI/CD Pipeline Architecture and Workflow Definition**

A robust, automated CI/CD pipeline is a non-negotiable requirement for ensuring software quality, security, and compliance.

* **Decision:** The project will implement a comprehensive CI/CD pipeline using **GitHub Actions**. A primary workflow, defined in .github/workflows/main.yml, will be triggered on every push to the main branch and on every pull request targeting main. This workflow will consist of a sequence of dependent jobs designed for a "fail-fast" approach.  
  **Workflow Jobs:**  
  1. **lint-and-format:** This initial job acts as a rapid quality gate.  
     * **Tools:** It will use ruff for combined linting and formatting checks and mypy for static type analysis.  
     * **Action:** The job will check out the code, install dependencies, and run ruff check. and mypy.. A failure in either tool will cause the job to fail, immediately halting the pipeline and providing fast feedback to the developer.  
  2. **unit-test:** This job runs only if lint-and-format succeeds.  
     * **Tools:** It will use pytest as the test runner and pytest-cov to generate code coverage reports.  
     * **Action:** The job will execute the complete unit test suite. Upon completion, it will upload the coverage report to a third-party service (e.g., Codecov) for tracking and visualization. The job will be configured to fail if any tests fail or if the code coverage percentage drops below a pre-defined threshold (e.g., 90%).  
  3. **security-scan:** This job runs in parallel with unit-test.  
     * **Tools:** It will utilize both **Bandit** to scan for common Python security vulnerabilities and **Semgrep** with its bandit ruleset for more advanced, pattern-based static application security testing (SAST).58  
     * **Action:** The job will scan the entire codebase for security issues. The workflow will be configured to fail the build if any high-severity vulnerabilities are detected, preventing insecure code from being merged.  
  4. **schema-validate-artefacts:** This crucial integration test runs only if the preceding jobs pass.  
     * **Action:** This job executes a custom Python script that invokes the core engine to generate a representative set of ODM-XML and ODM-JSON files from a small, internal test corpus. It then uses lxml and jsonschema to validate these generated files against the official CDISC schemas cached within the repository. This job verifies that the end-to-end process produces structurally compliant artefacts.  
  5. **package:** This job runs only if all previous jobs are successful.  
     * **Tools:** It will use the standard Python build package and Docker.  
     * **Action:** The job builds the Python source distribution (sdist) and wheel, and then builds the final Docker container image. These artefacts are stored temporarily using GitHub's upload-artifact action for use in the subsequent deployment job.  
  6. **deploy (Conditional):** This final job is triggered only on the creation of a tagged release on the main branch.  
     * **Action:** It downloads the artefacts from the package job. It then uses the pypa/gh-action-pypi-publish action to publish the Python package to PyPI using **Trusted Publishing**, which is a secure, tokenless authentication method.60 Finally, it pushes the Docker image to the designated container registry (e.g., GitHub Container Registry).  
* **Rationale and Analysis:**  
  * GitHub Actions is the native CI/CD solution for GitHub-hosted projects, offering seamless integration and a vast ecosystem of pre-built actions that simplify workflow creation.60  
  * The defined job sequence ensures efficiency and rigor. Fast-failing jobs like linting provide immediate feedback, while more comprehensive jobs like testing and validation run subsequently. This structure prevents wasting compute resources on builds that have basic quality issues.63  
  * The inclusion of the schema-validate-artefacts job is a critical design choice. It goes beyond typical unit testing to provide a strong guarantee that the system's primary output is compliant with the external CDISC standards, a core requirement of the project.  
  * This automated pipeline is a foundational component for meeting 21 CFR Part 11 requirements. It provides an auditable, enforceable software development lifecycle (SDLC). The logs from every workflow run serve as objective evidence that all code changes have passed a rigorous, predefined set of quality, security, and compliance checks before being merged or deployed. This transforms the abstract regulatory need for a "validated state" into a concrete, automated, and continuously verified process.63

## **Section 3: CDISC Reference Data Acquisition and Management**

This section details the critical procedures for acquiring, versioning, and managing the external CDISC standards content that our system depends on. A robust and automated approach is essential for maintaining compliance and ensuring the tool's long-term viability.

### **3.1. ODM Schema Ingestion and Typed Model Generation**

To ensure the system produces syntactically correct CDISC ODM artefacts and to provide a superior developer experience, we will programmatically ingest the official ODM schemas and generate strongly-typed Python models from them.

* **Decision:**  
  1. **Acquisition and Caching:** The official ODM-XML 2.0 XSD and the ODM-JSON 2.0 JSON Schema will be downloaded from the official CDISC sources (the CDISC website or its GitHub repositories).13 These schema files will be committed to the project's source code repository within a dedicated  
     schemas/ directory. This local caching is a critical step to ensure that all development, testing, and production builds are pinned to a specific, known version of the schemas, eliminating reliance on external network availability and protecting against unexpected upstream changes.  
  2. **Typed Model Generation from XSD:** The system will use the **xsdata** library to parse the ODM 2.0 XSD and generate a corresponding set of Python dataclasses.64 These generated classes will represent the entire ODM-XML object model, from the root  
     \<ODM\> element down to individual \<ItemData\> elements.  
  3. **Typed Model Generation from JSON Schema:** The system will use the **datamodel-code-generator** library to parse the ODM-JSON 2.0 schema and generate a corresponding set of **Pydantic** models.65 This aligns perfectly with the decision to use Pydantic for internal data validation and API modeling.  
* **Rationale and Analysis:**  
  * Generating typed models from the official schemas provides several profound advantages over manual XML/JSON manipulation. Firstly, it creates a strongly-typed, object-oriented interface for constructing ODM documents. This allows developers to work with Python objects (e.g., FormDef(), ItemDef()) instead of error-prone string concatenation or raw XML element creation, significantly reducing the risk of structural errors.  
  * Secondly, it enables modern developer tooling. With typed models, IDEs can provide intelligent code completion, and static analysis tools like mypy can catch type-related bugs before the code is even run. This drastically improves developer productivity and code quality.  
  * Finally, this approach enhances maintainability. When CDISC releases a new version of the ODM standard, the models can be regenerated. The differences in the generated code will immediately highlight the changes in the standard, guiding the necessary updates to the application logic.  
  * The choice of xsdata for XSD and datamodel-code-generator for JSON Schema is deliberate. xsdata produces modern, standard-library dataclasses, which are lightweight and integrate well with any Python code.64  
    datamodel-code-generator produces Pydantic models, which leverages the powerful validation and serialization capabilities we have already chosen for our stack, ensuring consistency across the application.65

### **3.2. Controlled Terminology (CT) Normalization and Lookup Service**

The system requires fast and reliable access to CDISC Controlled Terminology for mapping, validation, and populating permissible values in the generated CRFs.

* **Decision:**  
  1. **Acquisition:** The CDISC CT package for the specified version (initially 28 March 2025\) will be downloaded from the NCI-EVS FTP site.9 The source format will be one of the machine-readable versions, such as the text files (TSV/CSV) or the ODM-XML distribution, which are more reliable to parse than Excel or PDF.67  
  2. **Normalization and Storage:** The various raw CT files (which are separated by standard, e.g., SDTM, CDASH) will be processed by a dedicated build script. This script will parse, clean, and load the entire terminology set into a single, normalized **SQLite database file** (e.g., terminology.sqlite). This database will feature a structured schema with tables for codelists, terms, synonyms, and their relationships, with indexes on key lookup columns (e.g., codelist OID, term code) to ensure high query performance. This single SQLite file will be version-controlled in the Git repository and distributed as part of the application package.  
  3. **Lookup Service Implementation:** The application will **not** expose CT via a separate network service. Instead, a Python class, TerminologyService, will be implemented to encapsulate all interactions with the local SQLite database. This class will provide a clean, high-level API for the rest of the application, with methods such as get\_terms\_for\_codelist(codelist\_oid: str) \-\> List and is\_valid\_term(codelist\_oid: str, term\_code: str, term\_version: str) \-\> bool.  
* **Rationale and Analysis:**  
  * The choice of **SQLite** as the storage format offers the best balance of performance, portability, and simplicity for this use case. A single file database is trivial to distribute and requires no external server or dependencies. It provides the power of a relational database, including indexed lookups and complex queries, which is far superior to parsing flat files (like CSV or Parquet) at runtime.67 For the types of queries the system will perform (e.g., retrieving all terms for a given codelist), indexed lookups in SQLite will be extremely fast.  
  * Implementing the lookup functionality as an in-process Python service, rather than a separate network microservice, eliminates network latency and architectural complexity. This makes the terminology lookup a fast, reliable, local function call, simplifying the overall system design and improving performance.

### **3.3. Acquisition and Use of CDASH eCRF Examples for Test Corpora**

To ensure the system's output is not only syntactically valid but also semantically correct and aligned with industry best practices, a robust set of test cases based on official examples is required.

* **Decision:**  
  1. **Source of Examples:** We will systematically download a curated collection of eCRF examples from the official **CDISC eCRF Portal** and the **Library of CDASH CRF Examples**.69  
  2. **Format Prioritization:** For these examples, the **XML (ODM) format will be prioritized** over PDF or HTML versions.70 The ODM-XML files contain the structured metadata that represents the "ground truth" of the eCRF definition. These will serve as the "golden" files for our regression tests. The PDF versions will be used as inputs to test the capabilities and limitations of our PDF ingestion pipeline.  
  3. **Test Corpus Creation:** A representative subset of these downloaded examples will be organized into a tests/corpus/ directory within the repository. For each example, a corresponding test case will be created. This test will typically involve a synthetic protocol document designed to produce the target eCRF. The test will execute the full application pipeline—ingestion, NLP, mapping, and generation—and then perform a deep comparison between the generated ODM output and the "golden" ODM example file from CDISC.  
* **Rationale and Analysis:**  
  * Using official examples from CDISC as the basis for our validation and regression test suite is a critical quality assurance strategy. It ensures that the tool is tested against real-world, standards-compliant data structures.72  
  * This corpus directly supports the regression testing strategy outlined in Section 8.2. It provides a stable baseline against which all future code changes can be tested, ensuring that new features or bug fixes do not inadvertently break previously working functionality. This is essential for maintaining a validated state in a regulated environment.

### **3.4. Automated Ingestion Pipeline for Quarterly CT Updates**

CDISC Controlled Terminology is a moving target, with updates published quarterly.9 A manual update process is inefficient and prone to being overlooked. Therefore, an automated process is required.

* **Decision:** A scheduled **GitHub Actions workflow** will be implemented to fully automate the detection and initial processing of new CDISC CT releases.  
  1. **Detection:** The workflow will run on a weekly cron schedule. Its primary script will connect to the NCI-EVS FTP server, list the contents of the relevant CT directories (e.g., /CDISC/SDTM/), and parse the directory or file names to identify the latest release date.74 This date will be compared against the version currently used by the application.  
  2. Automated Pull Request (PR) Generation: If a new version is detected, the workflow will execute the following automated sequence:  
     a. Check out the repository to a new branch (e.g., chore/update-ct-to-YYYY-MM-DD).  
     b. Download the new CT package from the FTP site.  
     c. Execute the normalization script (from Section 3.2) to generate an updated terminology.sqlite database file.  
     d. Commit the new database file and any related configuration changes (e.g., updating the version number in a config file).  
     e. Use the GitHub CLI (gh), which is pre-installed on GitHub Actions runners, to programmatically open a pull request against the main branch. The PR description will be auto-populated with details about the new CT version.76  
  3. **Mandatory Human Review:** This automatically generated PR will **not** be merged automatically. It will be assigned to the project maintainers for review. The PR will trigger the full CI pipeline, and the results of the regression tests will be a key factor in the review. This provides a critical quality gate to assess the impact of the terminology changes before they are integrated.  
* **Rationale and Analysis:**  
  * This workflow strikes the perfect balance between automation and safety. It removes the manual toil of checking for updates while ensuring that a human-in-the-loop is present to analyze the impact of those updates.79  
  * The process of automatically creating a PR that runs the full test suite is a powerful mechanism. It forces the project to continuously validate its resilience against standards evolution. If a new CT version retires a term that is used in a regression test, the test will fail, immediately notifying the maintainers of the breaking change. This feedback loop ensures that the system's mapping and validation logic must be designed robustly to handle such changes, for example, by correctly identifying and flagging the use of retired terms from a previous CT version. This proactive, automated testing against real-world changes is far more effective than relying on theoretical resilience alone.

## **Section 4: Protocol Ingestion & Information Extraction**

This section details the most technically challenging component of the system: the pipeline responsible for ingesting unstructured or semi-structured protocol documents and transforming them into a structured, canonical representation of study requirements. This process is the foundation upon which all subsequent mapping and generation steps are built.

### **4.1. Build Importers**

A flexible, multi-format ingestion system is required to handle the variety of document types used for clinical protocols. The architecture will be modular, with a dedicated importer for each supported file type.

* **Decision:**  
  1. **DOCX Importer:** This will be the primary, most robust importer. It will use the **python-docx** library to parse the document's structure, including paragraphs, headings, and tables.17 To enhance the extraction of structured content from text, it will be supplemented with  
     **textacy**, which provides higher-level NLP preprocessing capabilities on top of spaCy.81 The  
     docx2csv library's approach to table extraction can serve as a reference for handling complex table structures.16  
  2. **PDF Importer:** This importer will use **pdfminer-six** as its core engine for extracting text content and layout information (e.g., character coordinates, bounding boxes).20 For table extraction, which is notoriously difficult in PDFs, a multi-pronged strategy will be employed:  
     * **Heuristic-based:** Attempt to reconstruct tables based on the alignment of text and the presence of vector lines (rectangles) detected by pdfminer-six.84  
     * **Library-based:** Leverage libraries like camelot or tabula-py which specialize in PDF table extraction, though they have their own dependencies (e.g., Java for Tabula) and limitations.21  
     * **Regex Fallback:** As a last resort for poorly structured PDFs, regular expressions will be used to find patterns indicative of tabular data (e.g., lists of assessments and visit names). This approach is brittle and will be used sparingly.  
  3. **Structured XML Importer:** This will be the simplest and most reliable importer. It will use the high-performance **lxml** library to parse the XML document and use **XPath** expressions to directly select and extract the required data elements from their known locations in the document tree.18  
* **Rationale and Analysis:**  
  * A modular design, where each importer is a separate class implementing a common interface (e.g., BaseImporter), allows for easy extension to support new formats in the future (e.g., FHIR ResearchStudy) without altering the core NLP pipeline.  
  * The choice of libraries is based on their fitness for purpose. python-docx provides direct access to the semantic structure of a Word document, which is far more reliable than parsing the raw XML within the .docx package.17  
    pdfminer-six is chosen for PDF because it provides low-level access to object positions on the page, which is essential for any heuristic-based table reconstruction logic.83  
    lxml is the industry standard for high-performance XML processing in Python.42

### **4.2. NLP Pipeline**

Once the raw text and table data are extracted, they must be processed through an NLP pipeline to identify and structure the key clinical concepts.

* **Decision:** The core NLP pipeline will be built using **spaCy** and **medspaCy**. It will process the ingested text in the following stages:  
  1. **Sentence Segmentation:** The first step is to break the document text into individual sentences. The standard spaCy sentencizer will be replaced with the **PyRuSH**\-based sentence splitter included in medspaCy.41  
     PyRuSH is a rule-based sentence boundary detector specifically designed for clinical text, which often contains non-standard punctuation and formatting (e.g., numbered lists, abbreviations with periods) that can confuse traditional segmenters.41  
  2. **Section Header Classification:** The pipeline will identify and classify document sections (e.g., "Schedule of Assessments," "Inclusion Criteria," "Adverse Event Reporting"). This will be implemented using the medspaCy **section detection** component, which is an evolution of the proven SecTag algorithm.87 This component uses a combination of rule-based matching against a dictionary of common section headers and machine learning techniques to identify section boundaries. This allows the subsequent pipeline stages to focus their processing on the most relevant parts of the protocol.  
  3. **Table Extraction and Interpretation:** For documents containing tables (especially the Schedule of Assessments), the extracted table data will be parsed. The logic will identify the header row and the visit columns to transform the 2D table into a structured list of assessments planned at each visit.  
  4. **Named Entity Recognition (NER):** This is the core information extraction step. A custom NER model will be trained using spaCy to identify key clinical trial concepts within the text. The target entities will include:  
     * Visit: e.g., "Screening," "Cycle 3 Day 1," "End of Treatment"  
     * Assessment: e.g., "Vital Signs," "12-lead ECG," "Blood Sample Collection"  
     * Biomarker: e.g., "serum creatinine," "hemoglobin A1c"  
     * Timing: e.g., "prior to dose," "within 30 minutes," "every 4 weeks"  
     * Population: e.g., "adult male subjects," "patients with Type II Diabetes"  
       The medspaCy framework, which builds on spaCy's NER capabilities, provides tools like the TargetMatcher that allow for rapid development using rule-based patterns, which can be used to bootstrap the training data for a more sophisticated statistical model.48  
* **Rationale and Analysis:**  
  * This staged pipeline design breaks a highly complex problem into a series of more manageable sub-problems. Classifying sections first allows the system to apply different, more targeted extraction logic to different parts of the protocol, improving accuracy. For example, NER for assessments can be focused primarily on the "Schedule of Assessments" section.  
  * medspaCy is the pivotal library choice here. Its specialized components for clinical sentence segmentation and section detection provide a massive advantage over building these from scratch.41 These tasks are well-studied problems in clinical NLP, and leveraging existing, validated solutions like SecTag/  
    medspaCy is a far more robust approach than re-implementing them.87  
  * For NER, a hybrid approach starting with rules (TargetMatcher) and evolving to a trained statistical model is the most pragmatic path. Rule-based matching is excellent for high-precision extraction of well-defined terms (e.g., specific lab tests) and can be used to generate a large volume of training data quickly. This data can then be used to train a statistical spaCy NER model, which will provide better recall and the ability to generalize to unseen or slightly varied phrasings of the target concepts.90

### **4.3. Persist a canonical Study Requirements JSON (your internal IR)**

The output of the NLP pipeline must be stored in a consistent, validated, and machine-readable format that is independent of the input source. This Internal Representation (IR) is the canonical source of truth for all subsequent steps.

* **Decision:** The extracted information will be persisted as a **Canonical Study Requirements JSON** object. The schema for this JSON will be rigorously defined and enforced using **Pydantic models**. This IR will serve as the single, validated data structure that decouples the ingestion/NLP phase from the mapping/generation phase.  
* Structure of the Canonical JSON:  
  The top-level Pydantic model (e.g., StudyProtocolIR) will contain metadata about the source protocol and a list of DataCollectionRequirement objects. Each DataCollectionRequirement will be a structured representation of a single piece of information to be collected, defined by a model like this:  
  Python  
  from pydantic import BaseModel, Field  
  from typing import List, Optional

  class Provenance(BaseModel):  
      source\_format: str  
      source\_identifier: str \# e.g., filename  
      location\_page: Optional\[int\] \= None  
      location\_line: Optional\[int\] \= None  
      location\_table\_id: Optional\[str\] \= None

  class DataCollectionRequirement(BaseModel):  
      requirement\_id: str \# A unique ID for this requirement  
      visit\_name: str  
      assessment\_name: str  
      timing\_details: Optional\[str\] \= None  
      population\_subset: Optional\[str\] \= None  
      provenance: Provenance

* **Rationale and Analysis:**  
  * **Decoupling:** Using a canonical IR is a fundamental architectural principle. It ensures that the mapping and generation logic (Sections 5 and 6\) does not need to know whether the protocol came from a DOCX, PDF, or XML file. It only needs to operate on the consistent, validated StudyProtocolIR object. This makes the system far more modular and maintainable.  
  * **Validation:** Using Pydantic to define the IR schema means that every piece of extracted information is validated before it is passed to the next stage of the pipeline.37 This prevents malformed data from propagating through the system and causing downstream errors.  
  * **Traceability:** The inclusion of a Provenance object within each DataCollectionRequirement is a critical design choice for regulatory compliance and user trust. It provides an unbreakable link back to the exact location in the source protocol (e.g., page 15, line 10, or table 3\) from which a requirement was extracted. This is essential for quality assurance, debugging, and providing an auditable trail for regulatory review.  
  * **Canonicalization:** For ensuring the integrity of this IR, especially for audit trail purposes, the final JSON output will be canonicalized according to the **JSON Canonicalization Scheme (JCS) as defined in RFC 8785**.92 This involves deterministic sorting of object keys and strict serialization rules, ensuring that the same logical content always produces the exact same byte-for-byte representation, which can then be reliably hashed.

## **Section 5: Mapping to CDISC Metadata**

This section describes the core semantic translation process: converting the extracted, canonical data collection requirements into formal CDISC metadata. This is where the system bridges the gap between the unstructured language of a protocol and the structured, standardized world of CDISC.

### **5.1. For every extracted data item, map to CDISC metadata**

For each DataCollectionRequirement in our canonical IR, the system must perform a multi-faceted mapping to the target CDISC standards.

* **Decision:** The mapping process will be a multi-step, algorithmically-driven procedure with a human-in-the-loop for quality control. For each extracted item (e.g., "Vital Signs at Screening"), the system will attempt to map it to:  
  1. **CDASH Variable Metadata:**  
     * **Mapping:** The system will use a combination of exact matching and **fuzzy string matching algorithms** to map the extracted assessment\_name to the Question Text or DRAFT CDASH Definition in the CDASHIG v2.1 metadata table.5 Algorithms like  
       **Levenshtein distance** or **Jaro-Winkler distance** will be employed to handle minor variations in terminology (e.g., "Vital Sign" vs. "Vital Signs").94  
     * **Output:** The result will be a mapping to a specific CDASH variable (e.g., VSPOS), along with its associated metadata: label, datatype, and role.  
  2. **CDISC Controlled Terminology (CT):**  
     * **Mapping:** If the CDASH variable is associated with a codelist (as specified in the Controlled Terminology Codelist Name column of the CDASH metadata), the system will link the data item to that codelist's OID.  
     * **Output:** The mapping will include the CodeListOID and, critically, the **version of the CT package** being used (e.g., "2025-03-28") to ensure traceability.9  
  3. **Planned SDTM Domain:**  
     * **Mapping:** The CDASHIG metadata provides a direct mapping from a CDASH variable to its target SDTM domain (e.g., VS for Vital Signs, AE for Adverse Events).5 The system will use this information to annotate the mapped item with its planned SDTM destination.  
     * **Output:** The mapping will include the target SDTM domain (e.g., SDTMDomain \= "VS").  
* **Rationale and Analysis:**  
  * This multi-step mapping process directly translates the raw protocol requirement into a fully specified, CDISC-compliant data point definition. The explicit goal of CDASH is to facilitate this downstream mapping to SDTM, and by leveraging the metadata provided in the CDASHIG, we are following the intended data flow.7  
  * The use of fuzzy matching is a pragmatic necessity. Clinical terminology is not always consistent across protocols. A simple exact match would fail on minor variations. Fuzzy matching algorithms provide the flexibility to identify likely matches, which can then be confirmed or corrected by a human reviewer.99 The similarity score from the fuzzy match can be used as a confidence score for the mapping.  
  * Traceability to the planned SDTM domain is a key benefit of using CDASH. It provides a clear line of sight from data collection all the way to data tabulation for regulatory submission, which is a core principle of the CDISC framework.101

### **5.2. Flag any unmapped items and surface them in a QA report**

Automated mapping will not be perfect. There will inevitably be protocol-specific assessments that do not have a clear equivalent in the standard CDASH domains. The system must handle these exceptions gracefully and transparently.

* **Decision:**  
  1. **Flagging:** Any DataCollectionRequirement from the canonical IR that cannot be mapped to a CDASH variable with a confidence score above a configurable threshold will be flagged as "unmapped."  
  2. **QA Report Generation:** After the mapping process completes, the system will generate a **Quality Assurance (QA) and Curation Report**. This report will be produced in two formats:  
     * **JSON:** A machine-readable format for integration with other systems.  
     * **HTML:** A human-readable format designed for review by a Data Manager or Study Designer.  
  3. **Report Content:** The report will clearly list all unmapped items. For each item, it will provide:  
     * The full details of the extracted requirement (visit, assessment name, etc.).  
     * The provenance (link back to the source protocol page/line).  
     * A list of the top 3-5 "best guess" CDASH variables identified by the fuzzy matching algorithm, along with their similarity scores.  
     * An interface (in the HTML report) for a human reviewer to either select one of the suggested mappings, manually enter a different CDASH variable, or flag the item as a truly custom variable that requires addition to a supplemental qualifier (SUPPQUAL) domain.  
* **Rationale and Analysis:**  
  * This "human-in-the-loop" design is critical for building a trustworthy and practical system. It acknowledges the limitations of automation and empowers the user to make the final, authoritative decisions for ambiguous cases.103  
  * The QA report is the primary interface for this curation workflow. By presenting the unmapped items along with intelligent suggestions, it dramatically speeds up the manual review process. The user is not starting from scratch but is guided towards the most likely correct mappings.  
  * This process is essential for handling non-standard variables, which are common in clinical trials. The SDTM standard has a defined mechanism for handling such variables (the SUPPQUAL domains), and this QA workflow provides the necessary input to correctly populate those domains.97 This ensures that even custom, study-specific data is handled in a standards-compliant manner.

### **5.3. Generate an ODM block per variable; group into by CRF**

Once all data items have been mapped (either automatically or through human curation), the final step is to translate these mappings into a structured, machine-readable format.

* **Decision:** The system will generate a set of **CDISC ODM 2.0** data structures. The generation process will follow the ODM hierarchy:  
  1. **ItemDef:** For each successfully mapped data collection requirement, a corresponding \<ItemDef\> element will be created in the ODM structure. This ItemDef will be populated with the metadata derived from the mapping process:  
     * OID: A unique Object Identifier will be generated (e.g., IT.VS.VSORRES.SYSTOLIC).  
     * Name: The CDASH variable name (e.g., VSSYSBP).  
     * DataType: The data type from the CDASH metadata (e.g., integer, text).  
     * \<Question\>: The Question Text from the CDASH metadata.  
     * \<CodeListRef\>: A reference to the appropriate CodeListOID if the variable uses controlled terminology.  
  2. **ItemGroupDef:** Related ItemDefs will be grouped into an \<ItemGroupDef\> element, which represents a logical collection of fields on a form (e.g., all the vital signs measurements).  
  3. **FormDef:** One or more ItemGroupDefs will be collected into a \<FormDef\> element, which represents a complete CRF (e.g., "Vital Signs Form").  
  4. **Serialization:** The entire collection of Study, MetaDataVersion, FormDef, ItemGroupDef, and ItemDef objects will be serialized into both **ODM-XML 2.0** and **ODM-JSON 2.0** formats, using the typed models generated in Section 3.1.  
* **Rationale and Analysis:**  
  * Generating ODM is the primary goal of the system's backend. ODM is the industry standard for exchanging clinical trial metadata and is the format expected by most modern EDC systems for study builds.105  
  * By structuring the output according to the standard ODM hierarchy (FormDef contains ItemGroupDef contains ItemRef), we ensure the generated files are compliant and immediately usable by downstream systems.8  
  * The use of the typed Python models generated from the ODM schemas makes this generation process robust and less error-prone. We are constructing a valid object graph in Python, which is then serialized to XML or JSON, rather than manually building the output strings. This guarantees that the output is structurally correct before it is even written to a file.  
  * Providing both XML and JSON serializations of the ODM increases the interoperability of the tool, catering to both legacy systems that expect XML and modern systems that may prefer JSON.13

## **Section 6: Markdown CRF Generator**

While the ODM output is essential for machine consumption, a human-readable representation is equally important for review, documentation, and collaboration. This section details the generation of user-friendly Markdown versions of the CRFs.

### **6.1. Design a YAML front-matter schema for CRF metadata**

To ensure that the generated Markdown files are self-describing and contain all necessary metadata for both human readers and downstream processing (like the static site generator), each file will begin with a structured YAML front-matter block.

* **Decision:** A standardized YAML front-matter schema will be defined and applied to every generated Markdown CRF file. This schema will capture key metadata about the form and its context within the study.  
  **Proposed YAML Front-Matter Schema:**  
  YAML  
  \---  
  crf\_id: "FRM.VS"  
  crf\_name: "Vital Signs"  
  crf\_version: "1.0"  
  study\_protocol\_id: "XYZ-123"  
  source\_protocol\_version: "3.0"  
  source\_protocol\_filename: "protocol\_v3.docx"  
  cdisc\_cdash\_version: "2.1"  
  cdisc\_ct\_version: "2025-03-28"  
  last\_modified: "2025-07-15T10:30:00Z"  
  status: "Draft"  
  \---

* **Rationale and Analysis:**  
  * **Standardization:** YAML front-matter is a widely adopted convention in static site generators (like Jekyll, Hugo, and our chosen MkDocs) and content management systems for embedding structured metadata within text files.107 Adopting this standard makes our output compatible with a broad range of tools.  
  * **Traceability and Context:** The schema is designed to provide complete context and traceability. Fields like study\_protocol\_id, source\_protocol\_version, cdisc\_cdash\_version, and cdisc\_ct\_version explicitly document the exact versions of all source and standard artefacts used to generate the CRF. This is critical for auditability and reproducibility, aligning with 21 CFR Part 11 principles.  
  * **Machine Readability:** While intended for human review, the YAML block is also machine-readable. This allows other tools or scripts to easily parse the metadata of each CRF file without needing to parse the Markdown content itself. For example, a script could quickly inventory all CRFs and their associated CT versions.  
  * **Best Practices:** The schema follows best practices by including essential identifiers (crf\_id), human-readable names (crf\_name), versioning information, and timestamps (last\_modified).108 Using clear, descriptive keys and consistent indentation is paramount.107

### **6.2. Create Jinja templates that loop through the ODM JSON and render sections**

The core of the Markdown generation process is the transformation of the structured ODM data into formatted text. This will be achieved using a powerful and flexible templating engine.

* **Decision:** A suite of **Jinja2 templates** will be created to render the canonical ODM JSON data into well-formatted Markdown files. The templating logic will be modular, with a main template and several included sub-templates for different components of a CRF.  
  **Template Design Strategy:**  
  1. **Input Data:** The templates will take the **ODM-JSON** representation of the study design as their input context. This is a clean, structured data source that is easy to iterate over in Jinja2.  
  2. **Main Template (crf.md.j2):** This template will define the overall structure of a CRF document. It will render the YAML front-matter first, followed by a main title. It will then loop through the FormDef objects in the input data.  
  3. **Nested Loops for Structure:** The templates will use nested loops to traverse the ODM hierarchy. The main template will loop through forms. Within that loop, it will include a sub-template that loops through the ItemGroupDefs (question groups) within that form. That sub-template, in turn, will include another template to loop through the ItemDefs (individual questions) within each group.52  
  4. **Component Sub-Templates:**  
     * \_header.md.j2: Renders the main CRF header information (e.g., Form Name, Instructions).  
     * \_item\_group.md.j2: Renders a question group, typically as a Level 2 Markdown heading (\#\#) followed by the questions.  
     * \_item.md.j2: Renders a single question. This template will contain logic to display the question text, data type, and any permissible values from a codelist. For codelists, it will render them as a bulleted list or a table.  
     * \_footer.md.j2: Renders any footer information, such as version details.

**Example Jinja2 Snippet (for \_item.md.j2):**Django  
\*\*{{ item.Question.TranslatedText }}\*\* (\`{{ item.OID }}\`)

\- \*\*Data Type:\*\* \`{{ item.DataType }}\`  
{% if item.CodeListRef %}  
\- \*\*Permissible Values (Codelist: {{ item.CodeListRef.CodeListOID }}):\*\*  
  \<ul\>  
  {% for code\_item in get\_codelist\_terms(item.CodeListRef.CodeListOID) %}  
    \<li\>\`{{ code\_item.CodedValue }}\` \- {{ code\_item.Decode.TranslatedText }}\</li\>  
  {% endfor %}  
  \</ul\>  
{% endif %}

* **Rationale and Analysis:**  
  * Jinja2 is the ideal tool for this task due to its Python heritage and powerful feature set, including loops, conditionals, template inheritance, and macros.52 This allows for the creation of clean, maintainable templates that separate presentation logic from the core application code.  
  * Using nested loops to iterate through the FormDef \-\> ItemGroupDef \-\> ItemDef hierarchy is a natural way to map the hierarchical structure of the ODM model to a hierarchical document structure in Markdown.110  
  * A modular template design using include statements makes the system more maintainable. Changes to how a single item is rendered can be made in one place (\_item.md.j2) without affecting the overall structure of the CRF.

### **6.3. Emit Git-friendly.md files alongside the source ODM JSON**

For review and version control, it is beneficial to have both the human-readable Markdown and the machine-readable source available, and to be able to easily see what has changed between versions.

* **Decision:** For each generated CRF, the system will output two files into the designated output directory:  
  1. **.md:** The human-readable Markdown file, generated by the Jinja2 templates.  
  2. **.odm.json:** The canonical, machine-readable ODM-JSON fragment that was used as the source data for rendering the Markdown file.  
* **Rationale and Analysis:**  
  * **Duality for Review:** Providing both representations serves different review purposes. A clinical expert or study designer can easily review the formatted .md file. A data manager or EDC programmer can inspect the .odm.json file to verify the technical metadata.  
  * **Git-Friendliness and Diffs:** This approach is inherently Git-friendly. Both Markdown and JSON are plain-text formats, which means that git diff can be used effectively on them. When a change is made to the protocol that results in a change to a CRF, a reviewer can see the exact changes in both the human-readable and machine-readable formats.  
  * Markdown itself can be made more "diff-friendly." For example, GitHub Flavored Markdown supports a diff language block where added lines are prefixed with \+ and removed lines with \-, creating a visual representation of changes directly within the document, which can be useful for changelogs or documentation.111 While our primary output won't be a diff, the plain-text nature of Markdown is what enables this capability and makes it superior to binary formats for version control.  
  * Storing the source JSON alongside the rendered output also ensures a complete, self-contained artefact. It guarantees that the exact data used to generate the Markdown file is preserved with it, which is another important aspect of traceability and reproducibility.

## **Section 7: Validation Layer**

A multi-layered validation framework is essential to ensure that all generated artefacts are compliant, correct, and trustworthy. Validation is not a single step but a continuous process that checks for structural integrity, adherence to business rules, and semantic correctness.

### **7.1. ODM structural validation: run every generated ODM document through the 2.0 XML/JSON schema**

The first layer of validation ensures that the generated files conform to the fundamental syntax and structure of the CDISC ODM standard.

* **Decision:** Every ODM-XML and ODM-JSON file generated by the system will be subjected to strict schema validation as a final, non-negotiable step in the generation pipeline.  
  1. **XML Validation:** For ODM-XML files, the system will use the **lxml** library to validate the document against the cached **ODM 2.0 XSD schema** (acquired in Section 3.1). The XMLSchema.validate() method will be used for this purpose.49  
  2. **JSON Validation:** For ODM-JSON files, the system will use the **jsonschema** library to validate the document against the cached **ODM 2.0 JSON Schema**.  
  3. **Error Handling:** If validation fails for any generated document, the process will halt, and the specific validation errors (e.g., "Element 'c': This element is not expected.") will be logged and included in the final validation report. The invalid file will not be saved to the final output directory.  
* **Rationale and Analysis:**  
  * Structural validation is the most basic and fundamental check of compliance. It ensures that the generated files are well-formed and can be parsed by any other standards-compliant tool.105  
  * Using lxml for XSD validation is the industry standard in Python. It is highly performant and provides detailed error logs that are invaluable for debugging issues in the generation logic.50 The  
    odmlib package also provides a higher-level wrapper around lxml for validation, which could be leveraged.113  
  * This validation step, integrated into the CI/CD pipeline (as job schema-validate-artefacts in Section 2.3), acts as a critical regression test. It guarantees that no code change can be merged if it results in the generation of a structurally invalid ODM document.

### **7.2. CDISC rules validation**

Beyond structural correctness, the content of the ODM file must adhere to the specific business rules and controlled terminology defined by CDISC standards.

* **Decision:** A second layer of validation will check for compliance with CDISC business rules and controlled terminology.  
  1. **Variable Name Validation:** The system will check that all mapped variable names (e.g., DM.ARMCD, VS.VSPOS) exist in the official **CDASH v2.1 specification** metadata.5 Any variable that is not a standard CDASH variable must be explicitly flagged as a custom variable (destined for a SUPPQUAL domain).  
  2. **Controlled Terminology (CT) Validation:** For every data point (ItemDef) that references a codelist (CodeListRef), the system will perform a value-level compliance check. This involves:  
     * Verifying that the CodeListOID exists in the version of the CT specified for the study.  
     * For each permissible value (CodeListItem), verifying that its CodedValue is a valid term within that codelist.  
     * Checking for compliance with other CT-related rules, such as data type and length constraints for TEST/TESTCD pairs.9  
  3. **Leveraging CDISC CORE:** The long-term strategy will be to integrate with the **CDISC Open Rules Engine (CORE)** project.115 As CORE matures and publishes its executable conformance rules, our system will invoke the CORE engine (or its underlying library,  
     cdisc-rules-engine 116) to run the official set of CDISC and regulatory business rules against our generated data. This will provide a much more comprehensive validation than we could develop in-house. Commercial tools like Pinnacle 21 also perform this function and serve as a model for the types of checks required.117  
* **Rationale and Analysis:**  
  * This layer of validation moves from syntactic correctness to semantic correctness. It's not enough for an ODM file to be well-formed; its content must accurately reflect the CDISC standards.  
  * Validating against the CDASH specification and the CT package ensures that the generated CRFs are not just "inspired by" CDISC but are truly compliant. This is critical for downstream data integration and regulatory submission.118  
  * Aligning with the CDISC CORE project is a strategic decision that future-proofs the system. By leveraging the official, community-vetted, open-source rules engine, we ensure that our validation logic will remain up-to-date with the latest conformance rules published by CDISC and regulatory agencies like the FDA.115 This avoids the significant and ongoing effort of manually implementing and maintaining hundreds of complex business rules.

### **7.3. Produce a consolidated validation log**

The results of all validation checks must be presented to the user in a clear, actionable format.

* **Decision:** At the end of the entire generation and validation process, the system will produce a single, consolidated validation log. This log will be available in two formats:  
  1. **validation-log.json:** A structured, machine-readable JSON file. This allows for programmatic processing of the validation results, such as displaying them in a web UI or feeding them into a quality management system.  
  2. **validation-log.html:** A human-readable HTML report. This report will be generated from the JSON log using a Jinja2 template. It will provide a clear, color-coded summary of the validation results, with sections for each type of check (Structural, CDASH, CT). Errors, warnings, and informational messages will be clearly distinguished.  
* **Structure of the JSON Log:**  
  JSON  
  {  
    "summary": {  
      "status": "FAILED",  
      "total\_checks": 152,  
      "errors": 2,  
      "warnings": 5  
    },  
    "results":  
  }

* **Rationale and Analysis:**  
  * Providing both JSON and HTML formats serves both machine and human consumers, a principle followed throughout this project's design.120  
  * A consolidated log is far more user-friendly than a collection of disparate log files from different validation steps. It provides a single source of truth for the quality of the generated artefacts.  
  * The structure of the log is designed to be actionable. Each result includes a clear status, a human-readable message, and, for errors, a link back to the specific item and its provenance in the source protocol. This allows users to quickly identify the root cause of a validation failure and address it, either by correcting the protocol or adjusting the mapping.

## **Section 8: Testing & Quality Control**

A rigorous and multi-faceted testing strategy is fundamental to building a reliable, high-quality software system, especially one intended for use in a regulated industry. This section outlines the quality control measures that will be implemented throughout the development lifecycle.

### **8.1. Unit tests for each parser, mapper, and template component**

Unit tests form the foundation of the testing pyramid. They are designed to test individual components (functions, classes) in isolation to verify their correctness.

* **Decision:** A comprehensive suite of unit tests will be developed using the **pytest** framework. Every significant component of the system will have dedicated unit tests.  
  * **Parsers:** Each protocol importer (DOCX, PDF, XML) will have tests that feed it small, targeted documents and assert that the correct text and table structures are extracted.  
  * **NLP Components:** The custom NLP components, such as the NER model, will be tested in isolation. For rule-based extractors, tests will provide sample text and assert that the correct entities are identified. For statistical models, tests will run the model on a small set of benchmark sentences and assert that the output meets a minimum quality threshold.  
  * **Mappers:** The mapping logic will be tested by providing it with canonical IR objects and asserting that they are correctly mapped to CDASH variables and CT codelists. External dependencies, like the TerminologyService, will be mocked using pytest-mock to isolate the mapping logic itself.121  
  * **Template Components:** Each Jinja2 template will be tested by rendering it with sample ODM JSON data and asserting that the generated Markdown output contains the expected content and structure.  
* **Rationale and Analysis:**  
  * pytest is the modern standard for testing in Python. Its use of plain assert statements, powerful fixture system, and rich plugin ecosystem make it far more productive and maintainable than the standard library's unittest.122  
  * Unit testing each component in isolation is a core software engineering best practice. It allows for precise identification of failures. If a test for the DOCX parser fails, the problem is known to be in that parser, not in the downstream NLP or mapping code.  
  * Mocking external dependencies is crucial for true unit testing. For example, when testing a mapping function, we want to test the logic of that function, not the correctness of the database query in the TerminologyService. pytest-mock provides a clean, fixture-based approach to mocking that integrates seamlessly with pytest.121

### **8.2. Regression test protocols: maintain a small corpus of public protocols and expected CRF outputs**

While unit tests verify individual components, regression tests verify that the system as a whole continues to work correctly as it evolves.

* **Decision:** A regression testing framework will be established based on a curated corpus of clinical trial protocols.  
  1. **Corpus Creation:** As described in Section 3.3, we will build a test corpus using the **CDASH eCRF examples from CDISC** and, where available, public-domain clinical trial protocols.  
  2. **Golden Files:** For each protocol in the corpus, a "golden file" of the expected output (the canonical ODM-JSON) will be created and checked into the repository. Initially, this may be created manually, but as the tool matures, its own validated output will become the golden file for future runs.  
  3. Test Execution: The regression test suite will iterate through the corpus. For each protocol, it will:  
     a. Run the entire end-to-end pipeline (ingest → parse → map → generate).  
     b. Compare the newly generated ODM-JSON output against the corresponding "golden file."  
     c. The test will fail if there are any unexpected differences.  
  4. **CI Integration:** The full regression test suite will be executed as part of the CI/CD pipeline on every pull request, ensuring that no change that breaks existing functionality can be merged.  
* **Rationale and Analysis:**  
  * Regression testing is the primary safeguard against introducing new bugs while fixing old ones or adding new features. A comprehensive regression suite provides confidence that the system remains stable over time.124  
  * Using a corpus of real or realistic protocols makes the tests much more meaningful than using purely synthetic data. It ensures the system is being tested against the kind of complexity and variability it will encounter in production.127  
  * The "golden file" approach is a standard pattern for regression testing complex data transformations. It provides a concrete, version-controlled definition of "correctness" for each test case. When a change is made that intentionally alters the output, the golden file can be updated as part of the same pull request, making the change explicit and reviewable.

### **8.3. Integrate code-coverage, linting, and security scans**

To ensure a high standard of code quality and security, several automated analysis tools will be integrated directly into the development workflow.

* **Decision:** The following tools will be integrated into the CI/CD pipeline (as detailed in Section 2.3):  
  1. **Code Coverage:** **coverage.py**, via the pytest-cov plugin, will be used to measure the percentage of the codebase that is executed by the test suite. A minimum coverage threshold (e.g., 90%) will be enforced in the CI pipeline.128  
  2. **Linting and Formatting:** **ruff** will be used for both linting (checking for stylistic errors and potential bugs) and code formatting. A single, consistent code style will be enforced across the entire project.  
  3. **Security Scanning:** **Bandit** and **Semgrep** will be used for Static Application Security Testing (SAST). Bandit is excellent for finding common, known security issues in Python code, while Semgrep allows for the definition of more complex, custom rules to find potential vulnerabilities specific to our application's logic.58  
* **Rationale and Analysis:**  
  * These automated quality gates are essential components of a modern, professional software development process. They catch entire classes of errors automatically, freeing up human reviewers to focus on the logic and architecture of code changes.  
  * **Code coverage** is a useful (though imperfect) metric for identifying areas of the code that are untested and therefore at higher risk of containing bugs.128 Enforcing a high coverage threshold encourages developers to write comprehensive tests.  
  * **Linting and consistent formatting** improve code readability and maintainability, which is critical for a long-term project, especially one that may involve open-source contributors.  
  * **Automated security scanning** is a fundamental requirement for any system that will handle potentially sensitive data or be exposed to the internet. Integrating SAST tools into the CI pipeline ensures that security is considered continuously throughout the development process ("shifting left"), rather than as an afterthought.59

## **Section 9: Packaging & Deployment**

This section details how the completed software will be packaged, distributed, and deployed, providing clear and distinct interfaces for its different user personas. The strategy emphasizes portability, ease of use, and consistency across environments.

### **9.1. Provide both a CLI and a REST API**

To meet the needs of both interactive power users and automated systems, the application will expose its core functionality through two primary interfaces.

* **Decision:** The system will be architected to provide both a Command-Line Interface (CLI) and a RESTful API.  
  1. **CLI (crf-gen):** A dedicated CLI tool will be created using the **click** library. It will provide a simple, intuitive command structure for generating CRFs from a local protocol file.  
     * **Example Usage:** crf-gen protocol.docx \--output-dir out/ \--ct-version 2025-03-28  
     * **Features:** The CLI will support options for specifying the input file, output directory, target CDISC versions, and other key parameters. It will provide clear progress indicators and print the validation report to the console upon completion.130  
  2. **REST API:** The API will be built using **FastAPI**. It will expose endpoints for the same core functionality.  
     * **Example Endpoint:** POST /generate  
     * **Request Body:** The request will be a multipart/form-data payload containing the protocol file and a JSON object with configuration options (e.g., ct\_version).  
     * **Response:** A successful request will return a JSON object containing the validation report and URLs to download the generated artefacts (a ZIP file containing the Markdown and ODM files). An unsuccessful request will return a structured error response with a 4xx or 5xx status code.  
* **Rationale and Analysis:**  
  * **click vs. argparse:** While argparse is part of the Python standard library, **click** is the superior choice for building modern, user-friendly CLIs.130 Its declarative, decorator-based approach makes it easier to create complex CLIs with nested subcommands, automatic help page generation, and rich parameter types. This leads to more maintainable and intuitive code compared to the more verbose setup required by  
    argparse.133  
  * **Dual Interfaces:** Providing both a CLI and a REST API is a strategic decision to maximize the tool's addressable audience. Data managers and programmers working locally will appreciate the power and scriptability of the CLI.4 Enterprise systems, EDC platforms, and automated CRO workflows will require the REST API for system-to-system integration.1 The core logic will be shared between both interfaces, ensuring consistent behavior and reducing code duplication.

### **9.2. Containerise with Docker; publish images to a registry**

To ensure portability, consistency, and ease of deployment, the entire application will be containerized.

* **Decision:** The application and all its dependencies will be packaged into a **Docker image**. A Dockerfile will be maintained in the root of the repository. This image will be built and tested as part of the CI/CD pipeline. Upon a tagged release, the final image will be published to a public container registry, such as **GitHub Container Registry** or Docker Hub.  
* **Dockerfile Strategy:**  
  * **Base Image:** The image will be based on an official, slim Python base image (e.g., python:3.11-slim) to keep the final image size small.  
  * **Multi-Stage Build:** A multi-stage build will be used to optimize the image. A builder stage will install build-time dependencies and compile the Python package. The final runtime stage will copy only the necessary installed application code and dependencies from the builder stage, resulting in a smaller, more secure production image.  
  * **Dependency Management:** The Dockerfile will copy the requirements.txt or pyproject.toml file and install dependencies in a separate layer before copying the application source code. This leverages Docker's layer caching, so that dependency installation is skipped if the requirements have not changed, speeding up subsequent builds.33  
  * **Entrypoint:** The container's ENTRYPOINT will be configured to run the FastAPI application using an ASGI server like uvicorn. The CLI will be accessible by overriding the entrypoint (e.g., docker run \<image\> crf-gen...).  
* **Rationale and Analysis:**  
  * Containerization solves the "it works on my machine" problem. It bundles the application, the specific version of Python, and all system and Python dependencies into a single, portable unit that runs identically everywhere.33  
  * This is essential for a tool used in a regulated environment. It allows a CRO or sponsor to pull a specific, version-tagged image and deploy it into their validated environment with a high degree of confidence that it will behave exactly as it did in the development and testing environments.  
  * Publishing to a public registry makes the tool easily accessible to the entire community. A user can get started with a single docker pull command.

### **9.3. Optional: Offer a single-page web UI that lets users upload a protocol and download a ZIP**

To cater to non-technical users like study designers, a simple, browser-based interface is highly desirable.

* **Decision:** An optional **Single-Page Application (SPA)** will be developed. This will be a lightweight frontend that interacts with the backend REST API.  
  * **Technology:** The SPA will be built using a modern JavaScript framework, with **React** (using Vite for scaffolding) being the recommended choice due to its vast ecosystem and developer pool.136 A component library like  
    **Chakra UI** will be used for styling to accelerate development.  
  * **Functionality:** The UI will be minimal and focused on a single workflow:  
    1. A file upload component allows the user to select a protocol document (DOCX or PDF) from their local machine.137  
    2. An "Upload and Generate" button sends the file to the /generate endpoint of the FastAPI backend.  
    3. While processing, the UI will display a loading indicator.  
    4. Upon completion, the UI will display the HTML validation report and provide a download link for a ZIP archive containing all the generated artefacts (Markdown CRFs, ODM files, logs).  
  * **Deployment:** The SPA will be a separate static asset. It can be served directly by FastAPI's StaticFiles middleware for simple deployments or hosted independently on a static hosting service (like GitHub Pages or AWS S3) for larger-scale deployments.138  
* **Rationale and Analysis:**  
  * A web UI dramatically lowers the barrier to adoption for users who are not comfortable with command-line tools or API clients.3 This is critical for engaging with clinical experts and study designers.  
  * Keeping the UI as a separate, simple SPA that communicates with the existing REST API is a clean architectural choice. It reuses the already-built backend logic and avoids mixing frontend and backend code, adhering to the principle of separation of concerns.136  
  * Using established tools like React and Vite allows for rapid development of a modern, responsive user interface. Libraries like Filestack or simple HTML forms can handle the file upload component, which is a well-understood problem.140

## **Section 10: Documentation & Onboarding**

Effective documentation is as crucial as the software itself. It empowers users, reduces the support burden, and fosters a healthy community. The documentation strategy will be comprehensive, targeting different user personas with tailored content.

### **10.1. Auto-generate API docs with OpenAPI / Swagger**

For developers and systems integrators, clear, accurate, and interactive API documentation is essential.

* **Decision:** The REST API documentation will be **automatically generated** using the native capabilities of **FastAPI**.  
  * **Mechanism:** FastAPI inspects the Pydantic models and type hints used in the API's path operation functions to generate an **OpenAPI 3.0 schema**.34 This schema is then used to render two interactive documentation interfaces, which will be available by default on a running instance of the service:  
    1. **Swagger UI:** Available at the /docs endpoint. This interface provides a comprehensive, interactive view of all endpoints, their parameters, request bodies, and response models. It includes a "Try it out" feature that allows users to make live API calls directly from their browser.142  
    2. **ReDoc:** Available at the /redoc endpoint. This provides an alternative, clean, three-pane layout for API documentation.142  
  * **Customization:** The auto-generated OpenAPI schema can be customized to include additional details, such as examples, descriptions, and custom metadata, by modifying the FastAPI application object.143  
* **Rationale and Analysis:**  
  * This "documentation-as-code" approach is a cornerstone of the FastAPI framework and a primary reason for its selection. It eliminates the common problem of API documentation becoming outdated. The documentation is always an exact reflection of the code's implementation because it is generated directly from it.34  
  * This directly and completely fulfills the task requirement without needing a separate documentation tool or manual writing process for the API reference. This saves significant development and maintenance effort.

### **10.2. Write a “How we map protocols to CDISC” guide with examples**

For users to trust and effectively use the tool, they need to understand its internal logic, especially the complex mapping process.

* **Decision:** A detailed technical guide titled **"Protocol to CDISC: The Mapping Process Explained"** will be written. This guide will be a central piece of the project's documentation, hosted on the MkDocs site.  
* **Content of the Guide:** The guide will follow best practices for writing effective technical documentation.144  
  1. **Audience and Objective:** Clearly state that the guide is for data managers and study designers who want to understand the tool's logic. The objective is to provide transparency into the automated mapping process.  
  2. **High-Level Overview:** Start with a flowchart or diagram illustrating the entire pipeline: Protocol Ingestion → NLP Extraction → Canonical IR → Semantic Mapping → Validation → Artefact Generation.  
  3. **Detailed Step-by-Step Explanation:** Break down the complex mapping process into manageable sections:  
     * **Information Extraction:** Explain how entities like Visit, Assessment, and Timing are identified using the NLP pipeline. Provide concrete examples of protocol text and the corresponding extracted data.  
     * **Semantic Mapping to CDASH:** Detail the process of matching an extracted Assessment to a CDASH variable. Explain the use of both exact and fuzzy matching, and show an example of how "Blood Pressure Measurement" is mapped to the relevant VS domain variables.  
     * **Controlled Terminology Linkage:** Explain how a mapped variable is linked to a specific CT codelist and version.  
     * **Handling Unmapped Items:** Describe the process for flagging unmapped items and how they are presented in the QA report for human curation.  
  4. **Use of Visuals and Examples:** The guide will be rich with visuals. It will include screenshots of protocol text, snippets of the resulting canonical JSON, and the final Markdown CRF output to illustrate the end-to-end transformation for a few key examples (e.g., Demographics, Vital Signs, Adverse Events).  
  5. **Review and Revision:** The guide will be treated as a living document, reviewed by both technical and clinical experts, and updated as the mapping logic evolves.  
* **Rationale and Analysis:**  
  * Transparency is key to trust, especially for an automated tool used in a regulated setting. This guide demystifies the "black box" of the NLP and mapping engine, allowing users to understand, validate, and rely on its output.103  
  * A well-written guide, following principles of clarity, structured formatting, and audience awareness, will significantly improve user onboarding and reduce the need for direct support.145

### **10.3. Publish versioning policy (how often you update CDISC references, semantic-versioning of your tool)**

Users need to understand how the tool's versions relate to the versions of the standards it supports to ensure they are using a compliant combination for their studies.

* **Decision:** A clear and public **Versioning Policy** will be published as part of the main documentation. This policy will cover both the tool itself and the CDISC standards it references.  
  1. **Tool Versioning:** The software will strictly adhere to **Semantic Versioning 2.0.0 (SemVer)**.148 The version number will be in the format  
     MAJOR.MINOR.PATCH.  
     * **MAJOR** version will be incremented for incompatible API changes or when support for a major, backward-incompatible CDISC standard is introduced (or an old one is removed).  
     * **MINOR** version will be incremented when new, backward-compatible functionality is added, or when support for a new, backward-compatible version of a CDISC standard (e.g., a new CT release) is added.  
     * **PATCH** version will be incremented for backward-compatible bug fixes.  
  2. **CDISC Standards Versioning:** The policy will state:  
     * The specific versions of CDASH, ODM, and CT that the current version of the tool was built and validated against.  
     * The process for updating standards, as defined in the steering document (Section 11.1).  
     * For Controlled Terminology, it will explicitly state the goal of supporting the new quarterly release within one MINOR release cycle of its publication by CDISC.  
* **Rationale and Analysis:**  
  * Semantic Versioning is the industry standard for communicating the nature of changes in software releases. Adhering to it allows users to manage dependencies and upgrades in a predictable way.149 For example, a user can safely upgrade from version 2.3.1 to 2.3.5, knowing that no breaking changes have been introduced.  
  * Publishing a clear policy on how CDISC standards versions are handled provides the predictability and transparency required by users in a regulated environment. A data manager starting a new study can consult the policy to know exactly which version of the tool and which version of the CT to use to be compliant with their company's SOPs and regulatory expectations.12

## **Section 11: Governance & Future-Proofing**

This section outlines the strategic policies and frameworks required to ensure the long-term viability, compliance, and community health of the project. A proactive governance model is essential for a tool that operates in the dynamic and highly regulated clinical research landscape.

### **11.1. Create a steering document for managing future CDISC standard versions**

The CDISC standards upon which this tool is built are not static. A formal process is required to manage the evolution of these standards and ensure the tool remains current and compliant.

* **Decision:** A formal steering document, titled **"Standard Version Adoption and Management Policy,"** will be created, version-controlled, and maintained in the project's Git repository (e.g., in GOVERNANCE.md). This document will establish the official process for adopting new versions of CDISC standards. The process will be overseen by a designated steering committee or the project's lead maintainers.  
* **Content of the Steering Document:**  
  1. **Scope:** The document will explicitly list the CDISC standards within the tool's scope (e.g., CDASH, ODM, Controlled Terminology, SDTM for mapping reference) and the current supported versions.  
  2. **Monitoring Process:** It will formalize the monitoring procedures. This includes the automated weekly check for new CT releases (as defined in Section 3.4) and a mandated biannual review of the CDISC roadmap for upcoming major releases of other standards like CDASH or SDTM.151  
  3. **Impact Assessment Protocol:** For any new major standard version, the document will mandate a formal impact assessment. This assessment must include:  
     * A technical analysis of changes, identifying new, modified, or retired elements and their impact on the tool's parsing, mapping, and validation logic.  
     * An estimation of the development effort required to implement support for the new version.  
     * An analysis of the impact on backward compatibility and the user base.  
  4. **Adoption and Support Policy:** The default policy will be to support the **latest final version plus the one previous major version** of any given standard. For example, upon the final release of CDASH v3.0, the tool would be updated to support both v3.0 and v2.1. Support for v2.1 would be deprecated and eventually removed in a future major release of the tool. This provides users with a clear transition window.  
  5. **Roadmap and Communication:** The steering committee will be responsible for publishing and maintaining a public roadmap item for the adoption of new major versions, communicating timelines to the user community.  
  6. **Tool Versioning Alignment:** The document will reiterate the Semantic Versioning policy (Section 10.3), explicitly linking changes in the tool's version to changes in standards support. A MINOR release will signify the addition of a new, backward-compatible standard (like a new CT package), while a MAJOR release will signify support for a backward-incompatible standard (like CDASH v3.0) or the removal of support for an older standard.148  
* **Rationale and Analysis:**  
  * The evolution of standards is a primary risk to the long-term relevance of this tool. A formal, documented governance process mitigates this risk by ensuring that changes are managed proactively rather than reactively.152  
  * This steering document provides the predictability and transparency that users in a regulated environment demand. It allows organizations to plan their own validation and upgrade cycles in alignment with the tool's support lifecycle. It demonstrates a mature approach to project management and a commitment to long-term maintenance.

### **11.2. Log and track regulated-system requirements**

For the system to be successfully deployed and validated in a GxP environment, all regulatory requirements must be explicitly tracked and linked to system features and tests.

* **Decision:** A formal **Requirements Traceability Matrix (RTM)** will be created and maintained as a core project artefact. This document will be the single source of truth for tracking compliance with all regulated-system requirements.  
  1. **RTM Structure:** The RTM will link every regulatory requirement (e.g., from 21 CFR Part 11\) to one or more system requirements, which are then traced to specific design specifications, code modules, and, crucially, test cases. The table defined in Section 1.4 serves as the initial template for this RTM.  
  2. **Audit Trail Specification:** The design of the audit trail, a cornerstone of compliance, will be meticulously specified in the RTM and design documents. This specification will cover:  
     * **Content:** The audit trail will capture the user ID, a secure timestamp, the action performed (create, modify, delete), a reference to the data record, the original value, and the new value, aligning with FDA guidance.24  
     * **Integrity:** The audit trail will be implemented as a secure, append-only log. At the application layer, there will be no functionality to alter or delete audit trail records, ensuring they are unalterable as required by 21 CFR 11.10(e).23  
     * **Reviewability:** The system's outputs will be designed to facilitate audit trail review. For example, every generated artefact will be traceable to a specific version of the input protocol and the CT package, allowing an auditor to correlate the output with the specific audit log entries for those source data ingestions.  
  3. **Disaster Recovery Plan (DRP):** For any hosted or enterprise version of the service, a formal DRP will be documented. This plan will outline the procedures for data backup (e.g., daily snapshots of the terminology database and user data), system restoration, and business continuity, including Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO).  
* **Rationale and Analysis:**  
  * A system is not "validated"; a system is "validation-ready." The actual validation is performed by the end-user organization within their specific context. The RTM is the primary document that enables this validation process. It provides auditors with a clear map demonstrating how each regulatory control has been implemented and tested.23  
  * The FDA's data integrity principles, known as ALCOA+ (Attributable, Legible, Contemporaneous, Original, Accurate, plus Complete, Consistent, Enduring, and Available), are directly addressed by this approach. The detailed audit trail design ensures attributability and originality. The system's validation and data integrity checks ensure accuracy. The DRP addresses the need for data to be enduring and available.24 By explicitly designing for these principles, we create a system that is fundamentally aligned with regulatory expectations.

### **11.3. Plan community contributions**

For the open-source component of the project to thrive, a clear and welcoming framework for community engagement and contribution is essential.

* **Decision:** A comprehensive framework for managing community contributions will be established from the project's inception.  
  1. **Contributor Guide (CONTRIBUTING.md):** A detailed contributor guide will be created and placed in the root of the repository. This document will provide clear, step-by-step instructions for potential contributors, including:  
     * How to set up the local development environment.  
     * The project's coding standards and style guide (which will be automatically enforced by ruff).  
     * The workflow for submitting changes (fork, branch, code, test, create pull request).  
     * Guidelines for reporting bugs and suggesting new features via GitHub Issues.  
  2. **Code of Conduct (CODE\_OF\_CONDUCT.md):** The project will officially adopt the **Contributor Covenant** (version 2.1 or newer) as its code of conduct.155 This is a widely respected, comprehensive document that sets clear expectations for behavior and fosters a safe, inclusive, and collaborative environment. The document will be customized to include a specific, private email address for reporting any violations.  
  3. **Contributor License Agreement (CLA):** To manage intellectual property and enable the dual-licensing model, a CLA will be required for all non-trivial code contributions. The CLA will grant the project maintainers the necessary rights to use, modify, and re-license the contributed code. This process will be automated using a tool like the **CLA Assistant** GitHub App, which can block pull requests from being merged until the contributor has signed the CLA.  
* **Rationale and Analysis:**  
  * A healthy open-source project is built on more than just code; it is built on a community. Clear documentation and guidelines are the single most important factor in lowering the barrier to entry for new contributors and ensuring that their efforts are productive.155  
  * A formal Code of Conduct is a non-negotiable component of a modern open-source project. It signals that the project is committed to creating a respectful and harassment-free environment for all participants.155  
  * The CLA is a critical legal instrument, particularly for a project with a commercial aspect. It clarifies the ownership and licensing of contributions, protecting both the contributor and the project. It ensures that the project has the legal standing to distribute the combined work under its chosen licenses (both open-source and proprietary), which is fundamental to the sustainability of the dual-license model.

## **Conclusion and Strategic Roadmap**

This technical and requirements specification outlines a comprehensive blueprint for an innovative system designed to automate the generation of CDISC-compliant CRFs from clinical study protocols. By leveraging a modern Python technology stack, a sophisticated NLP pipeline, and a rigorous, multi-layered validation framework, the proposed system will deliver significant value to the clinical research ecosystem. Key benefits include a dramatic reduction in the manual effort and time required for study start-up, a marked improvement in data quality and standardization from the point of collection, and enhanced regulatory compliance through a design that is auditable and traceable by default.

The architectural decisions prioritize modularity, maintainability, and security. The choice of FastAPI, Pydantic, and spaCy/medspaCy creates a cohesive and high-performance core, while the mandatory use of Docker ensures portable and consistent deployments. The dual-licensing model provides a strategic path to foster community innovation through an open-source core while ensuring the project's long-term financial sustainability through a commercial enterprise offering.

Crucially, the system is designed from the ground up to be "validation-ready" for use in GxP environments. The emphasis on automated testing, a robust CI/CD pipeline, immutable audit trails, and a formal governance structure for managing standards provides the objective evidence necessary to support a formal validation process.

**Implementation Roadmap:**

The development of this complex system should proceed iteratively, starting with a Minimum Viable Product (MVP) that delivers core value and expanding from there.

1. **Phase 1: Core Engine and Foundational Domains (MVP)**  
   * **Objective:** Build the core end-to-end pipeline for a limited set of common domains.  
   * **Tasks:**  
     * Implement the CI/CD pipeline foundation (lint, test, package).  
     * Set up the CDISC reference data management (ODM schemas, CT SQLite database).  
     * Build the DOCX importer.  
     * Develop the NLP pipeline for sentence segmentation and section detection.  
     * Implement rule-based NER and mapping logic for 2-3 core domains (e.g., **Demographics (DM)**, **Vital Signs (VS)**, **Concomitant Medications (CM)**).  
     * Implement the ODM and Markdown generation engines.  
     * Implement the structural and CT validation layers.  
     * Deliver the CLI as the primary interface.  
   * **Outcome:** A functional tool that can process simple DOCX protocols and generate validated CRFs for the most common study domains.  
2. **Phase 2: Expansion of Domain Coverage and API Development**  
   * **Objective:** Broaden the tool's utility and enable system integration.  
   * **Tasks:**  
     * Expand NER and mapping support to cover most other common CDASH domains (e.g., **Adverse Events (AE)**, **Medical History (MH)**, **Disposition (DS)**, **Exposure (EX)**).  
     * Develop and deploy the FastAPI REST API.  
     * Implement the automated CT update workflow (GitHub Action).  
     * Create the initial version of the user documentation, including the API reference and the mapping guide.  
   * **Outcome:** A powerful, API-driven service capable of handling the majority of data collection requirements in a typical clinical trial.  
3. **Phase 3: Advanced Features and User Experience**  
   * **Objective:** Enhance the system's robustness and lower the barrier to adoption.  
   * **Tasks:**  
     * Develop and deploy the optional SPA Web UI for file upload/download.  
     * Implement the PDF and structured XML importers.  
     * Begin training a statistical NER model using data bootstrapped from the rule-based system to improve extraction accuracy and generalization.  
     * Integrate with the CDISC CORE engine for advanced business rule validation.  
     * Establish the formal governance framework (steering committee, open-source contribution process).  
   * **Outcome:** A mature, user-friendly, and highly compliant system that serves a wide range of user personas and is positioned for long-term growth and community engagement.

By following this phased roadmap, the project can manage complexity, deliver value incrementally, and build a robust and sustainable solution that has the potential to become a cornerstone of modern, efficient clinical trial design.

### **Works cited**

1. Data Management for Clinical Research Data Services \- MCRA, accessed July 15, 2025, [https://www.mcra.com/our-service-offerings/cro-clinical-trial-research/data-management/biostatistics](https://www.mcra.com/our-service-offerings/cro-clinical-trial-research/data-management/biostatistics)  
2. Workflow Management Systems for Mid-Size CROs \- Applied Clinical Trials, accessed July 15, 2025, [https://www.appliedclinicaltrialsonline.com/view/workflow-management-systems-mid-size-cros](https://www.appliedclinicaltrialsonline.com/view/workflow-management-systems-mid-size-cros)  
3. Data Management Plan Template \- National Institute of Dental and Craniofacial Research, accessed July 15, 2025, [https://www.nidcr.nih.gov/sites/default/files/2018-03/clinical-data-management-plan-template\_0.docx](https://www.nidcr.nih.gov/sites/default/files/2018-03/clinical-data-management-plan-template_0.docx)  
4. Ensuring on-time quality data management deliverables from global clinical data management teams \- PMC, accessed July 15, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3043368/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3043368/)  
5. CDASHIG v2.1 | CDISC, accessed July 15, 2025, [https://www.cdisc.org/standards/foundational/cdashig-v2-1](https://www.cdisc.org/standards/foundational/cdashig-v2-1)  
6. CDASH 2.1 \- CDISC, accessed July 15, 2025, [https://www.cdisc.org/standards/foundational/cdash/cdash-2-1](https://www.cdisc.org/standards/foundational/cdash/cdash-2-1)  
7. The Magic that Happens between CDASH and SDTM \- CDISC, accessed July 15, 2025, [https://www.cdisc.org/kb/articles/magic-happens-between-cdash-and-sdtm](https://www.cdisc.org/kb/articles/magic-happens-between-cdash-and-sdtm)  
8. CDASHIG v2.0 | CDISC, accessed July 15, 2025, [https://www.cdisc.org/standards/foundational/cdash/cdashig-v2-0](https://www.cdisc.org/standards/foundational/cdash/cdashig-v2-0)  
9. Controlled Terminology \- CDISC, accessed July 15, 2025, [https://www.cdisc.org/standards/terminology/controlled-terminology](https://www.cdisc.org/standards/terminology/controlled-terminology)  
10. CDISC SDTM Controlled Terminology, accessed July 15, 2025, [https://cran.r-project.org/web/packages/sdtm.terminology/sdtm.terminology.pdf](https://cran.r-project.org/web/packages/sdtm.terminology/sdtm.terminology.pdf)  
11. sdtm.terminology package \- RDocumentation, accessed July 15, 2025, [https://www.rdocumentation.org/packages/sdtm.terminology/versions/2025-3-25](https://www.rdocumentation.org/packages/sdtm.terminology/versions/2025-3-25)  
12. Controlled Terminology Best Practices \- Pinnacle 21, accessed July 15, 2025, [https://www.pinnacle21.com/blog/controlled-terminology-best-practices](https://www.pinnacle21.com/blog/controlled-terminology-best-practices)  
13. ODM v2.0 | CDISC, accessed July 15, 2025, [https://www.cdisc.org/standards/data-exchange/odm-xml/odm-v2-0](https://www.cdisc.org/standards/data-exchange/odm-xml/odm-v2-0)  
14. ODM v2.0 \- CDISC, accessed July 15, 2025, [https://www.cdisc.org/odm-v2-0](https://www.cdisc.org/odm-v2-0)  
15. cdisc-org/DataExchange-ODM: ODM repository \- GitHub, accessed July 15, 2025, [https://github.com/cdisc-org/DataExchange-ODM](https://github.com/cdisc-org/DataExchange-ODM)  
16. ivbeg/docx2csv: Extracts tables from .docx files and saves ... \- GitHub, accessed July 15, 2025, [https://github.com/ivbeg/docx2csv](https://github.com/ivbeg/docx2csv)  
17. python \-docx to extract table from word docx \- Stack Overflow, accessed July 15, 2025, [https://stackoverflow.com/questions/46618718/python-docx-to-extract-table-from-word-docx](https://stackoverflow.com/questions/46618718/python-docx-to-extract-table-from-word-docx)  
18. The lxml.etree Tutorial, accessed July 15, 2025, [https://lxml.de/tutorial.html](https://lxml.de/tutorial.html)  
19. XPath and XSLT with lxml, accessed July 15, 2025, [https://lxml.de/1.3/xpathxslt.html](https://lxml.de/1.3/xpathxslt.html)  
20. Welcome to pdfminer.six's documentation\! — pdfminer.six 20250417.dev7+g51683b2 documentation, accessed July 15, 2025, [https://pdfminersix.readthedocs.io/](https://pdfminersix.readthedocs.io/)  
21. How to Extract PDF Tables in Python? \- GeeksforGeeks, accessed July 15, 2025, [https://www.geeksforgeeks.org/python/how-to-extract-pdf-tables-in-python/](https://www.geeksforgeeks.org/python/how-to-extract-pdf-tables-in-python/)  
22. PDF Table Extraction : r/dataengineering \- Reddit, accessed July 15, 2025, [https://www.reddit.com/r/dataengineering/comments/19832la/pdf\_table\_extraction/](https://www.reddit.com/r/dataengineering/comments/19832la/pdf_table_extraction/)  
23. FDA 21 CFR Part 11: Definition, Compliance Requirements, Benefits, and Software, accessed July 15, 2025, [https://simplerqms.com/21-cfr-part-11-requirements/](https://simplerqms.com/21-cfr-part-11-requirements/)  
24. What are the FDA audit trail requirements for clinical trials? \- Agatha, accessed July 15, 2025, [https://en.agathalife.com/what-are-the-fda-audit-trail-requirements-for-clinical-trials/](https://en.agathalife.com/what-are-the-fda-audit-trail-requirements-for-clinical-trials/)  
25. Guidance for Industry \- COMPUTERIZED SYSTEMS USED IN CLINICAL TRIALS | FDA, accessed July 15, 2025, [https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/fda-bioresearch-monitoring-information/guidance-industry-computerized-systems-used-clinical-trials](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/fda-bioresearch-monitoring-information/guidance-industry-computerized-systems-used-clinical-trials)  
26. CDISC Glossary Controlled Terminology \- NCI EVS, accessed July 15, 2025, [https://evs.nci.nih.gov/ftp1/CDISC/Glossary/CDISC%20Glossary.html](https://evs.nci.nih.gov/ftp1/CDISC/Glossary/CDISC%20Glossary.html)  
27. Audit Trail Reviews in Clinical Trials: What You Need to Know \- Medidata, accessed July 15, 2025, [https://www.medidata.com/en/life-science-resources/medidata-blog/audit-trail-review/](https://www.medidata.com/en/life-science-resources/medidata-blog/audit-trail-review/)  
28. 21 CFR Part 11: A Guide To FDA's Requirements \- Greenlight Guru, accessed July 15, 2025, [https://www.greenlight.guru/blog/21-cfr-part-11-guide](https://www.greenlight.guru/blog/21-cfr-part-11-guide)  
29. What is FDA 21 CFR Part 11? Compliance & Software Validation Guide \- Redzone, accessed July 15, 2025, [https://rzsoftware.com/what-is-fda-21-cfr-part-11-compliance-software-validation-guide/](https://rzsoftware.com/what-is-fda-21-cfr-part-11-compliance-software-validation-guide/)  
30. Open-Source vs Proprietary Software: The Clear Winner in 2025 \- O8 Agency, accessed July 15, 2025, [https://www.o8.agency/blog/open-source-software-vs-proprietary-software](https://www.o8.agency/blog/open-source-software-vs-proprietary-software)  
31. Open-Source Health Care Software | Journal of Ethics | American Medical Association, accessed July 15, 2025, [https://journalofethics.ama-assn.org/article/open-source-health-care-software/2011-09](https://journalofethics.ama-assn.org/article/open-source-health-care-software/2011-09)  
32. How Open-Source Benefits Clinical Trials \- Pharmaceutical Executive, accessed July 15, 2025, [https://www.pharmexec.com/view/how-open-source-benefits-clinical-trials](https://www.pharmexec.com/view/how-open-source-benefits-clinical-trials)  
33. Containerizing FastAPI Applications with Docker | Better Stack Community, accessed July 15, 2025, [https://betterstack.com/community/guides/scaling-python/fastapi-with-docker/](https://betterstack.com/community/guides/scaling-python/fastapi-with-docker/)  
34. FastAPI, accessed July 15, 2025, [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)  
35. Python Framework \- Flask Vs FastAPI Vs Django \- Lucent Innovation, accessed July 15, 2025, [https://www.lucentinnovation.com/blogs/technology-posts/flask-vs-fastapi-vs-django](https://www.lucentinnovation.com/blogs/technology-posts/flask-vs-fastapi-vs-django)  
36. Comparison of FastAPI with Django and Flask \- GeeksforGeeks, accessed July 15, 2025, [https://www.geeksforgeeks.org/python/comparison-of-fastapi-with-django-and-flask/](https://www.geeksforgeeks.org/python/comparison-of-fastapi-with-django-and-flask/)  
37. Data Validation with Pydantic \- Netguru, accessed July 15, 2025, [https://www.netguru.com/blog/data-validation-pydantic](https://www.netguru.com/blog/data-validation-pydantic)  
38. Python Data Validation with Pydantic | by Nineleaps \- Medium, accessed July 15, 2025, [https://medium.com/technology-nineleaps/python-data-validation-with-pydantic-9ca0342f9301](https://medium.com/technology-nineleaps/python-data-validation-with-pydantic-9ca0342f9301)  
39. Pydantic: Simplifying Data Validation in Python, accessed July 15, 2025, [https://realpython.com/python-pydantic/](https://realpython.com/python-pydantic/)  
40. Launching into clinical space with medspaCy: a new clinical text ..., accessed July 15, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8861690/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8861690/)  
41. medspacy/medspacy: Library for clinical NLP with spaCy. \- GitHub, accessed July 15, 2025, [https://github.com/medspacy/medspacy](https://github.com/medspacy/medspacy)  
42. lxml.etree versus ElementTree, accessed July 15, 2025, [https://lxml.de/1.3/compatibility.html](https://lxml.de/1.3/compatibility.html)  
43. Intro to Parsing HTML and XML with Python and lxml \- Scrapfly, accessed July 15, 2025, [https://scrapfly.io/blog/posts/intro-to-parsing-html-xml-python-lxml](https://scrapfly.io/blog/posts/intro-to-parsing-html-xml-python-lxml)  
44. Comparison of Flask, Django, and FastAPI: Advantages, Disadvantages, and Use Cases, accessed July 15, 2025, [https://medium.com/@tubelwj/comparison-of-flask-django-and-fastapi-advantages-disadvantages-and-use-cases-63e7c692382a](https://medium.com/@tubelwj/comparison-of-flask-django-and-fastapi-advantages-disadvantages-and-use-cases-63e7c692382a)  
45. FastAPI vs Django/Flask \- DEV Community, accessed July 15, 2025, [https://dev.to/hiteshchawla/fastapi-vs-django-core-difference-103a](https://dev.to/hiteshchawla/fastapi-vs-django-core-difference-103a)  
46. SpaCy vs. NLTK: A Comprehensive Comparison of Two Popular NLP Libraries in Python” | by Prabhu Srivastava | Medium, accessed July 15, 2025, [https://medium.com/@prabhuss73/spacy-vs-nltk-a-comprehensive-comparison-of-two-popular-nlp-libraries-in-python-b66dc477a689](https://medium.com/@prabhuss73/spacy-vs-nltk-a-comprehensive-comparison-of-two-popular-nlp-libraries-in-python-b66dc477a689)  
47. NLTK vs spaCy \- Python based NLP libraries and their functions \- Seaflux, accessed July 15, 2025, [https://www.seaflux.tech/blogs/NLP-libraries-spaCy-NLTK-differences](https://www.seaflux.tech/blogs/NLP-libraries-spaCy-NLTK-differences)  
48. Demo · medspacy medspacy · Discussion \#313 \- GitHub, accessed July 15, 2025, [https://github.com/medspacy/medspacy/discussions/313](https://github.com/medspacy/medspacy/discussions/313)  
49. XML Schema validation with lxml · Issue \#425 · mtconnect/cppagent \- GitHub, accessed July 15, 2025, [https://github.com/mtconnect/cppagent/issues/425](https://github.com/mtconnect/cppagent/issues/425)  
50. How do I use lxml to validate XML documents against a schema? \- WebScraping.AI, accessed July 15, 2025, [https://webscraping.ai/faq/lxml/how-do-i-use-lxml-to-validate-xml-documents-against-a-schema](https://webscraping.ai/faq/lxml/how-do-i-use-lxml-to-validate-xml-documents-against-a-schema)  
51. xml.etree.ElementTree vs. lxml.etree \- Björn Ricks, accessed July 15, 2025, [https://bjoernricks.github.io/posts/python/stdlib-etree-vs-lxml-etree/](https://bjoernricks.github.io/posts/python/stdlib-etree-vs-lxml-etree/)  
52. Template Designer Documentation — Jinja Documentation (3.1.x), accessed July 15, 2025, [https://jinja.palletsprojects.com/en/stable/templates/](https://jinja.palletsprojects.com/en/stable/templates/)  
53. Popular documentation tools \- Read the Docs, accessed July 15, 2025, [https://docs.readthedocs.com/platform/stable/intro/doctools.html](https://docs.readthedocs.com/platform/stable/intro/doctools.html)  
54. mkdocs-material/docs/alternatives.md at master · squidfunk/mkdocs ..., accessed July 15, 2025, [https://github.com/squidfunk/mkdocs-material/blob/master/docs/alternatives.md](https://github.com/squidfunk/mkdocs-material/blob/master/docs/alternatives.md)  
55. Template Inheritance \- Nunjucks, accessed July 15, 2025, [https://mozilla.github.io/nunjucks/templating.html](https://mozilla.github.io/nunjucks/templating.html)  
56. Nunjucks – A rich and powerful templating language for JavaScript by Mozilla | Hacker News, accessed July 15, 2025, [https://news.ycombinator.com/item?id=8444634](https://news.ycombinator.com/item?id=8444634)  
57. Docusaurus Vs Mkdocs | Which Documentation Generation Tool Is Better in 2025?, accessed July 15, 2025, [https://www.youtube.com/watch?v=es6GQFQ-3NM](https://www.youtube.com/watch?v=es6GQFQ-3NM)  
58. bandit ruleset \- Semgrep, accessed July 15, 2025, [https://semgrep.dev/p/bandit](https://semgrep.dev/p/bandit)  
59. Welcome to Bandit — Bandit documentation, accessed July 15, 2025, [https://bandit.readthedocs.io/](https://bandit.readthedocs.io/)  
60. Publishing package distribution releases using GitHub Actions CI/CD workflows, accessed July 15, 2025, [https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)  
61. Complete CI/CD with GitHub Actions and AWS for Python Developers: A Step-by-Step Guide, accessed July 15, 2025, [https://medium.com/@nomannayeem/complete-ci-cd-with-github-actions-and-aws-for-python-developers-a-step-by-step-guide-92807f6167ee](https://medium.com/@nomannayeem/complete-ci-cd-with-github-actions-and-aws-for-python-developers-a-step-by-step-guide-92807f6167ee)  
62. Automate your builds with GitHub Actions \- Python \- Docker Docs, accessed July 15, 2025, [https://docs.docker.com/guides/python/configure-github-actions/](https://docs.docker.com/guides/python/configure-github-actions/)  
63. Ultimate Guide to CI/CD Best Practices to Streamline DevOps ..., accessed July 15, 2025, [https://launchdarkly.com/blog/cicd-best-practices-devops/](https://launchdarkly.com/blog/cicd-best-practices-devops/)  
64. Code Generator — xsData 20.1 documentation \- Read the Docs, accessed July 15, 2025, [https://xsdata.readthedocs.io/en/v20.1/codegen.html](https://xsdata.readthedocs.io/en/v20.1/codegen.html)  
65. datamodel-code-generator \- Pydantic, accessed July 15, 2025, [https://docs.pydantic.dev/latest/integrations/datamodel\_code\_generator/](https://docs.pydantic.dev/latest/integrations/datamodel_code_generator/)  
66. Generate from JSON Data \- datamodel-code-generator, accessed July 15, 2025, [https://koxudaxi.github.io/datamodel-code-generator/jsondata/](https://koxudaxi.github.io/datamodel-code-generator/jsondata/)  
67. CDISC Terminology \- CBIIT \- National Cancer Institute, accessed July 15, 2025, [https://datascience.cancer.gov/resources/cancer-vocabulary/cdisc-terminology](https://datascience.cancer.gov/resources/cancer-vocabulary/cdisc-terminology)  
68. Python for CDISC SDTM Mapping \- Allwyn Dsouza, accessed July 15, 2025, [https://allwyndsouza.com/python-for-cdisc-sdtm-mapping](https://allwyndsouza.com/python-for-cdisc-sdtm-mapping)  
69. Library of CDASH CRF Examples \- CDISC, accessed July 15, 2025, [https://www.cdisc.org/standards/foundational/cdash/library-cdash-crf-examples](https://www.cdisc.org/standards/foundational/cdash/library-cdash-crf-examples)  
70. eCRF Portal \- CDISC, accessed July 15, 2025, [https://www.cdisc.org/kb/ecrf](https://www.cdisc.org/kb/ecrf)  
71. Examples Collection \- CDISC, accessed July 15, 2025, [https://www.cdisc.org/kb/examples](https://www.cdisc.org/kb/examples)  
72. Form Library (CDASH) \- OpenClinica Reference Guide, accessed July 15, 2025, [https://docs.openclinica.com/oc4/building-forms-and-studies/cdash-crf-library/](https://docs.openclinica.com/oc4/building-forms-and-studies/cdash-crf-library/)  
73. Controlled Terminology: FAQs \- CDISC, accessed July 15, 2025, [https://www.cdisc.org/kb/articles/controlled-terminology-faqs](https://www.cdisc.org/kb/articles/controlled-terminology-faqs)  
74. ftplib — FTP protocol client — Python 3.13.5 documentation, accessed July 15, 2025, [https://docs.python.org/3/library/ftplib.html](https://docs.python.org/3/library/ftplib.html)  
75. How to Automate File Transfer with Python ftplib | by Gabriel Marthendal | Level Up Coding, accessed July 15, 2025, [https://levelup.gitconnected.com/how-to-automate-file-transfer-with-python-ftplib-2dde0efe0325](https://levelup.gitconnected.com/how-to-automate-file-transfer-with-python-ftplib-2dde0efe0325)  
76. Creating pull requests in GitHub \- Graphite, accessed July 15, 2025, [https://graphite.dev/guides/create-pr-in-github-actions](https://graphite.dev/guides/create-pr-in-github-actions)  
77. Creating a pull request \- GitHub Docs, accessed July 15, 2025, [https://docs.github.com/articles/creating-a-pull-request](https://docs.github.com/articles/creating-a-pull-request)  
78. REST API endpoints for pull requests \- GitHub Docs, accessed July 15, 2025, [https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28\#create-a-pull-request](https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#create-a-pull-request)  
79. Real-time monitoring of an FTP server for new files : r/learnpython \- Reddit, accessed July 15, 2025, [https://www.reddit.com/r/learnpython/comments/2auyvc/realtime\_monitoring\_of\_an\_ftp\_server\_for\_new\_files/](https://www.reddit.com/r/learnpython/comments/2auyvc/realtime_monitoring_of_an_ftp_server_for_new_files/)  
80. How to Extract Tabular Data from Doc files Using Python? \- Analytics Vidhya, accessed July 15, 2025, [https://www.analyticsvidhya.com/blog/2021/09/how-to-extract-tabular-data-from-doc-files-using-python/](https://www.analyticsvidhya.com/blog/2021/09/how-to-extract-tabular-data-from-doc-files-using-python/)  
81. textacy \- PyPI, accessed July 15, 2025, [https://pypi.org/project/textacy/0.2.3/](https://pypi.org/project/textacy/0.2.3/)  
82. Walkthrough — textacy 0.12.0 documentation \- Read the Docs, accessed July 15, 2025, [https://textacy.readthedocs.io/en/0.12.0/walkthrough.html](https://textacy.readthedocs.io/en/0.12.0/walkthrough.html)  
83. Python by Examples: Extract PDF by PDFMiner.six | by MB20261 \- Medium, accessed July 15, 2025, [https://medium.com/@mb20261/python-by-examples-extract-pdf-by-pdfminer-six-246cba6f89b3](https://medium.com/@mb20261/python-by-examples-extract-pdf-by-pdfminer-six-246cba6f89b3)  
84. Extracting Tabular Data from PDFs \- Degenerate State, accessed July 15, 2025, [http://www.degeneratestate.org/posts/2016/Jun/15/extracting-tabular-data-from-pdfs/](http://www.degeneratestate.org/posts/2016/Jun/15/extracting-tabular-data-from-pdfs/)  
85. Python Libraries to Extract Tables From PDF: A Comparison \- Unstract, accessed July 15, 2025, [https://unstract.com/blog/extract-tables-from-pdf-python/](https://unstract.com/blog/extract-tables-from-pdf-python/)  
86. oxylabs/lxml-tutorial: A tutorial on parsing webpages with lxml \- GitHub, accessed July 15, 2025, [https://github.com/oxylabs/lxml-tutorial](https://github.com/oxylabs/lxml-tutorial)  
87. Evaluation of a Method to Identify and Categorize Section Headers in Clinical Documents | Request PDF \- ResearchGate, accessed July 15, 2025, [https://www.researchgate.net/publication/26777569\_Evaluation\_of\_a\_Method\_to\_Identify\_and\_Categorize\_Section\_Headers\_in\_Clinical\_Documents](https://www.researchgate.net/publication/26777569_Evaluation_of_a_Method_to_Identify_and_Categorize_Section_Headers_in_Clinical_Documents)  
88. Evaluation of a Method to Identify and Categorize Section Headers in Clinical Documents, accessed July 15, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3002123/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3002123/)  
89. Easy Medical NLP in Python using the medspaCy library | by Daniel Feller | Medium, accessed July 15, 2025, [https://medium.com/@danieljfeller/easy-medical-nlp-in-python-using-the-medspacy-library-4753f4806b6c](https://medium.com/@danieljfeller/easy-medical-nlp-in-python-using-the-medspacy-library-4753f4806b6c)  
90. EntityRecognizer · spaCy API Documentation, accessed July 15, 2025, [https://spacy.io/api/entityrecognizer](https://spacy.io/api/entityrecognizer)  
91. Custom Named Entity Recognition with Spacy \- Artificial Intelligence in Plain English, accessed July 15, 2025, [https://ai.plainenglish.io/custom-named-entity-recognition-with-spacy-part-1-b21ed944b7e5](https://ai.plainenglish.io/custom-named-entity-recognition-with-spacy-part-1-b21ed944b7e5)  
92. RFC 8785: JSON Canonicalization Scheme (JCS), accessed July 15, 2025, [https://www.rfc-editor.org/rfc/rfc8785](https://www.rfc-editor.org/rfc/rfc8785)  
93. CDASH Model v1.0 \- CDISC, accessed July 15, 2025, [https://www.cdisc.org/standards/foundational/cdash/cdash-model-v1-0](https://www.cdisc.org/standards/foundational/cdash/cdash-model-v1-0)  
94. What is Fuzzy Matching? | Aerospike, accessed July 15, 2025, [https://aerospike.com/blog/fuzzy-matching/](https://aerospike.com/blog/fuzzy-matching/)  
95. Fuzzy Data Matching Guide for Data-Driven Decision-Making \- WinPure, accessed July 15, 2025, [https://winpure.com/fuzzy-matching-guide/](https://winpure.com/fuzzy-matching-guide/)  
96. Fuzzy Matching 101: Cleaning and Linking Messy Data \- Data Ladder, accessed July 15, 2025, [https://www.dataladder.com/fuzzy-matching-101/](https://www.dataladder.com/fuzzy-matching-101/)  
97. SDTM and CDASH: Why You Need Both \- CDISC, accessed July 15, 2025, [https://www.cdisc.org/kb/articles/sdtm-and-cdash-why-you-need-both](https://www.cdisc.org/kb/articles/sdtm-and-cdash-why-you-need-both)  
98. Why is CDASH needed to map eCRF data to SDTM? \- CDISC, accessed July 15, 2025, [https://www.cdisc.org/sites/default/files/2023-07/2023\_Why%20is%20CDASH%20needed%20to%20map%20eCRF%20data%20to%20SDTM\_Anna%20Tsutsui\_ver%201.1.pdf](https://www.cdisc.org/sites/default/files/2023-07/2023_Why%20is%20CDASH%20needed%20to%20map%20eCRF%20data%20to%20SDTM_Anna%20Tsutsui_ver%201.1.pdf)  
99. What is Fuzzy Matching? How It Works & Why It's Important \- Senzing, accessed July 15, 2025, [https://senzing.com/what-is-fuzzy-matching/](https://senzing.com/what-is-fuzzy-matching/)  
100. Fuzzy Matching 101: Cleaning and Linking Messy Data, accessed July 15, 2025, [https://dataladder.com/fuzzy-matching-101/](https://dataladder.com/fuzzy-matching-101/)  
101. SDTM \- CDISC, accessed July 15, 2025, [https://www.cdisc.org/standards/foundational/sdtm](https://www.cdisc.org/standards/foundational/sdtm)  
102. 8\. Mapping of clinical trial data to CDISC-SDTM: a practical example based on APPROACH and ABIRISK \- FAIR Cookbook, accessed July 15, 2025, [https://faircookbook.elixir-europe.org/content/recipes/applied-examples/approach-cdisc.html](https://faircookbook.elixir-europe.org/content/recipes/applied-examples/approach-cdisc.html)  
103. AI CDASH Mapping: Beyond the Buzz – What Experts Need to Know \- Clinion, accessed July 15, 2025, [https://www.clinion.com/insight/ai-cdash-mapping-what-it-means-for-your-next-trial/](https://www.clinion.com/insight/ai-cdash-mapping-what-it-means-for-your-next-trial/)  
104. Clinical Data Acquisition Standards Harmonization importance and benefits in clinical data management \- PMC \- PubMed Central, accessed July 15, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC4640009/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4640009/)  
105. 17.1 CDISC ODM XML \- OpenClinica Documentation, accessed July 15, 2025, [https://docs.openclinica.com/?export\_pdf=17502](https://docs.openclinica.com/?export_pdf=17502)  
106. How to Use CDISC's ODM Standard for CRF Design | Certara, accessed July 15, 2025, [https://www.certara.com/blog/how-to-use-cdisc-odm-standard-for-crf-design/](https://www.certara.com/blog/how-to-use-cdisc-odm-standard-for-crf-design/)  
107. YAML Frontmatter \- Zettlr Docs, accessed July 15, 2025, [https://docs.zettlr.com/en/core/yaml-frontmatter/](https://docs.zettlr.com/en/core/yaml-frontmatter/)  
108. Using YAML frontmatter \- GitHub Docs, accessed July 15, 2025, [https://docs.github.com/en/contributing/writing-for-github-docs/using-yaml-frontmatter](https://docs.github.com/en/contributing/writing-for-github-docs/using-yaml-frontmatter)  
109. YAML Best Practices | RudderStack Docs, accessed July 15, 2025, [https://www.rudderstack.com/docs/profiles/dev-docs/yaml-refresher/](https://www.rudderstack.com/docs/profiles/dev-docs/yaml-refresher/)  
110. Variable usage in jinja2 inside markdown template \- Stack Overflow, accessed July 15, 2025, [https://stackoverflow.com/questions/65777167/variable-usage-in-jinja2-inside-markdown-template](https://stackoverflow.com/questions/65777167/variable-usage-in-jinja2-inside-markdown-template)  
111. Create a Git Diff in Markdown \- We Learn Code, accessed July 15, 2025, [https://welearncode.com/create-diff-markdown/](https://welearncode.com/create-diff-markdown/)  
112. Validation with lxml, accessed July 15, 2025, [https://lxml.de/validation.html\#xml-schema](https://lxml.de/validation.html#xml-schema)  
113. swhume/odmlib: Python package for working with CDISC ODM \- GitHub, accessed July 15, 2025, [https://github.com/swhume/odmlib](https://github.com/swhume/odmlib)  
114. Validate ODM | odmlib, accessed July 15, 2025, [https://swhume.github.io/odmlib/validate.html](https://swhume.github.io/odmlib/validate.html)  
115. CORE | CDISC, accessed July 15, 2025, [https://www.cdisc.org/core](https://www.cdisc.org/core)  
116. Open source offering of the cdisc rules engine \- GitHub, accessed July 15, 2025, [https://github.com/cdisc-org/cdisc-rules-engine](https://github.com/cdisc-org/cdisc-rules-engine)  
117. Clinical Data Validation | Pinnacle 21 by Certara, accessed July 15, 2025, [https://www.certara.com/pinnacle-21-enterprise-software/validation/](https://www.certara.com/pinnacle-21-enterprise-software/validation/)  
118. A Comprehensive Guide to CDISC SDTM: Everything You Need to Know \- Lindus Health, accessed July 15, 2025, [https://www.lindushealth.com/blog/cdisc-sdtm](https://www.lindushealth.com/blog/cdisc-sdtm)  
119. A Comprehensive Guide to CDISC: Everything You Need to Know \- Lindus Health, accessed July 15, 2025, [https://www.lindushealth.com/blog/a-comprehensive-guide-to-cdisc-everything-you-need-to-know](https://www.lindushealth.com/blog/a-comprehensive-guide-to-cdisc-everything-you-need-to-know)  
120. HTML5 JSON Report Format \- ServiceStack Documentation, accessed July 15, 2025, [https://docs.servicestack.net/html5reportformat](https://docs.servicestack.net/html5reportformat)  
121. pytest-mock Tutorial: A Beginner's Guide to Mocking in Python \- DataCamp, accessed July 15, 2025, [https://www.datacamp.com/tutorial/pytest-mock](https://www.datacamp.com/tutorial/pytest-mock)  
122. Testing Machine Learning Systems: Code, Data and Models \- Made With ML by Anyscale, accessed July 15, 2025, [https://madewithml.com/courses/mlops/testing/](https://madewithml.com/courses/mlops/testing/)  
123. How to use unittest-based tests with pytest, accessed July 15, 2025, [https://docs.pytest.org/en/stable/how-to/unittest.html](https://docs.pytest.org/en/stable/how-to/unittest.html)  
124. <www.lambdatest.com>, accessed July 15, 2025, [https://www.lambdatest.com/learning-hub/nlp-testing\#:\~:text=Regression%20Testing%3A%20NLP%20can%20be,to%20quickly%20identify%20new%20issues.](https://www.lambdatest.com/learning-hub/nlp-testing#:~:text=Regression%20Testing%3A%20NLP%20can%20be,to%20quickly%20identify%20new%20issues.)  
125. What Is Natural Language Processing (NLP) Testing \- LambdaTest, accessed July 15, 2025, [https://www.lambdatest.com/learning-hub/nlp-testing](https://www.lambdatest.com/learning-hub/nlp-testing)  
126. test — Regression tests package for Python — Python 3.13.5 documentation, accessed July 15, 2025, [https://docs.python.org/3/library/test.html](https://docs.python.org/3/library/test.html)  
127. Automated Regression Testing in 2025: Best Practises from Top QA Teams, accessed July 15, 2025, [https://python-bloggers.com/2025/03/automated-regression-testing-in-2025-best-practises-from-top-qa-teams/](https://python-bloggers.com/2025/03/automated-regression-testing-in-2025-best-practises-from-top-qa-teams/)  
128. Coverage.py — Coverage.py 7.9.2 documentation, accessed July 15, 2025, [https://coverage.readthedocs.io/](https://coverage.readthedocs.io/)  
129. pytest \- Codecov, accessed July 15, 2025, [https://about.codecov.io/tool/pytest/](https://about.codecov.io/tool/pytest/)  
130. Welcome to Click — Click Documentation (8.2.x), accessed July 15, 2025, [https://click.palletsprojects.com/](https://click.palletsprojects.com/)  
131. Creating composable CLIs with click in Python | Better Stack Community, accessed July 15, 2025, [https://betterstack.com/community/guides/scaling-python/click-explained/](https://betterstack.com/community/guides/scaling-python/click-explained/)  
132. Create a Mature Test CLI Tool with Python Click | Dojo Five, accessed July 15, 2025, [https://dojofive.com/blog/3-steps-to-make-a-professional-cli-tool-using-pythons-click/](https://dojofive.com/blog/3-steps-to-make-a-professional-cli-tool-using-pythons-click/)  
133. Building Python script CLIs with argparse and Click \- Trickster Dev, accessed July 15, 2025, [https://www.trickster.dev/post/building-python-script-clis-with-argparse-and-click/](https://www.trickster.dev/post/building-python-script-clis-with-argparse-and-click/)  
134. Build Command-Line Interfaces With Python's argparse \- Real Python, accessed July 15, 2025, [https://realpython.com/command-line-interfaces-python-argparse/](https://realpython.com/command-line-interfaces-python-argparse/)  
135. Scalable Python backend: Building a containerized FastAPI Application with uv, Docker, and pre-commit: a step-by-step guide \- DEV Community, accessed July 15, 2025, [https://dev.to/ismaarce/scalable-python-backend-building-a-containerized-fastapi-application-with-uv-docker-and-172j](https://dev.to/ismaarce/scalable-python-backend-building-a-containerized-fastapi-application-with-uv-docker-and-172j)  
136. Developing a Single Page App with FastAPI and React | TestDriven.io, accessed July 15, 2025, [https://testdriven.io/blog/fastapi-react/](https://testdriven.io/blog/fastapi-react/)  
137. Request Files \- FastAPI, accessed July 15, 2025, [https://fastapi.tiangolo.com/tutorial/request-files/](https://fastapi.tiangolo.com/tutorial/request-files/)  
138. Building a File Upload in FastAPI \- StackPuz Blog, accessed July 15, 2025, [https://blog.stackpuz.com/building-a-file-upload-in-fastapi/](https://blog.stackpuz.com/building-a-file-upload-in-fastapi/)  
139. Building a React CRUD App with a FastAPI \- StackPuz Blog, accessed July 15, 2025, [https://blog.stackpuz.com/building-a-react-crud-app-with-a-fastapi/](https://blog.stackpuz.com/building-a-react-crud-app-with-a-fastapi/)  
140. Filestack: The Best File Uploader & Upload API, accessed July 15, 2025, [https://www.filestack.com/](https://www.filestack.com/)  
141. How to Upload File in Python-Flask \- GeeksforGeeks, accessed July 15, 2025, [https://www.geeksforgeeks.org/python/how-to-upload-file-in-python-flask/](https://www.geeksforgeeks.org/python/how-to-upload-file-in-python-flask/)  
142. OpenAPI docs \- FastAPI, accessed July 15, 2025, [https://fastapi.tiangolo.com/reference/openapi/docs/](https://fastapi.tiangolo.com/reference/openapi/docs/)  
143. Extending OpenAPI \- FastAPI, accessed July 15, 2025, [https://fastapi.tiangolo.com/how-to/extending-openapi/](https://fastapi.tiangolo.com/how-to/extending-openapi/)  
144. The Essential Guide to Effective Technical Documentation \- Paligo, accessed July 15, 2025, [https://paligo.net/blog/how-to/the-essential-guide-to-effective-technical-documentation/](https://paligo.net/blog/how-to/the-essential-guide-to-effective-technical-documentation/)  
145. What Is Technical Writing? Mastering the Art of Simplifying Complexity | by Sandleen Shah, accessed July 15, 2025, [https://medium.com/@SandleenShah/what-is-technical-writing-mastering-the-art-of-simplifying-complexity-e1b215a72893](https://medium.com/@SandleenShah/what-is-technical-writing-mastering-the-art-of-simplifying-complexity-e1b215a72893)  
146. Writing Effective and Engaging Technical Documentation ... \- Guidde, accessed July 15, 2025, [https://www.guidde.com/blog/writing-effective-and-engaging-technical-documentation-actionable-steps](https://www.guidde.com/blog/writing-effective-and-engaging-technical-documentation-actionable-steps)  
147. CDISC SDTM A Basic Guide To SDTM Mapping | PDF \- Scribd, accessed July 15, 2025, [https://www.scribd.com/document/768213180/CDISC-SDTM-A-Basic-Guide-To-SDTM-Mapping](https://www.scribd.com/document/768213180/CDISC-SDTM-A-Basic-Guide-To-SDTM-Mapping)  
148. Semantic Versioning 2.0.0 | Semantic Versioning, accessed July 15, 2025, [https://semver.org/](https://semver.org/)  
149. Using Semantic Versioning to Simplify Release Management | AWS DevOps & Developer Productivity Blog, accessed July 15, 2025, [https://aws.amazon.com/blogs/devops/using-semantic-versioning-to-simplify-release-management/](https://aws.amazon.com/blogs/devops/using-semantic-versioning-to-simplify-release-management/)  
150. Understanding Semantic Versioning: A Standard for Software Releases | by Dean Biscocho, accessed July 15, 2025, [https://medium.com/@deanbiscocho/understanding-semantic-versioning-a-standard-for-software-releases-c1583c8a3c28](https://medium.com/@deanbiscocho/understanding-semantic-versioning-a-standard-for-software-releases-c1583c8a3c28)  
151. CDISC | Clear Data. Clear Impact., accessed July 15, 2025, [https://www.cdisc.org/](https://www.cdisc.org/)  
152. Trial Master File Reference Model \- CDISC, accessed July 15, 2025, [https://www.cdisc.org/tmf](https://www.cdisc.org/tmf)  
153. Navigating Audit Trail Review Regulations in Clinical Research \- Quanticate, accessed July 15, 2025, [https://www.quanticate.com/blog/audit-trail-review](https://www.quanticate.com/blog/audit-trail-review)  
154. Guidance on FDA 21 CFR Part 11 Compliance | Northwell Health, accessed July 15, 2025, [https://www.northwell.edu/sites/northwell.edu/files/2021-06/Guidance-on-FDA-21-CFR-Part-11-Compliance.pdf](https://www.northwell.edu/sites/northwell.edu/files/2021-06/Guidance-on-FDA-21-CFR-Part-11-Compliance.pdf)  
155. Contributor Covenant: A Code of Conduct for Open Source and ..., accessed July 15, 2025, [https://www.contributor-covenant.org/](https://www.contributor-covenant.org/)
