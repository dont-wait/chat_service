from fastapi.websockets import WebSocket

class WebSocketManager:
    def __init__(self):
        self.connected_clients = []
    
    async def connect(self, websocket: WebSocket):
        print(f"Client {websocket.client.host}: {websocket.client.port}")
        self.connected_clients.append(websocket)
        print(f"Client connected: {self.connected_clients}")

    async def send_message(self, websocket: WebSocket, message: str):
        message = {
            "client": f"Client {websocket.client.host}: {websocket.client.port}",
            "message": message
        }

        await websocket.send_json(message)

    async def disconnect(self, websocket: WebSocket):
        self.connected_clients.remove(websocket)
        print(f"Client {websocket.client.host}: {websocket.client.port} disconnected")
        print(f"Connected clients: {self.connected_clients}")