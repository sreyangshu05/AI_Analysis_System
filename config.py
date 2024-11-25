import os

class Config:
    WEBSOCKET_URL = os.getenv("WEBSOCKET_URL", "ws://localhost:8000")
    CACHE_EXPIRY = 3600  # 1 hour
    MAX_CONNECTIONS = 10
