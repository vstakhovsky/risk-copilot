
from fastapi import APIRouter
router = APIRouter()
@router.get("/projects/{pid}/statuses")
def statuses(pid: str):
    return {"project": pid, "releases": [], "dependencies": [], "recommendations": []}
