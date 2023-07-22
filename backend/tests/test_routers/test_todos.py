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

    def test_get_all_todos_filtered_by_title(self, client: TestClient, session: Session):
        TodoFactory.create_todo(session, title="hoge", description="ほげ")
        TodoFactory.create_todo(session, title="hage", description="はげ")
        TodoFactory.create_todo(session, title="higa", description="ひが")

        resp = client.get("/todos?title=a")
        data = resp.json()

        assert resp.status_code == status.HTTP_200_OK
        assert len(data) == 2

        resp = client.get("/todos?title=h")
        data = resp.json()
        assert len(data) == 3

        resp = client.get("/todos?title=z")
        data = resp.json()
        assert len(data) == 0

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


class TestRouterTodoPOST:
    def test_create_todo(self, client: TestClient, session: Session):
        resp = client.post("/todos", json={"title": "hoge", "description": "ほげ"})
        data = resp.json()

        assert resp.status_code == status.HTTP_201_CREATED
        assert data["id"] == 1
        assert data["title"] == "hoge"
        assert data["description"] == "ほげ"
