from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from core.uitility import encode_image
from pydantic import BaseModel, Field
from openai import OpenAI
import instructor


# Pydantic Structured models
class Node(BaseModel):
    id: int
    label: str
    color: str

class Edge(BaseModel):
    source: int
    target: int
    label: str
    color: str = "black"

class KnowledgeGraph(BaseModel):
    nodes: list[Node] = Field(..., default_factory=list)
    edges: list[Edge] = Field(..., default_factory=list)

# LLM
model_id = "gpt-4o-mini"
# llm = ChatOpenAI(model='gpt-4o-mini')
# llm = llm.with_structured_output(KnowledgeGraph, method="json_schema")

llm = OpenAI()
llm = instructor.from_openai(llm)

def generate_graph(image_path) -> KnowledgeGraph:
    try:
        # Encode the image
        base64_image = encode_image(image_path)

        response = llm.chat.completions.create(
            model=model_id,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Describe the relationship between rooms, windows and doors openings and connectivity. Start from the entrance and describe the layout as if you are giving a walking tour of the layout. Output a array of nodes(id, label, color) and the edges(source, target, label). Help me understand the following image by describing it as a detailed knowledge graph:"},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
                    ],
                }
            ],
            response_model=KnowledgeGraph,
        )
        print(response)
        return response
    except Exception as e:
        raise