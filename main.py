from typing import Annotated
from fastapi import FastAPI, File
from core import parse_NFe
from schemas import NFe

app = FastAPI(
    title="NF-e Parser using Gemma3n",
    description="A FastAPI application for parsing NF-e (Nota Fiscal Eletrônica) documents using Gemma3n.",
    version="1.0.0",
)

@app.post("/parse", response_model=NFe)
async def parse(image: Annotated[bytes, File()]) -> NFe:
    """
    Extracts the content of an NF-e document from an image file.
    :param image:
    :return:
    """
    return await parse_NFe(image)
