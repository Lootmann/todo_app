from typing import List

from sqlmodel import Session, select

from api.models import todos as todo_model


def get_all_todos(db: Session) -> List[todo_model.TodoRead]:
    return db.exec(select(todo_model.Todo)).all()


def find_by_id(db: Session, todo_id: int) -> todo_model.TodoRead | None:
    stmt = select(todo_model.Todo).where(todo_model.Todo.id == todo_id)
    return db.exec(stmt).first()


def filter_by_title(db: Session, title: str) -> List[todo_model.TodoRead]:
    # FIXME: There has to be a better way :^)
    stmt = select(todo_model.Todo).filter(todo_model.Todo.title.ilike(f"%{title}%"))
    return db.exec(stmt).all()


def create_todo(db: Session, todo: todo_model.Todo) -> todo_model.TodoRead:
    db_todo = todo_model.Todo.from_orm(todo)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo(db: Session, origin: todo_model.Todo, todo: todo_model.Todo) -> todo_model.TodoRead:
    origin.title = todo.title
    origin.description = todo.description

    db.add(origin)
    db.commit()
    db.refresh(origin)

    return origin


def delete_todo(db: Session, origin: todo_model.Todo) -> None:
    db.delete(origin)
    db.commit()
