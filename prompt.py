from langchain_core.prompts import PromptTemplate


NFe_EXTRACT_PROMPT = PromptTemplate(
    template="""You are an intelligent document parser specialized in Brazilian invoices (NF-e - Nota Fiscal Eletrônica).
Your task is to extract structured information from the invoice image or PDF provided.""",
    input_variables=[],
)
