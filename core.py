from langchain_ollama import OllamaLLM
from environment import env
from schemas import NFe

llm = OllamaLLM(
    base_url=env.OLLAMA_API_URL,
    model=env.OLLAMA_MODEL,
)

model_with_structure = llm.with_structured_output(NFe)

async def parse_nfe(image: bytes) -> NFe:
    """
    Parses the NF-e (Nota Fiscal Eletrônica) document from the provided image bytes.

    Args:
        image (bytes): The image bytes of the NF-e document.

    Returns:
        str: The parsed content of the NF-e document.
    """
    # TODO: Implement the actual parsing logic using the model_with_structure
    return NFe()