import React, { useState } from "react";

const FileUpload = ({ onResult }) => {
  const [file, setFile] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;
    
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://localhost:5000/upload", {
      method: "POST",
      body: formData,
    });
    const text = await res.text();
    onResult(text);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <input
        type="file"
        accept=".csv"
        onChange={(e) => setFile(e.target.files[0])}
        className="block w-full text-sm text-gray-700"
      />
      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Predict
      </button>
    </form>
  );
};

export default FileUpload;
