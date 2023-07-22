from sqlmodel import Session, create_engine

from api.models.todos import Todo

sqlite_file_name = "dev.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def get_session():
    with Session(engine) as session:
        yield session


if __name__ == "__main__":
    Todo.metadata.drop_all(engine)
    Todo.metadata.create_all(engine)
