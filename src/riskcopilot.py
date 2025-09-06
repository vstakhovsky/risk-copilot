
import json, os, argparse, pathlib, csv
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input", default="data/context.json"); ap.add_argument("--out", default="examples/output"); a=ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    ctx=json.load(open(a.input))
    rows="|Dom|Risk|\n|---|---|\n" + "\n".join([f"|{d}|{r}|" for d,items in ctx["constraints"].items() for r in items])
    open(os.path.join(a.out,"risks.md"),"w").write(open("templates/risk_md.md").read().format(project=ctx["project"]["name"],quarter=ctx["project"]["quarter"],rows=rows))
    with open(os.path.join(a.out,"raci.csv"),"w",newline="") as f: csv.writer(f).writerows([["Task","R","A","C","I"],["Add 3DS routing","Tech Lead","PM","Legal","Ops"]])
    open(os.path.join(a.out,"scope_options.md"),"w").write(open("templates/scope_options.md").read().format(project=ctx["project"]["name"],quarter=ctx["project"]["quarter"]))
    open(os.path.join(a.out,"adr-0001-3ds.md"),"w").write(open("templates/adr.md").read().format(number="0001",title="3DS Routing",context="..."))
    print("generated", a.out)
if __name__=="__main__": main()
