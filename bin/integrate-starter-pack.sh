#!/usr/bin/env bash
set -euo pipefail
SRC="${1:-$HOME/Downloads/risk-copilot-starter-pack}"
DST="$(pwd)"

echo "[i] source: $SRC"
echo "[i] dest  : $DST"

git checkout -b feat/starter-pack || true

# merge files (exclude .git)
rsync -av --exclude=".git" "$SRC"/ "$DST"/

# ensure .gitignore entries
cat >> .gitignore <<'EOF'
ui/.next/
ui/node_modules/
ui/.turbo/
out/
uploads/
dist/
__pycache__/
EOF

git add .
git commit -m "feat: integrate starter pack (CLI, API skeleton, UI scaffold, workflows, templates)" || true
git push -u origin feat/starter-pack
echo "[✓] done. Open a Pull Request on GitHub."
