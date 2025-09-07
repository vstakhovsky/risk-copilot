# 🚀 Risk Copilot

**Multi-agent “Risk & Constraints Analyzer”** that transforms messy inputs into clear deliverables.

Tired of Technical Product Managers cutting off context, missing critical project files and stakeholders, and spitting out incomplete risk assessments?
Save your project with Risk Copilot! → Upload your complete project context → Configure specialized AI agents → Get comprehensive risk analysis, scope options, RACI matrices, ADRs, and diagrams → Export results directly into your project management workflow. 5 specialized agents per day! → Drop those deliverables into Jira, Confluence, or GitHub and apply the entire project strategy in a single integration.
That means you get 5 comprehensive, fully coherent project analyses per day for your entire organization—absolutely streamlined, thanks to complete context transfer and multi-agent intelligence.
Perfect for complex projects:

- **🏗️ Enterprise Software Development
- **🏦 Financial Services & Compliance
- **🏥 Healthcare & Regulated Industries
- **🚀 Startup Product Launches

---

## 🖼️ Screenshots


<img width="697" height="168" alt="Screenshot 2025-09-08 at 00 11 56" src="https://github.com/user-attachments/assets/067f0186-dace-4b89-bfdd-6a45750fe7de" />

<img width="618" height="608" alt="Screenshot 2025-09-08 at 00 12 20" src="https://github.com/user-attachments/assets/b32fb337-1e71-4b0d-bf47-7765b1bca0ef" />

---

## 🌍 Table of Contents

- [Problem](#-problem)
- [Value](#-value)



---

## 🌍 Problem
Technical Product Managers spend days aligning risks, dependencies, legal and operational constraints across Jira, Confluence, GitHub, and endless meetings.  
This leads to delays, misalignment, and knowledge loss.

---

## 💎 Value
- Ready-to-use **PR artifacts** with traceable evidence and GitHub-style diffs.  
- Unified **status dashboard** for releases, dependencies, and scope changes.  
- Seamless integration into existing workflows.

---

## 📊 Data Flow
- **Input:** Context JSON, documents, *aromas* (prompt profiles).  
- **Output:**  
  - `out/risks.md`  
  - `out/scope_options.md`  
  - `out/raci.csv`  
  - `out/adr-*.md`  
  - `out/diagrams/*.mmd`

---

## ✅ Functional / 🔒 Non-Functional
**Functional**  
- Risks / Scope / RACI / ADR / Diagrams generation  
- Evidence & confidence scores  
- REST API + CLI  
- GitHub diffs & status dashboard  

**Non-Functional**  
- Traceability & audit logs  
- Secrets protection (KMS)  
- Horizontal scalability  
- Security-first design

---

## ⚙️ Tech Stack
- **Backend:** Python 3.11 + FastAPI  
- **Agents:** Claude MCP (v0.2+)  
- **DB:** SQLite / Postgres  
- **Vector Store:** Qdrant / FAISS  
- **Frontend:** Next.js (v0.2)  
- **Infra:** Replit / Vercel  

---

## 🏗️ Architecture

flowchart TB
  UI[Web UI] --> API[FastAPI Orchestrator]
  API --> AGENTS[Claude Sub-Agents via MCP]
  API --> DB[(Database)]
  API --> ART[(Artifacts Repo)]
  API --> VEC[(Vector DB)]
  UI -. "diffs" .-> ART



---

## 🔁 Process Pipeline
flowchart LR
  A[Intake] --> B[Risk Analysis]
  B --> C[Scope Options]
  C --> D[RACI Matrix]
  D --> E[ADR Records]
  E --> F[Diagrams]
  F --> G[Validate & Export]

---

## 📐 UML Sequence

sequenceDiagram
  participant U as User
  participant UI as Web UI
  participant API as FastAPI
  participant A as Claude Agents
  participant Repo as Repo/DB

  U->>UI: Upload docs + select aroma
  UI->>API: POST /run
  API->>A: analyze_risks, scope_options, make_raci, generate_adr
  A-->>API: artifacts + evidence
  API->>Repo: store artifacts
  API-->>UI: run_completed
  UI-->>U: Show diffs, evidence, status

---

## 🔐 AI Security

Threats
- Prompt injection / jailbreak
- Indirect injection (via external docs)
- Data exfiltration
- Tool abuse / SSRF / supply-chain
- RAG poisoning

Controls
- Guardrails & content filters
- Evidence + confidence scores
- HITL checkpoints
- Allow-/deny-lists for tools
- Sandbox execution
- IAM least-privilege
- KMS for secrets
- Immutable logs
- Continuous CI/CD security evals

---
## 📈 Roadmap
- v0.2: UI + MCP
- v0.3: BPMN/PR Flow integration
- v1.0: RBAC + full audit

------
## 🚀 Quick Start

# Generate artifacts
python3 src/riskcopilot.py --input data/context.json --out out/

# Run API server
pip install -r server/requirements.txt
uvicorn server.main:app --reload



