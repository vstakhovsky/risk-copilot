
import json, argparse, pathlib
from artifacts.generator import generate_all

def main():
    p = argparse.ArgumentParser(description="Risk & Scope Copilot — CLI v0.1")
    p.add_argument("--input", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()
    outdir = pathlib.Path(args.out); outdir.mkdir(parents=True, exist_ok=True)
    ctx = json.load(open(args.input))
    artifacts = generate_all(ctx, outdir)
    print("[ok] artifacts:"); [print(" -", a) for a in artifacts]

if __name__ == "__main__":
    main()
