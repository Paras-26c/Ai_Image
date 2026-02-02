from fastapi import APIRouter, UploadFile, File
import os, uuid
from app.services.inspector import inspect_images

router = APIRouter()

@router.post("/api/v1/image/inspect")
async def inspect(files: list[UploadFile] = File(...)):
    paths = []
    os.makedirs("temp", exist_ok=True)

    for f in files:
        path = f"temp/{uuid.uuid4()}_{f.filename}"
        with open(path, "wb") as out:
            out.write(await f.read())
        paths.append(path)

    return inspect_images(paths)
