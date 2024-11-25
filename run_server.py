import asyncio
from app.websocket_client import WebSocketClient
from app.response_processor import ResponseProcessor

async def main():
    client = WebSocketClient()
    processor = ResponseProcessor()
    await client.connect()

    try:
        while True:
            message = await client.receive()
            student_id, response = message.split(":")
            feedback = await processor.process_response(student_id, response)
            await client.send(str(feedback))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())
