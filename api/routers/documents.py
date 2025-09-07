
from fastapi import APIRouter, UploadFile, File
import pathlib
router = APIRouter()
@router.post("/documents")
async def upload(file: UploadFile = File(...)):
    path = pathlib.Path("uploads")/file.filename
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as f: f.write(await file.read())
    return {"ok": True, "path": str(path)}
