const ResultBox = ({ result }) => {
  return (
    <div className="bg-gray-100 p-4 rounded mt-4 whitespace-pre-wrap">
      {result ? result : "Results will appear here..."}
    </div>
  );
};

export default ResultBox;
