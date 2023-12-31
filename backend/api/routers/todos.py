from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from api.cruds import todos as todo_api
from api.db import get_session
from api.models import todos as todo_model

router = APIRouter(tags=["todos"])


@router.get(
    "/todos",
    response_model=List[todo_model.TodoRead],
    status_code=status.HTTP_200_OK,
)
def read_todos(*, db: Session = Depends(get_session), title: str = None):
    if title:
        return todo_api.filter_by_title(db, title)
    return todo_api.get_all_todos(db)


@router.get(
    "/todos/{todo_id}",
    response_model=todo_model.TodoRead,
    status_code=status.HTTP_200_OK,
)
def read_todo(*, db: Session = Depends(get_session), todo_id: int):
    found = todo_api.find_by_id(db, todo_id)
    if not found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo {todo_id} Not Found"
        )
    return found


@router.post(
    "/todos",
    response_model=todo_model.TodoRead,
    status_code=status.HTTP_201_CREATED,
)
def create_todo(*, db: Session = Depends(get_session), todo: todo_model.TodoCreate):
    return todo_api.create_todo(db, todo)


@router.patch(
    "/todos/{todo_id}",
    response_model=todo_model.TodoRead,
    status_code=status.HTTP_200_OK,
)
def update_todo(*, db: Session = Depends(get_session), todo_id: int, todo: todo_model.TodoUpdate):
    found = todo_api.find_by_id(db, todo_id)
    if not found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo {todo_id} Not Found"
        )
    return todo_api.update_todo(db, found, todo)


@router.delete(
    "/todos/{todo_id}",
    response_model=None,
    status_code=status.HTTP_200_OK,
)
def delete_todo(*, db: Session = Depends(get_session), todo_id: int):
    found = todo_api.find_by_id(db, todo_id)
    if not found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo {todo_id} Not Found"
        )
    return todo_api.delete_todo(db, found)
