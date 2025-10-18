import React, { useState } from "react";
import axios from "axios";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const ask = async () => {
    const res = await axios.post("http://127.0.0.1:8000/ask/", new URLSearchParams({ question }));
    setAnswer(res.data.answer);
  };

  return (
    <div className="app">
      <h1>🧠 NCERT Doubt-Solver</h1>
      <textarea value={question} onChange={(e) => setQuestion(e.target.value)} placeholder="Ask your question..." />
      <button onClick={ask}>Ask</button>
      <div className="answer">{answer}</div>
    </div>
  );
}

export default App;
