from random import randint, sample
from string import ascii_letters, digits

from sqlmodel import Session

from api.models import todos as todo_model


def random_string(min_: int = 5, max_: int = 10):
    return "".join(sample(ascii_letters + digits, randint(min_, max_)))


class TodoFactory:
    @staticmethod
    def create_todo(db: Session, title: str = None, description: str = None) -> todo_model.TodoRead:
        if not title:
            title = random_string()

        if not description:
            description = random_string()

        todo = todo_model.TodoCreate(title=title, description=description)
        db_todo = todo_model.Todo.from_orm(todo)
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo
