from fastapi import FastAPI
from src.routes import blocks, transactions, accounts
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()
PORT = int(os.getenv("PORT", 8000))

app = FastAPI(title="MCP Ethereum Context Server")

# Register routes
app.include_router(blocks.router, prefix="/context/block")
app.include_router(transactions.router, prefix="/context/transaction")
app.include_router(accounts.router, prefix="/context/account")

@app.get("/")
def root():
    return {"message": "MCP Ethereum Context Server running 🚀"}

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=PORT, reload=True)
