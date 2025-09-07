
from fastapi import APIRouter
import difflib
router = APIRouter()
@router.get("/diff")
def unified(a: str, b: str):
    with open(a) as fa, open(b) as fb:
        diff = list(difflib.unified_diff(fa.readlines(), fb.readlines(), fromfile=a, tofile=b))
    return {"diff": "".join(diff)}
