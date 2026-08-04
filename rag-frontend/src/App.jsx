import { useState } from 'react';

function App() {
  const [messages, setMessages] = useState([
    { sender: 'ai', text: 'Hello! Ask me any question regarding NVIDIA\'s financial performance or corporate directives.' }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { sender: 'user', text: input };
    setMessages((prev) => [...prev, userMessage]);
    const currentInput = input;
    setInput('');
    setIsLoading(true);

    try {
      // Calling your live local FastAPI backend server
      const baseUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000'; // Default to localhost if not set
      const response = await fetch(`${baseUrl}/ask`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: currentInput }),
      });

      const data = await response.json();
      setMessages((prev) => [...prev, { sender: 'ai', text: data.answer || 'No response key found.' }]);
    } catch (error) {
      console.error("Error communicating with API:", error);
      setMessages((prev) => [...prev, { sender: 'ai', text: 'Error: Could not reach the corporate AI backend.' }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '700px', margin: '40px auto', padding: '20px', fontFamily: 'Segoe UI, sans-serif' }}>
      <h2 style={{ textAlign: 'center', color: '#1a1a1a', marginBottom: '20px' }}>📊 Enterprise Financial Intelligence Engine</h2>

      <div style={{ border: '1px solid #e0e0e0', height: '450px', overflowY: 'auto', padding: '20px', marginBottom: '15px', borderRadius: '12px', backgroundColor: '#f9f9f9', display: 'flex', flexDirection: 'column', gap: '15px' }}>
        {messages.map((msg, index) => (
          <div key={index} style={{ alignSelf: msg.sender === 'user' ? 'flex-end' : 'flex-start', maxWidth: '75%' }}>
            <div style={{ backgroundColor: msg.sender === 'user' ? '#007bff' : '#ffffff', color: msg.sender === 'user' ? '#ffffff' : '#333333', padding: '10px 16px', borderRadius: msg.sender === 'user' ? '16px 16px 0px 16px' : '16px 16px 16px 0px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)', fontSize: '14px', lineHeight: '1.5' }}>
              {msg.text}
            </div>
          </div>
        ))}
        {isLoading && (
          <div style={{ alignSelf: 'flex-start', color: '#777', fontSize: '13px', fontStyle: 'italic' }}>
            Analytics assistant is calculating data context...
          </div>
        )}
      </div>

      <form onSubmit={handleSendMessage} style={{ display: 'flex', gap: '10px' }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Query financial metrics, risk factors, corporate growth..."
          style={{ flexGrow: 1, padding: '12px 16px', borderRadius: '8px', border: '1px solid #ccc', fontSize: '14px', outline: 'none' }}
          disabled={isLoading}
        />
        <button type="submit" style={{ padding: '12px 24px', cursor: 'pointer', backgroundColor: '#28a745', color: '#fff', border: 'none', borderRadius: '8px', fontWeight: 'bold', fontSize: '14px' }} disabled={isLoading}>
          Send
        </button>
      </form>
    </div>
  );
}

export default App;