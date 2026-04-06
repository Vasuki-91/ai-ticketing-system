import React, { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const askAI = async () => {
    setLoading(true);
    try {
      const res = await fetch("https://ai-ticketing-system-c1y6.onrender.com/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question }),
      });

      if (!res.ok) {
        throw new Error("Server error");
      }

      const data = await res.json();

      // ✅ Store FULL response
      setResponse(data);

    } catch (error) {
      console.error(error);

      // ✅ Safe error structure
      setResponse({
        answer: "Error connecting to backend",
        analysis: {}
      });
    }
    setLoading(false);
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1 style={styles.title}>🎫 AI Ticketing System</h1>

        <input
          type="text"
          placeholder="Describe your issue..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          style={styles.input}
        />

        <button onClick={askAI} style={styles.button}>
          {loading ? "Processing..." : "Submit"}
        </button>

        {response && (
          <div style={styles.result}>
            <h3>Response</h3>

            {/* ✅ Answer */}
            <p>{response.answer}</p>

            {/* ✅ Safe optional rendering */}
            {response.analysis && (
              <>
                <p><b>Category:</b> {response.analysis.category}</p>
                <p><b>Severity:</b> {response.analysis.severity}</p>
                <p><b>Sentiment:</b> {response.analysis.sentiment}</p>
                <p><b>Department:</b> {response.analysis.department}</p>
                <p><b>Action:</b> {response.analysis.action}</p>
                <p><b>Confidence:</b> {response.analysis.confidence}</p>
              </>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

const styles = {
  container: {
    height: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    background: "#f4f6f8",
  },
  card: {
    background: "white",
    padding: "30px",
    borderRadius: "12px",
    boxShadow: "0 4px 10px rgba(0,0,0,0.1)",
    width: "400px",
    textAlign: "center",
  },
  title: {
    marginBottom: "20px",
  },
  input: {
    width: "100%",
    padding: "10px",
    marginBottom: "15px",
    borderRadius: "8px",
    border: "1px solid #ccc",
  },
  button: {
    width: "100%",
    padding: "10px",
    background: "#007bff",
    color: "white",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer",
    fontWeight: "bold",
  },
  result: {
    marginTop: "20px",
    textAlign: "left",
    background: "#f9f9f9",
    padding: "15px",
    borderRadius: "8px",
  },
};

export default App;