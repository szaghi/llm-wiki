> **SUPERSEDED (2026-07-08).** This Deep-Research export was the origin document
> for this repository and is retained for provenance only. The operative law is
> `CLAUDE.md` (+ per-bundle `CLAUDE.md`); rationale is in `DECISIONS.md`.
> Known defects (see DECISIONS.md D13): Docs-export artifacts (relative-link
> examples mangled to `docs.google.com`, equations lost to dead `![][imageN]`
> placeholders), content-farm sourcing, §6.1 "stateful merge" implemented as an
> unconditional overwrite, §6.2 linter false-fails on `---` inside bodies.
> Its OKF claims were verified against the real spec and absorbed. **Never
> ingest this file into any bundle.**

# **Local LLM Wiki & Google Open Knowledge Format (OKF) Implementation Guide**

## **1\. Theoretical Foundation: Stateful Compilation vs. Stateless Retrieval**

The standard approach to giving Large Language Models (LLMs) access to custom documents is Retrieval-Augmented Generation (RAG)1. While highly scalable for millions of unstable corporate records, standard RAG possesses an inherent cognitive limitation: it is mathematically forgetful4. Because the retrieval mechanism is stateless, the model is forced to rediscover conceptual associations, temporal sequences, and logical relationships from scratch on every individual query4. Chunks of information remain isolated from one another in vector space, leaving the model blind to cross-document contradictions or systemic evolutions unless those specific fragments happen to be co-retrieved within the same transient context window1.  
In April 2026, Andrej Karpathy proposed an alternative paradigm: the LLM Wiki2. Rather than employing the LLM as a static responder that dynamically retrieves raw, disconnected chunks, this pattern leverages the model as an active, stateful compiler4. Under this framework, raw source materials are treated as immutable "source code," while a structured, interlinked Markdown directory functions as the "compiled codebase"6.  
The Google Open Knowledge Format (OKF v0.1), open-sourced in June 2026, formalizes this exact LLM Wiki pattern into a portable, vendor-neutral standard9. OKF defines a "Knowledge Bundle"—a self-contained, version-controlled repository of Markdown files where every document represents a discrete "Concept" bound by explicit, machine-readable metadata and native bidirectional hyperlinks9.  
By shifting the computational burden from real-time vector similarity lookups to upfront semantic compilation, knowledge is synthesized and integrated at the point of ingestion3. The comparative mechanics of these two paradigms are delineated below.

| Architectural Dimension | Traditional Stateless RAG | Compiled LLM Wiki (Karpathy & OKF Pattern) |
| :---- | :---- | :---- |
| **Systemic State** | Stateless; derived dynamically from raw chunks at query time2 | Stateful; compiled, synthesized, and updated incrementally4 |
| **Standard Specifications** | Ad-hoc document splitting and embedding setups12 | Google Open Knowledge Format (OKF v0.1)9 |
| **Data Progression** | Raw Sources ![][image1] Chunks ![][image1] Vector Store ![][image1] Context Injection12 | Raw Sources ![][image1] LLM Synthesis ![][image1] Standardized OKF Bundle ![][image1] IDE6 |
| **Linkage Mechanism** | Dense vector similarity calculations (cosine distance)12 | Explicit relative \[links\](/path.md) and \[\[wikilinks\]\] \[cite: 11, 15, 16\] |
| **Temporal Tracking** | Fragile; conflicting historical claims are co-retrieved blindly5 | Robust; updates overwrite stale claims or explicitly flag timeline shifts5 |
| **Scale Envelope** | High scale; designed for millions of dynamic corporate documents1 | Bounded scale; optimized for highly curated corpuses (\~100–500 documents)1 |
| **Infrastructure Required** | Vector databases, orchestrators (LangChain), hosting12 | Local file system, lightweight CLI engine, markdown viewer7 |
| **Maintenance Profile** | Low upfront ingestion overhead; high processing cost per query2 | High ingestion compilation overhead; near-zero query-time cost4 |

## **2\. Directory Topography & File Layout**

An OKF-compliant directory structure is distributed as a **Knowledge Bundle**9. The configuration below maps Karpathy’s three-layer structure4 directly to the normative guidelines of the Google OKF specification11:

Plaintext  
my-okf-wiki/  
├── CLAUDE.md                   \# System Schema (Core instructions for Claude Code) \[cite: 19, 20\]  
├── AGENTS.md                   \# Portable Agent Guidelines (Cursor, Codex, local runners) \[cite: 23, 24\]  
├── config.yaml                 \# Core ingestion and metadata pipeline configurations \[cite: 24\]  
├── raw/                        \# LAYER 1: Immutable Source Files  
│   ├── inbox/                  \# Drop-zone for uncompiled PDF, HTML, or DOCX documents \[cite: 25, 26, 27\]  
│   └── assets/                 \# Local image, diagram, and media attachment directory \[cite: 6, 28\]  
├── wiki/                       \# LAYER 2: OKF Bundle Root \[cite: 11, 16\]  
│   ├── index.md                \# Reserved: Root progressive-disclosure catalog  
│   ├── log.md                  \# Reserved: Append-only chronological system change log  
│   ├── metrics/                \# OKF Concept Folder (Domain-specific directory)  
│   │   ├── index.md            \# Subdirectory index (Contains no frontmatter)  
│   │   └── user\_retention.md   \# OKF Concept Document (YAML \+ Markdown)  
│   ├── tables/                 \# OKF Concept Folder \[cite: 11, 16\]  
│   │   └── customer\_db.md      \# OKF Concept Document representing a database schema \[cite: 9, 16\]  
│   ├── playbooks/              \# OKF Concept Folder \[cite: 11, 16\]  
│   │   └── data\_pipeline.md    \# OKF Concept Document representing a runtime guide  
│   └── references/             \# OKF Concept Folder (One summary page per raw source) \[cite: 11, 23\]  
└── .wiki/                      \# LAYER 3: SQLite ingestion history and local QMD indexes \[cite: 27\]

### **Layer Rules & Isolation Boundaries**

1. **raw/ (Layer 1 \- Immutable)**: The compiling LLM agent has read-only access to this folder4. Under no circumstances are files in this folder modified, renamed, or deleted23. This guarantees that the entire wiki can be cleanly re-compiled from scratch should prompt guidelines or model backends change6.  
2. **wiki/ (Layer 2 \- LLM-Owned)**: The LLM agent has full write privileges here4. The human researcher primarily browses and queries this layer4.  
3. **.wiki/ (Layer 3 \- Internal State)**: This directory is git-ignored and used by local indexers, storing local SQLite databases, chunk registries, and vector caches27.

## **3\. The System Constitution (CLAUDE.md)**

To force your agent (such as Claude Code, Cursor, or local CLI scripts) to act as a disciplined OKF compiler rather than a generic chatbot4, you must define a strict system constitution4. Place the following instruction set inside CLAUDE.md at the project root31:

# **OKF Wiki Compiler Constitution (v0.1 Spec)**

You are the automated, stateful compiler of this local Knowledge Bundle. You must strictly enforce the Google Open Knowledge Format (OKF v0.1) specification.

## **1\. Structural Boundaries**

* raw/ is IMMUTABLE. Never write, modify, or delete files here.  
* wiki/ is the OKF Bundle Root. You have full ownership of compile and write operations in this directory.

## **2\. Concept Document Standards**

Every .md file in wiki/ (except the reserved files index.md and log.md) is an OKF **Concept**.

* Every Concept file must begin with a parseable YAML frontmatter block.  
* The YAML block must contain a non-empty type field defining the classification (e.g., Metric, Table, API Endpoint, Playbook, Reference).  
* Use kebab-case filenames for all concept paths.

### **Standard YAML Header**

## **type: Metric \# REQUIRED title: "User Retention" \# Recommended display name description: "Measures week-over-week user retention rates." \# Summary resource: "https://ops.internal/metrics/retention" \# Unique reference URI tags: \[product, growth, metrics\] \# Optional tags timestamp: 2026-07-08T08:00:00Z \# ISO 8601 change stamp**

### **Conventional Body Headers**

Structure the Markdown body with these sections where applicable:

* \# Schema for structures, tables, or columns.  
* \# Examples for fenced code blocks or use-cases.  
* \# Citations for references.

## **3\. Reserved Files Protocol**

