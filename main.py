from fastapi import FastAPI
from generator import generate_password

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API activa. Usa /password o /docs"}

@app.get("/password")
def password(length: int = 16, symbols: bool = True):
    if length < 6 or length > 64:
        return {"error": "Password length must be between 6 and 64"}
    return {
        "password": generate_password(length, symbols)
    }
