
from pathlib import Path
def make_diagrams(ctx, outdir: Path):
    d = outdir/"diagrams"; d.mkdir(exist_ok=True)
    (d/"process.mmd").write_text("flowchart LR\n  A[Intake] --> B[Risk Analysis]\n  B --> C[Scope Options]\n  C --> D[RACI]\n  D --> E[ADR]\n  E --> F[Diagrams]\n  F --> G[Validate & Export]\n")
    (d/"architecture.mmd").write_text("flowchart TB\n  UI[Web UI] --> API[FastAPI Orchestrator]\n  API --> AGENTS[Claude Sub-Agents via MCP]\n  API --> DB[(Database)]\n  API --> ART[(Artifacts Repo)]\n  API --> VEC[(Vector DB)]\n  UI -. \"diffs\" .-> ART\n")
    return [str(d/"process.mmd"), str(d/"architecture.mmd")]
