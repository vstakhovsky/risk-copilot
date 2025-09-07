
from pathlib import Path
def make_risks(ctx, outdir: Path):
    md = ["# Risks & Constraints",
          "- **Architecture**: <fill> [evidence: <link>]",
          "- **Legal**: <fill> [evidence: <link>]",
          "- **Operations**: <fill> [evidence: <link>]",
          "- **Security**: <fill> [evidence: <link>]",
          "- **Dependencies**: <fill> [evidence: <link>]"]
    p = outdir/"risks.md"; p.write_text("\n".join(md)); return [str(p)]
