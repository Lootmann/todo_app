from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session

from tests.factory import TodoFactory


class TestRouterTodoGET:
    def test_get_all_todos(self, client: TestClient, session: Session):
        TodoFactory.create_todo(session)
        TodoFactory.create_todo(session)
        TodoFactory.create_todo(session)

        resp = client.get("/todos")
        assert resp.status_code == status.HTTP_200_OK

        data = resp.json()
        assert len(data) == 3

    def test_get_one_todo(self, client: TestClient, session: Session):
        todo = TodoFactory.create_todo(session)
        resp = client.get(f"/todos/{todo.id}")
        data = resp.json()

        assert resp.status_code == status.HTTP_200_OK
        assert data["id"] == todo.id
        assert data["title"] == todo.title
        assert data["description"] == todo.description

    def test_get_one_todo_with_wrong_todoid(self, client: TestClient, session: Session):
        resp = client.get("/todos/101")
        data = resp.json()

        assert resp.status_code == status.HTTP_404_NOT_FOUND
        assert data["detail"] == "Todo 101 Not Found"
