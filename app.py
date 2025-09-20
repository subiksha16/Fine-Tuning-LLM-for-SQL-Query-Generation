# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from mlx_lm.generate import generate
from mlx_lm.utils import load
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI()
# Allow frontend (browser) requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify ["http://localhost:3000"] etc.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    #instruction = f"Translate the following request into a SQL query:\n{query.prompt}"
    instruction = f"""
Translate the following request into a SQL query.
Return **only the SQL query**, with no explanation, no formatting, no markdown.

Request: {query.prompt}
"""

    output = generate(model, tokenizer, instruction)
    #output = generate(model, tokenizer, query.prompt)
    return {"sql": output}