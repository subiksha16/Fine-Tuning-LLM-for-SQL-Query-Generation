# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from mlx_lm.generate import generate
from mlx_lm.utils import load

# Create FastAPI app
app = FastAPI()

# Load model once at startup
model, tokenizer = load(
    "mlx-community/Ministral-8B-Instruct-2410-4bit",
    adapter_path="adapters"
)

# Define input data model
class Query(BaseModel):
    prompt: str

# Endpoint for SQL generation
@app.post("/generate")
def generate_sql(query: Query):
    instruction = f"Translate the following request into a SQL query:\n{query.prompt}"
    output = generate(model, tokenizer, instruction)
    #output = generate(model, tokenizer, query.prompt)
    return {"sql": output}