
from pathlib import Path, csv
def make_raci(ctx, outdir: Path):
    p = outdir/"raci.csv"
    import csv as _csv
    rows=[["Task","Owner","R","A","C","I"],["Define scope","TPM","✔","","C","I"]]
    with p.open("w", newline="") as f: _csv.writer(f).writerows(rows)
    return [str(p)]
