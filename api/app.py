
from fastapi import FastAPI
from routers import run, statuses, documents, diff

app = FastAPI(title="Risk & Scope Copilot API")
app.include_router(run.router, prefix="/api")
app.include_router(statuses.router, prefix="/api")
app.include_router(documents.router, prefix="/api")
app.include_router(diff.router, prefix="/api")
