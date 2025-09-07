
from pathlib import Path
def make_scope(ctx, outdir: Path):
    md = ["# Scope Options (Quarter)","## A — Minimal","- bullets...",
          "## B — Realistic","- bullets...","## C — Stretch","- bullets..."]
    p = outdir/"scope_options.md"; p.write_text("\n".join(md)); return [str(p)]