Do not use index.md or log.md for regular Concept Documents. They are strictly reserved.

### **index.md (Directory Catalog)**

Every directory (including root wiki/) should feature an index.md file to support progressive disclosure.

* Must have NO YAML frontmatter (with the sole exception of the root wiki/index.md which may declare okf\_version: "0.1").

* # **Uses sections grouping relative concept links under markdown headings with the description pulled from the linked file:**   **Section / Group Heading**

  * [Display Name](http://docs.google.com/relative/path.md) \- Single sentence description.

### **log.md (Change History)**

* Must have NO frontmatter.

* ## **Stores flat list of date-grouped changes, newest first, using strict YYYY-MM-DD ISO 8601 headings:**   **Directory Update Log**   **2026-07-08**

  * **Creation**: Ingested [customer\_db](http://docs.google.com/wiki/tables/customer-db.md) reference.  
  * **Update**: Refined calculations in [user\_retention](http://docs.google.com/wiki/metrics/user_retention.md).

## **4\. Graph Navigation and Cross-Linking**

* Concepts must link to other concepts using standard Markdown links.  
* Prefer **absolute bundle-relative paths** starting with / to avoid breaking if paths move: \[Customer Table\](/tables/customer\_db.md).  
* Use relative links when linking to neighboring files: \[Next Steps\](./other\_playbook.md).

## **5\. Citations Formatting**

When extracting knowledge from raw files, cite sources inside a numbered \# Citations section at the bottom of the concept document:

# **Citations**

1. [raw/inbox/2026\_q2\_report.pdf](http://docs.google.com/raw/inbox/2026_q2_report.pdf)

## **4\. Core Operational Pipelines**

The life cycle of the system is driven by three continuous processes: Ingest, Query, and Lint4.

                     \+---------------------------+  
                     |  Raw File Dropped in Inbox|  
                     \+-------------+-------------+  
                                   |  
                                   v  
                     \+-------------+-------------+  
                     |      INGEST PIPELINE       |  
                     |  \- Chunking & Ingestion   |  
                     |  \- 3-Pass Ingest Pipeline |  
                     \+-------------+-------------+  
                                   |  
                                   v  
                     \+-------------+-------------+  
                     |      QUERY PIPELINE        |  
                     |  \- QMD Hybrid Search      |  
                     |  \- LLM Reranking & RRF    |  
                     \+-------------+-------------+  
                                   |  
                                   v  
                     \+-------------+-------------+  
                     |       LINT PIPELINE       |  
                     |  \- Compliance Check       |  
                     |  \- Contradiction Resolves |  
                     \+---------------------------+

### **4.1. The Ingest Pipeline**

When a user drops a document (e.g., PDF, HTML, DOCX) into raw/inbox/, the ingestion script automates parsing and coordinates the compiling LLM through a three-pass compilation loop27:

1. **Extraction Pass (Thinking On)**: The LLM reads the raw source text and outputs structured JSON mapping its core thesis, key takeaways, and a list of mentioned entities and concepts27. To optimize token consumption during large batch updates, the system utilizes delta-tracking and hashing29. Only modified or newly introduced chunks are processed, saving up to 95% of active API call costs29:  
   ![][image2]  
   ![][image3]  
   Where ![][image4] represents the raw source document, ![][image5] is the number of LLM analysis passes, and ![][image6] represents newly introduced segments29.  
2. **Page Drafting and Merging Pass (Thinking Off)**: The agent processes each extracted entity or concept27. If a page does not exist, it drafts a new markdown file using defined templates25. If the page already exists, the agent performs a stateful merge: it reads the current page, evaluates the new findings, and updates the document without destroying past context, appending the new reference to the YAML frontmatter27.  
3. **Source Summary Pass**: The agent writes a custom summary file to wiki/sources/\<slug\>.md detailing its origin, publication data, key claims, and an audit list of every wiki page created or updated during the run27.

### **4.2. The Query Pipeline**

Queries are routed through a local hybrid search engine (e.g., Tobias Lütke's QMD)22.

1. **Intent Classification**: Simple conversational messages skip retrieval and get a quick reply, saving up to 30 seconds of system latency27.  
2. **Hybrid Retrieval**: Technical queries are expanded into alternative phrasings using query expansion12. The engine searches the wiki using a hybrid combination of BM25 and vector semantic search21.  
3. **Reciprocal Rank Fusion (RRF)**: Candidate results are combined using a position-aware RRF scoring formula:  
   ![][image7]  
   Where ![][image8] is the set of retrieval backends, ![][image9] is the zero-indexed rank of document ![][image10] within backend ![][image11], ![][image12] is a constant smoothing parameter (typically 60), and ![][image13] represents a dynamic, position-aware weight21. QMD modulates this weight based on rank (![][image14] for top 3 results to favor exact matches, scaling down to ![][image15] for ranks 11+ to trust semantic vectors more)21.  
4. **Synthesis**: The top-ranked pages are loaded into the LLM's active context window1. The model generates a cited synthesis using \[\[wikilinks\]\] to point directly to source and concept nodes27.

### **4.3. The Lint Pipeline**

The Lint Pipeline acts as an automated system auditor, checking the repository structure at regular intervals1:

* **Orphan Detection**: Identifies wiki pages with no incoming links from other pages18.  
* **Link Verification**: Checks for broken \[\[wikilinks\]\] and resolves them using fuzzy matching23.  
* **Contradiction Check (Deep Lint)**: Evaluates conceptually related wiki nodes to flag logical or factual contradictions18. For example, if a node in concepts/ contains a theoretical claim contradicted by a newly ingested source, the linter identifies the collision and flags it in the markdown files under a \#\# Contradictions block5.

## **5\. Local Setup & Tooling Configuration**

This section details how to configure a 100% local, private, and offline LLM Wiki environment using Ollama, Claude Code, and QMD6.

### **Step 1: Install System Dependencies**

Ensure Node.js (version 22 or higher) and Python (3.11 or higher) are installed locally on your machine21.

Bash  
\# Install Claude Code globally \[cite: 25\]  
npm install \-g @anthropic-ai/claude-code

\# Install Tobias Lütke's QMD search engine globally \[cite: 21, 27\]  
npm install \-g @tobilu/qmd

\# Ensure Ollama is installed and run the local reasoning model \[cite: 27\]  
ollama pull qwen3:14b

### **Step 2: Initialize Project Directories & Git Version Control**

Create your workspace and initialize it as a Git repository to enable version control and rollback capability for your compiled files6.

Bash  
\# Create directory structures \[cite: 27, 40\]  
mkdir \-p local-wiki/raw/inbox local-wiki/raw/assets  
mkdir \-p local-wiki/wiki/sources local-wiki/wiki/concepts local-wiki/wiki/entities local-wiki/wiki/syntheses  
mkdir \-p local-wiki/outputs

cd local-wiki  
git init

\# Configure .gitignore to keep state files out of your Git history  
cat \<\< 'EOF' \> .gitignore  
.DS\_Store  
.wiki/  
node\_modules/  
.venv/  
.env  
raw/assets/  
EOF

### **Step 3: Configure QMD Collections & Context Trees**

QMD allows you to register descriptive metadata contexts at arbitrary folder levels21. When QMD retrieves a document chunk, it attaches this hierarchical context, allowing downstream LLM agents to make precise decisions regarding the logical origin of information21.

Bash  
\# Initialize the local search index  
qmd init

\# Add your OKF wiki directory as a searchable collection  
qmd collection add wiki/ \--name local-okf \--pattern "\*\*/\*.md"

\# Add hierarchical contexts  
qmd context add qmd://local-okf/concepts "Theoretical frameworks and abstract conceptual definitions."  
qmd context add qmd://local-okf/entities "Specific tools, technologies, organizations, and historical figures."  
qmd context add qmd://local-okf/sources "Authoritative source documents, papers, and web captures."

\# Pull the GGUF models locally (EmbeddingGemma-300M and Qwen3-Reranker-0.6B) \[cite: 21, 35, 36\]  
qmd embed

## **6\. Code Recipes**

### **6.1. The Ingestion Engine (ingest\_okf.py)**

This script uses markitdown for high-fidelity document text extraction and coordinates with your local Ollama instance running Qwen3 to extract metadata and compile OKF-compliant Concept Documents27.

Python  
import os  
import json  
import yaml  
import re  
from datetime import datetime  
from markitdown import MarkItDown  
from openai import OpenAI

\# Initialize local LLM client pointing to Ollama  
client \= OpenAI(  
    base\_url="http://localhost:11434/v1",  
    api\_key="ollama"  
)  
MARK\_PARSER \= MarkItDown()

def parse\_raw\_document(file\_path):  
    """Converts a local file to clean Markdown text."""  
    try:  
        result \= MARK\_PARSER.convert(file\_path)  
        return result.text\_content  
    except Exception as e:  
        print(f"Error parsing {file\_path}: {e}")  
        return ""

def generate\_okf\_pages(raw\_text, source\_filename):  
    """Sends raw text to the local LLM and returns structured OKF JSON."""  
    system\_prompt \= """  
    You are an expert AI compiler that extracts structured units of knowledge from raw inputs.  
    Identify all distinct 'Concepts' (definitions, schemas, runbooks, metrics) within the source text.  
      
    For each concept, you must output:  
    1\. The target file path relative to the wiki root (e.g., 'concepts/attention-mechanism.md' or 'tables/orders.md').  
    2\. A brief 'type' classification (e.g., 'Concept', 'Table', 'Metric', 'Playbook').  
    3\. A clear, title-cased display title.  
    4\. A concise, one-sentence description.  
    5\. A clean Markdown body, incorporating schemas or visual guides. All source citations must be listed under a standard '\# Citations' section.  
      
    Output strictly valid JSON matching this schema:  
    {  
      "concepts": \[  
        {  
          "file\_path": "subdirectory/filename.md",  
          "type": "Metric",  
          "title": "User Retention",  
          "description": "Measures user retention.",  
          "body": "\# User Retention\\n\\nBody content...\\n\\n\# Citations\\n1. raw/inbox/source-file.pdf"  
        }  
      \]  
    }  
    """  
      
    try:  
        response \= client.chat.completions.create(  
            model="qwen3:14b",  
            messages=\[  
                {"role": "system", "content": system\_prompt},  
                {"role": "user", "content": f"Source File: {source\_filename}\\n\\nContent:\\n{raw\_text}"}  
            \],  
            response\_format={"type": "json\_object"}  
        )  
        return response.choices\[0\].message.content  
    except Exception as e:  
        print(f"LLM extraction failure: {e}")  
        return "{}"

def save\_and\_merge\_concept(concept, source\_path):  
    """Saves the concept page to the correct subdirectory using OKF specifications."""  
    target\_path \= os.path.join("wiki", concept\["file\_path"\])  
    os.makedirs(os.path.dirname(target\_path), exist\_ok=True)  
      
    frontmatter \= {  
        "type": concept\["type"\],  
        "title": concept\["title"\],  
        "description": concept\["description"\],  
        "resource": f"local://{source\_path}",  
        "timestamp": datetime.utcnow().isoformat() \+ "Z"  
    }  
      
    \# Write the compiled file to disk  
    with open(target\_path, "w", encoding="utf-8") as f:  
        f.write("---\\n")  
        yaml.safe\_dump(frontmatter, f, default\_flow\_style=False)  
        f.write("---\\n\\n")  
        f.write(concept\["body"\])  
    print(f"\[OK\] Ingested Concept Node: {target\_path}")

def run\_ingestion\_pipeline():  
    inbox\_dir \= "raw/inbox"  
    if not os.path.exists(inbox\_dir):  
        print(f"Inbox directory '{inbox\_dir}' not found.")  
        return

    for filename in os.listdir(inbox\_dir):  
        full\_path \= os.path.join(inbox\_dir, filename)  
        if os.path.isfile(full\_path) and not filename.startswith('.'):  
            print(f"Processing source: {filename}...")  
            text\_content \= parse\_raw\_document(full\_path)  
            if not text\_content:  
                continue  
              
            raw\_response \= generate\_okf\_pages(text\_content, filename)  
            try:  
                extracted\_data \= json.loads(raw\_response)  
                for concept in extracted\_data.get("concepts", \[\]):  
                    save\_and\_merge\_concept(concept, os.path.join("raw/inbox", filename))  
            except json.JSONDecodeError:  
                print(f"Failed to parse JSON response for {filename}")

if \_\_name\_\_ \== "\_\_main\_\_":  
    run\_ingestion\_pipeline()

### **6.2. The OKF Compliance Linter (lint\_okf.py)**

This script audits your wiki files against the normative conformance guidelines specified in §9 of the Google OKF v0.1 specification, flagging missing metadata, broken paths, or malformed layouts11.

Python  
import os  
import yaml

def validate\_okf\_bundle(wiki\_dir):  
    failures \= 0  
    reserved\_files \= \["index.md", "log.md"\]  
      
    print(f"Auditing OKF Bundle at: {wiki\_dir}\\n" \+ "="\*50)  
      
    for root, dirs, files in os.walk(wiki\_dir):  
        for file in files:  
            file\_path \= os.path.join(root, file)  
            rel\_path \= os.path.relpath(file\_path, wiki\_dir)  
              
            if not file.endswith(".md"):  
                continue  
                  
            \# Rule 1: Reserved files must adhere to listing and logging standards  
            if file in reserved\_files:  
                if file \== "index.md":  
                    with open(file\_path, 'r', encoding='utf-8') as f:  
                        content \= f.read()  
                    \# index.md files must contain NO YAML frontmatter, except root version declaration  
                    if content.startswith("---") and rel\_path \!= "index.md":  
                        print(f"\[FAIL\] {rel\_path}: Subdirectory index.md files MUST NOT contain YAML frontmatter.")  
                        failures \+= 1  
                continue  
              
            \# Rule 2: Every concept page must contain valid YAML frontmatter delimiters  
            with open(file\_path, 'r', encoding='utf-8') as f:  
                content \= f.read()  
                  
            if not content.startswith("---"):  
                print(f"\[FAIL\] {rel\_path}: Missing standard YAML frontmatter block start.")  
                failures \+= 1  
                continue  
                  
            try:  
                parts \= content.split("---")  
                if len(parts) \< 3:  
                    print(f"\[FAIL\] {rel\_path}: YAML frontmatter is unclosed.")  
                    failures \+= 1  
                    continue  
                      
                header\_yaml \= parts\[1\]  
                metadata \= yaml.safe\_load(header\_yaml)  
                  
                \# Rule 3: The frontmatter block MUST contain a non-empty 'type' key  
                if not metadata or "type" not in metadata or not str(metadata\["type"\]).strip():  
                    print(f"\[FAIL\] {rel\_path}: Frontmatter is missing a valid 'type' key.")  
                    failures \+= 1  
                      
            except Exception as e:  
                print(f"\[FAIL\] {rel\_path}: Syntax error in YAML frontmatter block. Error: {e}")  
                failures \+= 1  
                  
    if failures \== 0:  
        print("\\n\[SUCCESS\] Your Knowledge Bundle is strictly compliant with the OKF v0.1 specification.")  
    else:  
        print(f"\\n\[WARNING\] Audit finished. Found {failures} conformance issues that must be corrected.")

if \_\_name\_\_ \== "\_\_main\_\_":  
    validate\_okf\_bundle("wiki")

## **7\. Visualizing the Knowledge Graph**

Standardizing your interlinked wiki pages on relative paths or bidirectional links enables dynamic exploration and graph layout analysis6:

1. **Open the Vault**: Install and open Obsidian, choosing "Open folder as vault" and pointing it to your local local-wiki/ folder6.  
2. **Filter the Graph**: Click the gear icon in the Obsidian Graph View to configure filters6. In the "Filters" input block, write \-file:index.md \-file:log.md44. This hides directory listings and chronologies, preventing them from acting as central hubs so you can visualize direct relationships between concept and entity nodes44.  
3. **Deploy Dataview**: Install the community plugin Dataview6. Create a new Markdown dashboard and paste the following snippet to generate a dynamic table tracking recently updated files sorted by OKF metadata1:  
   Snippet di codice  
   TABLE type as Type, description as Summary, timestamp as Updated  
   FROM "wiki"  
   WHERE file.name \!= "index" AND file.name \!= "log"  
   SORT timestamp DESC  
   LIMIT 10

4. **Local Asset Pathing**: In Obsidian *Settings ![][image1] Files and links*, set the "Attachment folder path" to raw/assets/1. This ensures any images clipped during research are stored locally and are accessible to the LLM1.

#### **Bibliografia**

1. LLM Knowledge Base for Coding Agents: Beyond RAG \- Verdent Guides, [https://www.verdent.ai/guides/llm-knowledge-base-coding-agents](https://www.verdent.ai/guides/llm-knowledge-base-coding-agents)  
2. LLM Wiki: Karpathy's 3-Layer Pattern That Replaces RAG (2026 Guide) \- decodethefuture, [https://decodethefuture.org/en/llm-wiki-karpathy-pattern/](https://decodethefuture.org/en/llm-wiki-karpathy-pattern/)  
3. RAG, LLM Wiki, Agentic Search: Differences, Costs and Use Cases (2026), [https://pasqualepillitteri.it/en/news/1496/rag-llm-wiki-agentic-search-differences-costs-2026](https://pasqualepillitteri.it/en/news/1496/rag-llm-wiki-agentic-search-differences-costs-2026)  
4. Karpathy's LLM Wiki: How We Built a 2188-Document Knowledge Base from AI Research, [https://echofold.ai/news/karpathy-llm-wiki-how-to-build-personal-knowledge-base](https://echofold.ai/news/karpathy-llm-wiki-how-to-build-personal-knowledge-base)  
5. Andrej Karpathy's LLM Wiki: Why the Future of AI Memory Isn't RAG | Gamgee Blog, [https://gamgee.ai/blogs/karpathy-llm-wiki-memory-pattern/](https://gamgee.ai/blogs/karpathy-llm-wiki-memory-pattern/)  
6. LLM Wiki \- Gist \- GitHub, [https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)  
7. Karpathy's LLM Wiki: A Knowledge Base That Compounds \- AI Builder Club, [https://www.aibuilderclub.com/blog/karpathy-llm-wiki](https://www.aibuilderclub.com/blog/karpathy-llm-wiki)  
8. LLM Wiki 1 — Building a Minimal LLM Wiki | by Ken Moriwaki | May, 2026 | Medium, [https://medium.com/@ken.moriwaki/building-a-minimal-llm-wiki-19a2fb0e9ac7](https://medium.com/@ken.moriwaki/building-a-minimal-llm-wiki-19a2fb0e9ac7)  
9. Open Knowledge Format | Definition, Scope and Compliance (Grounding Page), [https://groundingpage.com/facts/open-knowledge-format/](https://groundingpage.com/facts/open-knowledge-format/)  
10. How the Open Knowledge Format can improve data sharing | Google Cloud Blog, [https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)  
11. knowledge-catalog/okf/SPEC.md at main \- GitHub, [https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)  
12. What It Takes to Build a RAG System from Scratch in Python \- Dataquest, [https://www.dataquest.io/blog/build-a-rag-system-from-scratch/](https://www.dataquest.io/blog/build-a-rag-system-from-scratch/)  
13. GitHub \- pguso/rag-from-scratch: Demystify RAG by building it from scratch. Local LLMs, no black boxes \- real understanding of embeddings, vector search, retrieval, and context-augmented generation., [https://github.com/pguso/rag-from-scratch](https://github.com/pguso/rag-from-scratch)  
14. Build a RAG System in 50 Lines of Python | by Shane | LLM Implementation | Medium, [https://medium.com/@LLMImplementation/build-a-rag-system-in-50-lines-of-python-d181db025480](https://medium.com/@LLMImplementation/build-a-rag-system-in-50-lines-of-python-d181db025480)  
15. GitHub \- nvk/llm-wiki: LLM-compiled knowledge bases for any AI agent. Parallel multi-agent research, thesis-driven investigation, source ingestion, wiki compilation, querying, and artifact generation., [https://github.com/nvk/llm-wiki](https://github.com/nvk/llm-wiki)  
16. Google's New Knowledge Standard: What is the Open Knowledge Format (OKF)? | by Dreamwalker(박제창) | Jun, 2026 | Medium, [https://medium.com/@aristojeff/googles-new-knowledge-standard-what-is-the-open-knowledge-format-okf-f044ddf5b6bd](https://medium.com/@aristojeff/googles-new-knowledge-standard-what-is-the-open-knowledge-format-okf-f044ddf5b6bd)  
17. I Built a Knowledge Base That Thinks — Inspired by Karpathy's LLM Wiki | OceanBase, [https://en.oceanbase.com/blog/knowledge-base-thinks-inspired-by-karpathy-llm-wiki](https://en.oceanbase.com/blog/knowledge-base-thinks-inspired-by-karpathy-llm-wiki)  
18. I used Karpathy's LLM Wiki to build a knowledge base that maintains itself with AI \- Medium, [https://medium.com/@k.balu124/i-used-karpathys-llm-wiki-to-build-a-knowledge-base-that-maintains-itself-with-ai-df968e4f5ea0](https://medium.com/@k.balu124/i-used-karpathys-llm-wiki-to-build-a-knowledge-base-that-maintains-itself-with-ai-df968e4f5ea0)  
19. How to Build Karpathy's LLM Wiki: The Complete Guide to AI-Maintained Knowledge Bases, [https://blog.starmorph.com/blog/karpathy-llm-wiki-knowledge-base-guide](https://blog.starmorph.com/blog/karpathy-llm-wiki-knowledge-base-guide)  
20. Andrej Karpathy's LLM Wiki: Create your own knowledge base | by Urvil Joshi | Medium, [https://medium.com/@urvvil08/andrej-karpathys-llm-wiki-create-your-own-knowledge-base-8779014accd5](https://medium.com/@urvvil08/andrej-karpathys-llm-wiki-create-your-own-knowledge-base-8779014accd5)  
21. ehc-io/qmd: Query Markdown \- MCP server for hybrid search over markdown knowledge bases \- GitHub, [https://github.com/ehc-io/qmd](https://github.com/ehc-io/qmd)  
22. Tobi Lütke's QMD: Why Shopify's CEO Built His Own AI Memory System | Gamgee Blog, [https://gamgee.ai/blogs/tobi-lutke-qmd-local-semantic-search/](https://gamgee.ai/blogs/tobi-lutke-qmd-local-semantic-search/)  
23. llm-wiki/AGENTS.md at master \- GitHub, [https://github.com/Pratiyush/llm-wiki/blob/master/AGENTS.md](https://github.com/Pratiyush/llm-wiki/blob/master/AGENTS.md)  
24. What Is Andrej Karpathy's LLM Wiki? How to Build a Personal Knowledge Base With Claude Code | MindStudio, [https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code](https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code)  
25. How to Build Andrej Karpathy's LLM Knowledge Base from Scratch for Dummies | by Theo James | Medium, [https://medium.com/@theo-james/how-to-build-andrej-karpathys-llm-knowledge-base-from-scratch-for-dummies-a025f6c4d100](https://medium.com/@theo-james/how-to-build-andrej-karpathys-llm-knowledge-base-from-scratch-for-dummies-a025f6c4d100)  
26. GitHub \- NiharShrotri/llm-wiki: Local LLM-maintained personal wiki, built on Karpathy's LLM-Wiki pattern. Runs on Ollama \+ Qwen3 \+ QMD., [https://github.com/NiharShrotri/llm-wiki](https://github.com/NiharShrotri/llm-wiki)  
27. AGENTS.md \- Programming-With-Maury/Karpathy-LLM-Wiki \- GitHub, [https://github.com/Programming-With-Maury/Karpathy-LLM-Wiki/blob/main/AGENTS.md](https://github.com/Programming-With-Maury/Karpathy-LLM-Wiki/blob/main/AGENTS.md)  
28. Building a Production-Grade Local RAG Pipeline — 100% Free, No Cloud Required, [https://levelup.gitconnected.com/building-a-production-grade-local-rag-pipeline-100-free-no-cloud-required-8d172e929623](https://levelup.gitconnected.com/building-a-production-grade-local-rag-pipeline-100-free-no-cloud-required-8d172e929623)  
29. I built Karpathy's LLM Wiki twice — once as code, once as a .md. Here's what each one gives up. | by Leandro Bernardo \- Towards AI, [https://pub.towardsai.net/i-built-karpathys-llm-wiki-twice-once-as-code-once-as-a-md-heres-what-each-one-gives-up-08b31170999a](https://pub.towardsai.net/i-built-karpathys-llm-wiki-twice-once-as-code-once-as-a-md-heres-what-each-one-gives-up-08b31170999a)  
30. Andrej Karpathy's LLM Wiki Pattern: Cut Claude Token Usage 95% with a Two-Folder System | MindStudio, [https://www.mindstudio.ai/blog/karpathy-llm-wiki-pattern-cut-claude-token-usage-95-percent](https://www.mindstudio.ai/blog/karpathy-llm-wiki-pattern-cut-claude-token-usage-95-percent)  
31. LLM Wiki: Karpathy's Idea for AI Knowledge Bases \- Denser.ai, [https://denser.ai/blog/llm-wiki-karpathy-knowledge-base/](https://denser.ai/blog/llm-wiki-karpathy-knowledge-base/)  
32. Tobias Lütke tobi \- GitHub, [https://github.com/tobi](https://github.com/tobi)  
33. GitHub \- tobi/qmd: mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local, [https://github.com/tobi/qmd](https://github.com/tobi/qmd)  
34. What is QMD and how does it work? | by Hithesh Jayawardana \- Medium, [https://medium.com/@hithesh0215/what-is-qmd-and-how-does-it-work-9c0d1de490e8](https://medium.com/@hithesh0215/what-is-qmd-and-how-does-it-work-9c0d1de490e8)  
35. Installation \- QMD (Query Markup Documents), [https://tobi-qmd-3.mintlify.app/installation](https://tobi-qmd-3.mintlify.app/installation)  
36. qmd \+ nano-graphrag: You Do Not Need Pinecone for This \- DEV Community, [https://dev.to/stevengonsalvez/qmd-nano-graphrag-you-do-not-need-pinecone-for-this-45ne](https://dev.to/stevengonsalvez/qmd-nano-graphrag-you-do-not-need-pinecone-for-this-45ne)  
37. Karpathy's LLM Wiki? No Code with Claude or Github Copilot\! \- DEV Community, [https://dev.to/rosidotidev/karpathys-llm-wiki-no-code-with-claude-or-github-copilot-5fb0](https://dev.to/rosidotidev/karpathys-llm-wiki-no-code-with-claude-or-github-copilot-5fb0)  
38. QMD Memory Backend: Collection Name Inconsistency Between Gateway and QMD CLI · Issue \#54942 \- GitHub, [https://github.com/openclaw/openclaw/issues/54942](https://github.com/openclaw/openclaw/issues/54942)  
39. ZalaAvinash/rag-from-scratch-python: A small, readable, fully local Retrieval-Augmented Generation pipeline in Python. pypdf \+ Ollama \+ ChromaDB. No API keys, no cloud. \- GitHub, [https://github.com/ZalaAvinash/rag-from-scratch-python](https://github.com/ZalaAvinash/rag-from-scratch-python)  
40. GitHub \- SamurAIGPT/llm-wiki-agent: A personal knowledge base that builds and maintains itself. Drop in sources, [https://github.com/SamurAIGPT/llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent)  
41. Build An OKF Brain Like Mine\! \- Search Engine Journal, [https://www.searchenginejournal.com/build-an-okf-brain-like-mine/580661/](https://www.searchenginejournal.com/build-an-okf-brain-like-mine/580661/)  
42. Feature: MCP server config support in openclaw.json · Issue \#43509 \- GitHub, [https://github.com/openclaw/openclaw/issues/43509](https://github.com/openclaw/openclaw/issues/43509)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAYCAYAAAAVibZIAAAAdklEQVR4XmNgGAWjYMABBxCnATEPugQlgBGIW4HYGF2CUgAysBeIWdAlKAEg1xYAcRyUjRUIALEkiVgOiOcD8WQg5mOgEjAB4tVALIMuQS4QBuLFQCyPLkEJyALiCHRBSgAonU4FYml0CUoAKLZ5ofQoGAX0AAA5bAi7Yfn2hgAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlQAAAB7CAYAAACy/R7jAAANo0lEQVR4Xu3df4wsWVUH8GNc/IU/WNmoqMRddQUVAQMoqEQkgmtQVNAIuAaCQVFQgwQRUPMETVYNCvgDIxJcDAIGRbMqCkSfSoAo8VdYJYDxaYwEjZoY/lCMP+43t69TU6+6p2emd1+/mc8nOZk3VT3V3dU1754591RVFQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFwJd2/x2hbvbnFbi49bLb9Xize2eFeLV7a422o5AAALrmvxmhbvb3HTZPmDWjxx8j0AAGs8oMVjW7x6Fdeslj96tQ4AgCM8rsX9qlenUqW6T4sPafGc6tUrAAA2SOL0jBbXVu+fenuLC6vvszzrAQDYIBWoZ02+v7nF7S0e1eLxk+UAAKyRHqn0Sg2fWD2hev1qHQAARxj9U1MXqidV+qcAADbI9ade1OLfWvxqi+sn69KU/sLSPwUAAAAAAAAAAAAAAAAAAABcMbm+1L+3+N9VfLDF328Z/zr5uaXI5RZyeQUAgDNt3OB4JEH/2OIzDz1iOx9dPXl6bov31sH2LkweAwBwZuWGx2+ugyQo/86yk0qS9vDqidVfV79VDQDAmZeqVKpTI6n63jr9VdA/vsXvtXj6fMXEh7a4tk7/XFO73uaut3deJUm/y3whAGdHBszPaPG1LR5Zh6szN7T48Mn3Z9ljW/x39YQqXx9xePWJfFqLW2u54pXB9UdaPGa+4hS23WZuq5PP+mEtPmK17B61/DqTSD2zxTNW/+ZkvqDFq2p5HwNwFfvIFs9q8YEWf9bix6r3AL29xXe0+Ibq97AbA+5Zd02Ll9ZBlerd1ROi01pXmUiS8hN1OEl5cl3e/L4u/rLF5/Uf+39L25y6a4tXtHhHi2+p/nn/RfVerz+o9Td7zut/ZfWk80rKa56fDPBPk2Xvr35M59jeRze3+LlaPh4AuAp9dvX+niRSnzNbl//sX9vif6oPuOdJkp8/rIPBOsnHHTH4fW6LP6leARySBPx2ix+vg76rJEDp6ZqeMZjX84QW72nxqatlsbTNqTTOv7HFC+rwexrTnXmv6xKxyPO/rcU95yvuZGOfvK/Fp0+W57V/TYv/rJ4YJ0HeN/mMb6ujK4gAXAUe2OKfa3Pz9ZdXv4RAvp43mZpJAjOSqlR9dikD/0+vYprAJGFJUjOtriRhSOJwsXpCNGR6LtNHH7P6ft02px7X4va6vEk+j8+2vm22fC4Jyqvryp+5mCTyH6ofv0muprJf/q7Fv1T/o2Ef5XN4a63/3QPgKvAJLd7Z4m9aXH941SEPqD6lNK2AnCdPrYOEKslVkqxd+ZTq04nzZPUpLR49W/aV1V9D+qKmkmi9sA6Sp3XbHJIMva7FH9VBEjb1U9U/86N8U/UqWJrUj5Km/MQ66d375FqfAK6T95jq6XyfxEhA59WrfZLXlTNAv2S+AoCrQwauTPdkgH72bN1cBtdfrvPTPzWXKbGfr4Ok6o+rN3LvQhKCJLTTZDUJTxKq+XMkacjzzxOtz6rD/UxL25xKdeti9Wb7b6zLk5j71nZ9R/erXgF60HzFghtbvL6W+9Cyf3+wer/T/LUcJcdu9kmSzblUf7IulbR9nPKLMWV53qbTAc6M9NZkqmSbv94z4J33KYkkAqn6jKQqCdYu+qmSEFysw1N4S9b1Ci3ZZpsX6uC9ZDo3Fauvr+0SqWFMqW3bA3T/Fr9bh5Oq0yRTSfB/q5b3yfi8UoFdSuL2ya3Vp1mP+/4B2AOpcmQwzYB0NVaefqAuP9NtU/xObZ5y2sZDqzc5Z7+lurOLs9wymCaZOaqCkoRhqX9qyTbbTIKcQXwkVSPSCH/U9odR6Tqqwjk1TapOk0xFpjYvVe8BfEX1JDeRkyhyhl8a+j92PHiPbZMAA7CnxlTJUu/JlZDXkSTlq+cr9kgG/VzkcyQfJ701zVSSn8RRRgK8zee17TYjSc2DqyciqVSlH2nae5X1mX5cmj4cCdU2r2kqSVUucvqyOnkyFaN/KttJtWxEGu13UT28s+R3cdteNAD2zEiojqouZID64RYftvo+TcxPO1i9UQbKPHbbv7yTBOxzQhV5L7ncwEiqtt0X62yb/CRpyfPN+6eWbNpmpvRSHVry9OrPMf0Mkkj9QvXjYG4kVFl/HEl2XlK9z2s+VXcc4xjedspxX+V9ZF/Mz7gE4CqQM7S2SajyuOkp9Pdp8ZOT7zfJAJELF94RCVW2Oa1KHBU5ozFnku3CvatfQHIXt6TZlPwMI3FZ6hVasmmbOZvs++cLV7Lv/6u2P+PsJFN+SaYyFZfKVK6VlSnndQneJqN/ap8vibAtU34AV7F7Ve8zSW/Rukbk66tPBY2G9C+s3uT7t6vl48yq9Kk8r3qi9eLqVY0M/JnWGf0tuap1ZBupTuRxF+rwtYOOk1DlquBpot428lrXvc/jSEIwenV2Ma2UytPSNZSmjtM/FZu2mcE7+38uiWHO+rxYB8+RxOo3avkMusgUVaaqvme+Yo1pMjUS0SRDJ0mqcozlpIqLtX6fJOnKc72pxXe2+JnqV/v/4tX6HA85bm+pfoyO5XltufVSlmdfJfIc82XZv4kLLX5xteyTqr/PJ1f/HF5evd9vk02fFwB7LoNGKiypSDxp9f1UTp1fOs09Cc+0+pGBJo9Lw3akpyhTYhnwcrmFX189ZkjFakwRZYop108ajpNQXQljn2WA3tVZj6n+5QKb181XTBynfyrWbTNN6q+r5euOfVH1s+LGNbZS0bu5euN9mryXqnv5jLOtac/VOkkyfrSW7wF4kqTqpur9U0vJ4VQuPZHbJz2++vPmUg9/1eLzV//Oe87XVFOT1OQPjVQ0X1V9ejv7LAljjuv5srtVT9KynyJfcw2vB7b42erPl6RzU8KZx2S7R70PAPZYBsnvavEf1W87k2Qh9+3LwPKiWj5Dap5QpYqRAWr02IxpoEwVLiVUkWTkkdUH2Om29jmhysCXBDAXw0wisSvZR++py6etkqAmWflAHT4LL/epS4Kw6TWs22bOikuymwH+UvWqyhOr7/ckYF86Hlj9jMhUW1K5yWe5JJ99fi7bPcqXVT/W5snUkITl+XXQq7fON1efbp3uk1Tvsv0lOfZyDI4LlY6kciSn+R3IfkoylP2ax+X4fGv134lUl3JsLy1L5fC91at+qYLma86SzFTmpeq/B99dy79HQxKuXNdsm944APZcpkYeVn1QyNd5AjQ1EqoMTDdWnw66VJcnVKmSTBOqPDZVimdWn3a5oS5PzvY5oUqlJjcOPk4VZRsZqDOQr0taTmLdNpMkjeRn+pmnopLPZi6f0VtWX5dcqP2+aGbME6rIcZYqaT7LJMhJprJvxuOSZKWyleWpvv559eN7vixJ3KXVz0xlf9yz+u9Atp9p03XTzQ+pfh/NdfsYgDNqJEEZqJ5afeB4Wx3crDdTJ/k+g8w0ocpjU4XIQDQGoAz42Va+pn9kXxOqTINNp8N2LYN0KhvrBt2T2MU2kxCkQpVBf1q9iiQX6ZEbU737KsfebXVwNfe87iSbj6leURoJfSpFmcpN79NXtfi+6tW0RKbvvmJhWaZJs49zRfbI8kdVvwxFKmmRKcJM6Y0/OKby+PStJfJvAM6RTI+kapFKU/5Cj4e3+LXq00e/VD1BygCRPpwMuhmIMuikCvLSOmhSz0Dyp9WnX55Svdn9HbW+CfpKSBUjlalUqE4r+yT7YX56fAb932zxiNny09jFNvMZvabFc+ryxCwJW/rhlipb+yT7IdOcv1I9yclx+rzqrzuVuRx/SfYz3Z3K6e9XT57yM9/e4lur9/mN3sDpsmw7y5OIZRr1udX3d/5gSBKX/Zfleb6lKl5+NtPru656AnCVyGA0PyMpyUL+yp83L+f7/JU+lYFo07TivhjJ1JNqNxWEnOGYBu95chJ5rkwN7XJw3cU289nNP9MkAm+o0233zjKd8ksTeaY6p8b03vQ95rPO93nsOE6Xlk1lmnUkl3lcHp/HzZ9vyGPzh0UqZQBwZmWATOUhlYtdJFOZcsotcOZ9TVOp/v1QHd2YfRy73mYSrFQUNzXF75Mk+Un+Mj23T1KRvWm+EADOklQPdnWtqVQ/cu2lD1a/btINh1dzB0p1KElLGu8zZbvUxwQA3AEyXZOeoZzKfu+6/IrrmyJVm1wOIlWoXJ/onXX49P5M8eyi2gUAsLeS7GSKb5oE7SpyEUpTPADAmZezEjM9N6b7dhm3VG+KBgAAAAAAAAAAAAAAAAC2dd/q99877vWj8vhcHT3XpQIAONfGzXCP4wnVb0x8e4tnz9YBAHAMt5aECgA4x+5a/abCL6t+o+STkFABAOfa17W4f4s3tHhIi2taPL/FxQ3x4hYfVQckVADAuXZjiwe3eFOLa2frtiWhAgDOvQurGHIvvntsiLvX4bMBJVQAwLl2XYu3VK9SPa36VF4SpnkSJaECAFgjydGbW7ygxUNn646S3quXt3hfi3e1uKV6dQsA4Ny5S/Wz/QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADOpf8Deax6+XadCUIAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,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>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAZCAYAAADTyxWqAAABVElEQVR4Xu3UvyuFURzH8a9Q5FcRUQzKooxKSjGJxUJRbJIymEhklZRBFouSjcEguyQTk8GiFOUfMBj9eH+cc+89jsfTozsY+NSre5/vee55zq/nmv35VGMAg6jztQY05m7IknKs4g7zmMMVNnGOzsKt6SnDDg5QFdQ1okucmRtxpvTiAV1xA1nBdlxMyxoe0Ro3kEWMxMW07OMNyyiN2jpQH9VSM2GuM3nBKaZRG96UNdrJdXMd5TqVa0ueeqZoijoCG3gy1+Fs0K6Hztg3D9CPtSYlcQMZwiuWgpo62UVLUMtHu3SCiriBTOEWbf66D8cYzt8RRUfiGT1RXaPVeo366yZznev60L7u+MeJPsICbvx37eAW7jFuhenraDRjD5O+9imV5kagaGG7MWbuJU+adjsu/GfR0a5qZHr1+qO2H0dLoD8CvSWaVdGpsYTF/88v5x3pADJ/iBWrJgAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADUAAAAaCAYAAAAXHBSTAAACN0lEQVR4Xu2WS6iNURTHl1DKm8FNVylFKcqzm1CIMiEhKQO3jExJitJN3booeVzJoyQJUTJAYSAmysTEjFwTQpiYSOH3b+2d7+y7zzH51Pfx/evX2WetdfbZr7X2NmvUqNHf1Cp4Bz8LfIYPof0VjsOE+IM66QJ8h+WJfaH5BO/DuMRXaY2HJ/AKuhKfJvIIfsCaVle1NQc+wU0YlfgmwzPL72KltcE8f3anDrQUvsFTmJj4Kq2Tlt8JTeIhfITFia/Sijmj3bgC5wKX4C1chOkxuC6K+fQAZsC0AmMKcbVSzKf9qaPOUj7Vrlx3UryfhqC71dWi+XAdzsNeuAUHYWzwb4RjcBZ2wehgnw2HYQAuw7w2NmmZef5ehc0wokNsR82FL3DH/pw/veYLMAVGwik4Y14h75lfBxqI7Dv9JzYIS0Jbx3xRG9sCuAtTA2prbLnYtloBb2z4ey8OJqf15hUxSuX/JcwM3/USUYwq6L5g6zN/YmkHe8wnnbP1w2PYElBbfeViS1U6Ka3aUPg8HdAqa0JxUjqeK+EEvIe1bWx6dxb7jsrFlqq4C3G1es3vN+36c/MrQNKqH4LtcMB+vyU3mU82Z1tnvjvxxTLLPH9ysaVKk3pt3vEe80HojtNAbsNR8yKhzxehrd07AtvM808DzdmUo+rzBuwwL0LqNxdbquLxU2VTsUjP9yQbXmz0ONaA9SiO8TlblPouvi87xZairXDN/E/+CanC6QioMq1OfI0a/e/6BTcvfXd0xEaYAAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADQAAAAaCAYAAAD43n+tAAACk0lEQVR4Xu2XS6iNURTHlzzyliuvIpGUUm5RUsqdEIkBiqIMJGVgILp5DAxIZCCSyS0MFAMDkQnphsgjj4GJKMpYGRh6/H937c/Zd5/7PZzu4Hy3869f39dee31n7732Xmsfs44qa6LoE7/E5v+w5akVn2HXZNFvQw+gyJanVnz+CecesV5MC20zxMysQwUVDaDIlqdWfGysOCE+i4PigHglzovHYqn5pE6Jc+bbYMmAp2uSuf89cVK8tcYAymy0XRMXxZyoPc+nVGPEFXHT/EOZiMxL89VhlTaIj2K2WCYehj4sxg2xY8DL296YD6DIxu9eFruDjeclMc7yfSpptfhqPshUx8xXLhMDXCn2mUdwrlguPohFoU+8RYpstH0SvWJ7eN43H0+eTyWdFt/EvNQgHRFbwjsTeSHWmfftN5/QCvEuvKN4AEU2Jvsl9IlV5FNJ18UfcVSMTmyLRVd4px+riFi9Z2KbeRJ5LdYE2xTxxHwAbM882wTziOwMtlFik/li5flUEh9kQkC+fyT2iqlxJ2mreYT2iOPigbgtFoiN5mdql3nEv4vnorvExoLxnUPm25vooyKfUnEuzphPJpsYvLfmbUhfIsZqpiK608MzTi5lNkSJ4NuxynxKhSPp+az4YT6p/YN6tLmYACEfarVJ0b+tcWZqIQ42eZ96kIpM89N8D2diS5Cu023YNiId3xXjU4N5kaOIzo/amEifNdJp24nsQRRWJe1sQxICKbk2oliRcg+bV2XeSdUXzIsd1474bFET7pin07YURY1IoOw6w/Wjx5q34CzzLUjEbllz8a2dqDvcgq/a4CRRay0UT8NzRIgCS4S4Ca9NbLUUCYP/S1xgOX8jQtx6a58QOupoGPQXC/yJcdrUH7cAAAAASUVORK5CYII=>

[image7]: <data:image/png;base64,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>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAaCAYAAACzdqxAAAABTUlEQVR4Xu2ULUsEURSGj2BQ0KKCQcNiM4pY/ACDRo3rD7CYLWrbYhBEMBtFLEYFEYN/wigYXDaJIGpQ/HjeOfeye/cDdwymeeBhhz2HM2feubtmBf/NLNbwO3iLI0lHyjJ+mvfq8xqHk44m9rGKDzjeVItowCk+4xn2puVWBvAYD/EVp9NyRg9u4A5+4WZabs8EHmHZ/BFX0nLGlPngbfzA+bTcnlXzTWbwzVq36ccKjuEF3uFoY0MnKriEk/iIu0nVbM28rsH3ljNfvTBtoW1OzDMVJdwyH6ThufPtM7/JTVDXGqahJW/NrnPnK7Slto0ZakPFIHTjP+UbUb7KeRH3zF+cUFQ6413nqwOvOCLKTydDA3TEIrnyncNzHGz4TmdYZ1nxxBco9CS/5ruAT1b/f3jH9VDTr+7K6r//A3wJfbH3EodCvaCgoBt+AHZzRnAvsxTcAAAAAElFTkSuQmCC>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAaCAYAAAD1wA/qAAAC7UlEQVR4Xu2XS6hNURjHP3lE3o+SPK+BwsDAoxQTIQoDBgYMbnllJgbK6N5koGSAklIyMCAD8rxdSTFQRgYoMiAlAwaKiTz+v9Ze5+z93b3OU50r51+/zt1rrbPO/p5rXbOu/l+NFFPFCD9RQxPEWD/YSY0WJ8R2P5HQFDFdLBDXxfzCbAd1RJy2+tHYJ36K3+JiNrZW3BCT46JOaal4Jnr8REIrxXexK3vG+HPiaGVFBxRfAupFIwoDvonlubHV4pU17oy/rtnitVjvJxLC2EvihZiRG6dJENUYpaQmic1ibvbM5xYxq7KiNWHAWzHHT+REI1ghNlpYxwtjjI8gNXOlZLwiWtwF0S8+iDPivIWcfGnthZM9Hln4jTKtE28sNAPAaIr9QH5RJvZ6LCb6iahNFr64THy14A1C+UB8FourS5vWZQvtc5SfkFaJT2Jn9oynT9rQ+ojaKt5ZjSw5aMEIevwPscbCpqQWRiZD2YAwBLxopU8zYltN1UcUhnwUC/2EFymV2qRVpQyhdn5ZOCSjYkGX1QfCEDIGpydF3pF/NYupBaUMId8xJN/NSCfSqqw+UN3UQtQB9VBrk2sWDre94p7oFYssdJOr2d9eeJxaG+/GMcR7l9bKQciBSN3syM0h5mkGM914Qfn68OIs2COOiQExzYJX2JROQwR7rXqlyAvHlKUrtffFqkXNXYrzBo/T+s/a0CbD79+xOpfIPvHcwkXNixefJ26JbdkYLzBoIa8Rni+7QrCO9upfirPjlHhiIfXYmwi8F3fFISumOF2P7lf2GwVhZarXI6JCDcWOQZhjUdJ1MIprhFfsTqkTOd5y40vzHvnnqB4LV5Sy32hKpByewtjYJmM9MfdQLLGQgl67LXx3nJ9oQuxBHRLJtnTYQvohvHzfqvmNlyj+41b+fwPG3xYb/ESDIkI4ggO0bY2xojd8wdGVankLA29mn82I6PdZtakMC1Hw/Rac0qi4SO63YWREV139q/oD0Ut9aGVGHhIAAAAASUVORK5CYII=>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAZCAYAAADnstS2AAAA3UlEQVR4Xu3SsQtBURTH8StMlEUsSkZlMymLshgo/gKTyWKSzDJZ7GaLf0AM/gTKZLYaDRj4Hvfduu+6s1J+9Yl3z33XOc9T6meSRAZRt2Cnhhue2CIRLn8mhzMmbsGXqtKnt9yCL0NcUHQLEhlCCk1kscJO6SFDkU17TNELvt8xtzdJ8jhhhEiw1lX6SYT6jWGp9NQFa93br1zIovQnN0rk09uvDCM/17DW5JE90EEFA1MoKX2y6S2l9D92RRlj1IPae6A+DlhggzaOWGOGuNls4r4wsiFtXf/zpbwAH9wkzOofuXsAAAAASUVORK5CYII=>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAaCAYAAAC6nQw6AAABF0lEQVR4Xu3SMUtCURjG8TcyKChDdAlpDYIghwgEF7eECBHXoCkRnIpwMKLP0Fa4uLcVEdEg+Akc2tWxiKAhiJb+rx4Pr/c63vE+8MN7n8M913vOEYkTJ7okUcKmu1/CHsqmW8AWqu5X72eyiltcYYRjPOAULXzgEHe4xAkGOJdADlDDLr7xinU3toEh3rHvOk0HXZn8CZ+6TCap4A9FM7aNTzRNpw93cY+E6X1u8IaM6Y7wi4LpppM3TOezhp6E36KTD5A1nU7whR3T+Uzfcma6eZ+wgmdHry9kdu38+sz7BDu5brvuom6OHou2BBb8Gn2kTafn6gd50+lDT3jBI3JmbJxlCcxMFpGS8MHTXjdED22cOJHmH2DYLhijlc5IAAAAAElFTkSuQmCC>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAbCAYAAACqenW9AAAA9UlEQVR4Xu3SoYsCQRTH8ScqKOqhGC+IeAjX/AMuarJpNPgPWLQYxSheunbRfigGu2C0mkwGsVmMd3B33+fOwDK7cggXDP7gAztvht03Mytyk4kgj6w74WaET/yg58yFpoEvvLgTYXnDDo9OPZAMVlgg4cwF8owj+masmy2jhqRdZNPCN6qIY4gx5hKyYdtvCQNUxFsUOJ0c1tjgXbyWNNpGFykzPsf2exLv7drCg3+BP1ct9l/GE7aYyYUjdC9jIt4edC91tE1d0ljiAzFT08U61vN9RdHUpYADOrZAmthjaup6Qefog34uagsm+sU/f9V7/j+/q+oqHbeR1QMAAAAASUVORK5CYII=>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAaCAYAAACkVDyJAAABi0lEQVR4Xu2UvSuFYRjGL/lIIfkoiYikMBhkUMg/wGAiyylkslBEBiUbJaNOyWDwsSkfKQllMBsNSkyymV1X9/PkeYXyvmcwvL/6dd7n45z7vp/3fg6QkpLyX8inXbSfFgbzebTMfYoW2hmMY6EAG3SRXtH1YG2IvsGCVNN7+kKbgz1/ZoAu0XJ6TXfxWcEmLIiCaW6OPiNhwEnaRnvoOx1x8xX0DtEE6ukJLIHELNMn2uTGSuKVTvkNbm4NCd+hKKWX9JAWuLlhWMXdbixU/Wgwjk0tfYQ1jmfezWlNKBFV509gkO7TDjoBO+oMbaVZuueev8V34Kobq3P1Y2FH9tEF2HHW0XFYgme0EpbYA511ezKwwD+iI9Q7O6DndJre0Fu6Q7dgnSwUoIEewa6O0D3W99RsQsnrlH5FldXA3qlQplXOr42iKnWN/AmM0W3YPiWm4Or8nNFLj2HJKYiC+Y7W2gVthx19TpiBXSWhik5hxypUmZpohTa6ucQUIfq/Wxw8ixJE11NS4vEBXg46/3lhxiQAAAAASUVORK5CYII=>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFwAAAAaCAYAAAA67jspAAADkElEQVR4Xu2YS6hNURjHP3lEXnlE8rokQiKPwS1kgEIkj/KY3EImHqGIDG7JgCgZSUoG8h7JK9INRcgIE8kjj5GMyER8P99a3bX3WXufe7i5p+761b979lr7rLP3f33rW9+6IolEIpFI1CcTVIdVJ1XrVL2y3VGGqa6oFrvPefVx901RrVYNUXVx7XNU611/p2Ol6qVqmpgZB1S3Vf3DmyLMUH1T/SrQZnffmkjfe7Hf63SMVL2SbLQNUD1RbQnaYixVPRVbFaFaVHekdcK477XTI9V2VT/X1+nAaKKUaPWw7M+KGefTQowdqvm5Nky+pJoctGH4nuC6JrqKPdxcVfegnYfs6/7CONXU4LpeOS6VhsMZ1WfV2Fx7yHTVwOCadz0klqJC/tpwDD6m2qe6pzoa9C1TfRUzebDqhVR/4HoAY4sMj7WXgQcnJBuIgOGMd1MsrbxRbRIL3lLmqfaLLZv7YsvORzCRgsmYTdtu1SdpX8NZNeRMNpy2au2fb8YhXbRI3NhaDR+kuqtqzHeIGU6fXw28xwcxj0ozALMyUWzQ72K7L/hNJpyAEaobYhNQr/QW29xixtZqOF48l/j79nTy+D0C08cE7YU0S/ZmJuGLtJZBvu2IVJnBOqDI2KL2GNTspIvLqm65viIYn/JwUb4jj1+G4eArxCJ+lrsGZrxsOf8N5DwOD/kDRpnKqgw4KHFjMYSgYqVWwwcc38kzXvVRdVWyhylvOOmmFF7indjG6WEHpo0+YCKIbr8CGPSiWKm0USzVNIk9zCnVBfe5GqSAJapVNQgzymCj+ynZ8o7lf83JpwImuyG4DiFKMY/Jy+MPR6HhPqXEJroCX4H4wdmRMTOsSDi27hUbeLhqg9gE3RLbOJgYdutd7p4mMeM7Aja7x2Jp0uM3Nb9HAe+AqeekMm2QSumLlX4UGJjbELTxmffnkJSvaKKQQlhCFPgcgbeqHqgeii0VBvKnLAweJTbDRBMwq3yPzRaYvNjD/i9mipVqVA2sCgoA6unQDFbpD3cPQRKyU4oNB8Z/JhZ021RvVeel+r8OMvAwQ6U1R/IQRAvKPxBRThnpVwCnu9Ni9/GjmN/o+joK0tVC1XKx434t8N0FUn5cD8dvkEqP2pXZqutik8MPYbavaOijRp0ktmwT7QBLrtl9JqIpofxmQWSzifIfutGuLfGP9JBsPszv9Cy3Nm0eiUQikUgkEhX8Bl8zuQov8Or8AAAAAElFTkSuQmCC>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFwAAAAaCAYAAAA67jspAAADmklEQVR4Xu2YXchNWRjHHw2aiaFhImF8JEKiGFLIhZRkEqN83LyFuCBfRUS9NblgZkquNInmQhrcyVckGZlpuKG4IDESpSY3TErM/H+evcba+6xzzsbL+07v/tevs/fa6+yz9389z7PWOmaVKlWqVKlSx9QosVv8JJaKz/KXS6mLWC9WFy9IvcQ68/vvEAPylzuXFoqbYoLoKb4TZ0XvuFMJTRHPxJZC+xBxTawUn4o54paYHHfqLBosbotlUdsX4opYE7U1E4NzXvxjecO7iv3iWHYctFOctnfLpP+1MJqonBi1URoOiQvmEd9M9N8ovrfaCB8uHhXa0AKr/d2kPjHvNEN0i9r50c+zTzRCjI/OO6r2WvrFfzY3CsOaiVLyg5hqtYbPEq8KbWieeTbEmVUjDN4jtomL4sfo2jfiibnJX4obVv6B21MYW8/wVHtRlBImwqHmfYuGB2PrGV5sz2mm2G7+I7+ap12IYCIFkzGbts3iobWt4WTNVXH/LVjy+ptpUS4uWNrYMobznhvEouw8ZTjHKWNLGc4sO9o8df4Wi7P2MMnEAzBInDIfgI6qHuKcpY0tYzirDLI8lNaU4dT2lLGlDA9qFQ/EsOycQfhLrAodsjbqWkev4fWMrdceRHbsMy8lQSnD6xlbr71GIQ3jZQ4zLhH/dXaOiP5G6fwuYsLuZ75pKEuzVQbLs5SxGE5QkakpjRPXLV++Hpub+DQ7Z8KcJl5YrbHBcLxrKF7iT/OJM4ib0cY1xEAQ3SEDuPkRMVasMC81LWKk+Rr1l+y4mSgBc8W3bwGZ1khM9i/NzQlic3Iig2PEYA+NzlNKRfhAcc98jotFNaAqNHu+/1YgRAaifmFmvCKZLraalxN+cLn5AJ0RfcwH5o7YlPVpMTe+PdRX/GFeJoOYnInuMEch3oGIPGz5DUwsMpxMj4OR92Pn+ru92bkGzxrdKyfSgNE5ar4FXisuid/MU5FlUrg5Bn8ljptHEyIS+B6TLWLwiin3MTVJ3DVfWZEVLAB2WX6fQZY+z/oU5yXK3GXzTGFQgPISsgYvTppnMtv6A+Z+1StXSfEw/e1NjeQhiBYoPhBRzjIyZACL/YPm/XgYzJ+aXWsvUa5mi/nm2/22VtgwMqB8cv7BxMTBCDM4mIzZYUXDNf6DGGOetpXaQKxFW7NjIpo/bcKqgMhmEqXODcnaKr2nulu+HhZnetI5vl6pUqVKlSpVqlRe/wJE1cQOsWOX8AAAAABJRU5ErkJggg==>