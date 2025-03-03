# Import required modules from FastAPI
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

# Create a FastAPI application instance
app = FastAPI()

# Configure CORS (Cross-Origin Resource Sharing) middleware
# This allows cross-origin requests from any origin (*) for development purposes
# In production, you should specify allowed origins instead of using "*"
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"]  # Allow all headers
)

# Root endpoint for basic health check
@app.get("/")
async def welcome_note():
    return {"message": "Welcome to the Websocket Server"}

# WebSocket endpoint definition
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Accept the WebSocket connection request
    await websocket.accept()
    
    # Maintain persistent connection using infinite loop
    while True:
        try:
            # Wait for and receive text message from client
            data = await websocket.receive_text()
            
            # Process the received data (simple reversal example)
            # In a real application, this could be replaced with AI model inference
            # or other business logic
            response = f"AI Response: {data[::-1]}"
            
            # Send processed response back to client
            await websocket.send_text(response)
            
        except Exception as e:
            # Basic error handling - close connection on exception
            print(f"Error: {e}")
            await websocket.close()
            break