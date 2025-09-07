
from pathlib import Path
def make_adr(ctx, outdir: Path):
    p = outdir/"adr-0001-decision.md"
    p.write_text("# ADR-0001: Example\n\nContext/Decision/Consequences TBD\n")
    return [str(p)]
