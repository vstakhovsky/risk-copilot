from pathlib import Path

def make_diagrams(ctx, outdir: Path):
    d = outdir / "diagrams"
    d.mkdir(parents=True, exist_ok=True)
    (d/"process.mmd").write_text("""flowchart LR
  A[Intake] --> B[Risk Analysis]
  B --> C[Scope Options]
  C --> D[RACI]
  D --> E[ADR]
  E --> F[Diagrams]
  F --> G[Validate & Export]
""")
    (d/"architecture.mmd").write_text("""flowchart TB
  UI[Web UI] --> API[FastAPI Orchestrator]
  API --> AGENTS[Claude Sub-Agents via MCP]
  API --> DB[(Database)]
  API --> ART[(Artifacts Repo)]
  API --> VEC[(Vector DB)]
  UI -. "diffs" .-> ART
""")
    return [str(d/"process.mmd"), str(d/"architecture.mmd")]
