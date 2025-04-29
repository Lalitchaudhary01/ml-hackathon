import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import ResultBox from "./components/ResultBox";

function App() {
  const [result, setResult] = useState("");

  return (
    <div className="min-h-screen bg-white text-black p-6 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">🎓 Student Risk Predictor</h1>
      <FileUpload onResult={setResult} />
      <ResultBox result={result} />
    </div>
  );
}

export default App;
