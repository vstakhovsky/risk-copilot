
from pathlib import Path
from cli.artifacts.generator import generate_all
def run_pipeline(ctx, outdir: Path, aroma: str | None = None):
    return generate_all(ctx, outdir)
