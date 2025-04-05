from fastapi import FastAPI, UploadFile, File
from main import read
# import io
from typing import Annotated

app = FastAPI()
# import polars as pl

@app.post("/upload_excel")
async def create_file(file: Annotated[bytes | None, File()] = None):
    print(file)
    # if not file:
    #     return {"message": "No file sent"}
    # else:
    #     return {"file_size": len(file)}
    return read(file)