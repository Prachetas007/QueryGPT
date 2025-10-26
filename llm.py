# vertex_llm.py
from langchain.llms import VertexAI
from langchain import PromptTemplate, LLMChain

# Prompt for SQL generation
prompt = PromptTemplate(
    input_variables=["question"],
    template="""
    You are a BigQuery expert.
    Convert the following natural language question into a syntactically valid BigQuery SQL query.
    Only output the SQL query.
    Question: {question}
    SQL:
    """
)

# Vertex AI LLM (text-bison)
llm = VertexAI(model_name="text-bison@latest", temperature=0.2)

# LangChain chain
chain = LLMChain(prompt=prompt, llm=llm)
