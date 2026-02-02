from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Vehicle Inspection Backend")
app.include_router(router)
