from fastapi import FastAPI
from chatbot import chat

app = FastAPI()

@app.get("/ask")
def ask(question: str):
    return {"response": chat(question)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)