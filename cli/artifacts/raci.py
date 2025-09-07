from pathlib import Path
import csv

def make_raci(ctx, outdir: Path):
    p = outdir / "raci.csv"
    rows = [
        ["Task","Owner","R","A","C","I"],
        ["Define scope","TPM","✔","","C","I"],
    ]
    with p.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return [str(p)]
