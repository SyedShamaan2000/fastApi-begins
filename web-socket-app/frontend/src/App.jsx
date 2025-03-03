// Import necessary React hooks
import { useState, useEffect } from "react";

function App() {
  // State variables
  const [socket, setSocket] = useState(null); // WebSocket connection object
  const [messages, setMessages] = useState([]); // Array to store chat messages
  const [input, setInput] = useState(""); // Input field state

  // useEffect for initial WebSocket connection setup
  useEffect(() => {
    // Create new WebSocket connection to local server
    const ws = new WebSocket("ws://localhost:8000/ws");

    // Event handler for incoming messages
    ws.onmessage = (event) => {
      // Add received message to state with 'AI' sender tag
      setMessages((prev) => [...prev, { sender: "AI", text: event.data }]);
    };

    // Save WebSocket instance to state
    setSocket(ws);

    // Cleanup function to close connection when component unmounts
    return () => ws.close();
  }, []); // Empty dependency array ensures this runs only once on mount

  // Function to handle message sending
  const sendMessage = () => {
    if (socket && input) {
      // Send message through WebSocket
      socket.send(input);
      // Add user's message to state with 'User' sender tag
      setMessages((prev) => [...prev, { sender: "User", text: input }]);
      // Clear input field
      setInput("");
    }
  };

  // Component rendering
  return (
    <>
      <div className="main-container">
        <div className="chat-container">
          {/* Chat messages display area */}
          <div className="chat">
            {messages.map((message, index) => (
              <div
                key={index}
                className={`message ${
                  message.sender === "AI" ? "left" : "right"
                }`}
              >
                {/* Message content bubble */}
                <div className="message-content">{message.text}</div>
                {/* Sender label */}
                <div className="message-sender">{message.sender}</div>
              </div>
            ))}
          </div>

          {/* Message input section */}
          <div className="input-container">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)} // Update input state
              onKeyPress={(e) => e.key === "Enter" && sendMessage()} // Send on Enter
              placeholder="Type your message..."
            />
            <button onClick={sendMessage}>Send</button>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
