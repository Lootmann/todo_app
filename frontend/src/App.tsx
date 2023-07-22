import { Sidebar } from "./components/Sidebar";
import { Header } from "./components/Header";

function App() {
  return (
    <div
      className="min-h-screen bg-neutral-950 text-slate-200 text-xl
      flex"
    >
      <div className="flex-1 flex">
        <Sidebar />

        <div className="flex flex-1 flex-col">
          <Header />

          <p className="p-4">Main Content</p>
        </div>
      </div>
    </div>
  );
}

export default App;
