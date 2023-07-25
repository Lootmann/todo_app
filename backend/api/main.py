from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers.todos import router as todo_router

app = FastAPI()

origins = [
    "http://localhost:5173",  # default vite port
    "http://localhost:5174",  # next vite port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo_router)
