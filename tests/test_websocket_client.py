import pytest # type: ignore
import asyncio
from app.websocket_client import WebSocketClient

@pytest.mark.asyncio
async def test_websocket_connect():
    client = WebSocketClient(uri="ws://echo.websocket.org")
    await client.connect()
    assert client.connection.open
    await client.close()

@pytest.mark.asyncio
async def test_websocket_send_receive():
    client = WebSocketClient(uri="ws://echo.websocket.org")
    await client.connect()
    test_message = "Hello, WebSocket!"
    await client.send(test_message)
    received_message = await client.receive()
    assert received_message == test_message
    await client.close()

@pytest.mark.asyncio
async def test_websocket_close():
    client = WebSocketClient(uri="ws://echo.websocket.org")
    await client.connect()
    await client.close()
    assert client.connection.closed
