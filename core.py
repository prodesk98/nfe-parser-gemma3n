from langchain_core.messages import HumanMessage
from langchain_ollama.chat_models import ChatOllama
from environment import env
from schemas import NFe
from PIL import Image

import base64
from io import BytesIO


llm = ChatOllama(
    base_url=env.OLLAMA_API_URL,
    model=env.OLLAMA_MODEL,
    temperature=0,
)


llm_with_structure = llm.with_structured_output(NFe)


def convert_jpeg_bytes_to_base64(image: bytes) -> str:
    """
    Converts JPEG image bytes to a Base64 encoded string.

    Args:
        image (bytes): The image bytes to convert.

    Returns:
        str: Base64 encoded string of the image.
    """
    buffered = BytesIO()
    image = Image.open(BytesIO(image))
    if image.mode == "RGBA": image = image.convert("RGB")
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


async def parse_NFe(image: bytes) -> NFe:
    """
    Parses the NF-e (Nota Fiscal Eletrônica) document from the provided image bytes.

    Args:
        image (bytes): The image bytes of the NF-e document.

    Returns:
        str: The parsed content of the NF-e document.
    """
    message = HumanMessage(
        content=[
            {"type": "text", "text": "Please extract the structured information from the NF-e document in the image."},
            {
                "type": "image",
                "source_type": "base64",
                "data": convert_jpeg_bytes_to_base64(image),
                "mime_type": "image/jpeg",
            },
        ],
    )
    result = await llm_with_structure.ainvoke([message])
    return result