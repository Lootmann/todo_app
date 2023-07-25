import { Sidebar } from "./components/Sidebar";
import { Header } from "./components/Header";
import axios from "axios";
import React from "react";

type Todo = {
  id: number;
  title: string;
  description: string;
};

const URL = "http://127.0.0.1:8888/todos";

function App() {
  const [todos, setTodos] = React.useState<Todo[]>([]);

  React.useEffect(() => {
    axios.get(URL).then((resp) => {
      setTodos(resp.data);
    });
  });

  return (
    <div
      className="min-h-screen bg-neutral-950 text-slate-200 text-xl
      flex"
    >
      <div className="flex-1 flex">
        <Sidebar />

        <div className="flex flex-1 flex-col">
          <Header />

          <div className="p-4">
            <h2>Main Content</h2>

            <ul>
              {todos.map((todo) => (
                <li>
                  {todo.id} {todo.title} {todo.description}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
