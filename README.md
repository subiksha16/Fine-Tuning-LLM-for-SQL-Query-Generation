# English → SQL Query Generator (Fine-Tuned LLM)

This project fine-tunes an open-source large language model (LLM) to **translate English natural language queries into SQL**. It leverages **MLX-LM**, **LoRA**, and parameter-efficient fine-tuning techniques to improve SQL generation accuracy and reduce inference errors.

---

## 🚀 Features

- Fine-tuned **Mistral 8B / Llama** on English-to-SQL datasets.
- Parameter-efficient fine-tuning using **LoRA**, reducing inference errors by ~25%.
- RESTful API built with **FastAPI** for seamless integration.
- **Streamlit / HTML frontend** for interactive query generation.

---

## 🛠 Tech Stack

- **Model & Training:** MLX-LM, Mistral 8B, LoRA fine-tuning  
- **Backend:** FastAPI, Pydantic, Python 3.12  
- **Frontend:** Streamlit + HTML/CSS/JS  
- **Data:** Custom English-to-SQL datasets (JSONL)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/english-to-sql-llm.git
cd english-to-sql-llm
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Ensure your LoRA adapters and dataset are in place:
```bash
adapters/       # fine-tuned model adapters
data/           # train.jsonl, valid.jsonl, test.jsonl
```
4. Running the API
Start the FastAPI backend:
```bash
uvicorn app:app --reload
```
📁 Project Structure
```bash
EnglishToSQL_Final/
│
├─ app.py                  # FastAPI backend
├─ frontend.py             # Streamlit frontend
├─ index.html              # Optional web interface
├─ data/                   # JSONL/CSV datasets
├─ adapters/               # LoRA adapters
└─ README.md
```





 
