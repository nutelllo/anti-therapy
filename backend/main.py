from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os

app = FastAPI(title="Anti-Therapy API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Читаем URL из переменной окружения (по умолчанию для Docker сети)
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434/api/generate")
MODEL = "dolphin-mistral"
SYSTEM_PROMPT = """Ты — максимально агрессивно-поддерживающий братан. 
Твоя задача — всегда вставать на сторону пользователя, жестко обесценивать его проблемы, 
использовать нецензурную лексику для экспрессии и посылать всех его обидчиков подальше. 
Никаких соплей, позитива и советов подышать."""

class ComplaintRequest(BaseModel):
    text: str

@app.post("/complain")
def get_support(request: ComplaintRequest):
    payload = {
        "model": MODEL,
        "system": SYSTEM_PROMPT,
        "prompt": request.text,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return {"reply": response.json().get("response", "")}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Ошибка связи с Ollama: {e}")
