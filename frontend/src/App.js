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
        body: JSON.stringify({ question: question }), // ✅ FIXED
      });

      const data = await res.json();
      setResponse(data);
    } catch (error) {
      console.error(error);
      setResponse({ answer: "Error connecting to backend" });
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
            <p>{response.answer}</p>

            {response.ticket_id && (
              <p><b>Ticket ID:</b> {response.ticket_id}</p>
            )}

            {response.status && (
              <p><b>Status:</b> {response.status}</p>
            )}

            {response.category && (
              <p><b>Category:</b> {response.category}</p>
            )}

            {response.severity && (
              <p><b>Severity:</b> {response.severity}</p>
            )}

            {response.department && (
              <p><b>Department:</b> {response.department}</p>
            )}

            {response.sentiment && (
              <p><b>Sentiment:</b> {response.sentiment}</p>
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