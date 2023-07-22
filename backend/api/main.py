from fastapi import FastAPI

from api.routers.todos import router as todo_router

app = FastAPI()

app.include_router(todo_router)
