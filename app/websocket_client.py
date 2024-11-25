import asyncio
import websockets # type: ignore
from config import Config

class WebSocketClient:
    def __init__(self, uri=Config.WEBSOCKET_URL):
        self.uri = uri
        self.connection = None

    async def connect(self):
        try:
            self.connection = await websockets.connect(self.uri)
        except Exception as e:
            raise ConnectionError(f"Failed to connect: {e}")

    async def send(self, data):
        if self.connection is None:
            raise ConnectionError("WebSocket connection not established.")
        await self.connection.send(data)

    async def receive(self):
        if self.connection is None:
            raise ConnectionError("WebSocket connection not established.")
        return await self.connection.recv()

    async def close(self):
        if self.connection:
            await self.connection.close()
