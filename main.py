from fastapi import FastAPI
from routes.routes import router as player_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Football Stats API"}

app.include_router(player_router)