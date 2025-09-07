
from fastapi import APIRouter
from pydantic import BaseModel
import json, pathlib
from ..services.orchestrator import run_pipeline

router = APIRouter()

class RunRequest(BaseModel):
    project_id: str
    context_path: str
    aroma: str | None = None

@router.post("/projects/{pid}/run")
def run(pid: str, req: RunRequest):
    outdir = pathlib.Path("out")/pid
    outdir.mkdir(parents=True, exist_ok=True)
    ctx = json.load(open(req.context_path))
    artifacts = run_pipeline(ctx, outdir, aroma=req.aroma)
    return {"ok": True, "artifacts": [str(p) for p in artifacts]}
