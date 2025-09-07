
from pathlib import Path
from .risks import make_risks
from .scope import make_scope
from .raci import make_raci
from .adr import make_adr
from .diagrams import make_diagrams

def generate_all(ctx, outdir: Path):
    out = []
    out += make_risks(ctx, outdir)
    out += make_scope(ctx, outdir)
    out += make_raci(ctx, outdir)
    out += make_adr(ctx, outdir)
    out += make_diagrams(ctx, outdir)
    return out
