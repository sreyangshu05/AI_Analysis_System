"""
AI Analysis System Package
===========================
This package contains modules for the AI analysis system, including WebSocket client,
response processing, caching, and utilities.
"""

__version__ = "1.0.0"
__author__ = "Sreyangshu Sarkar"

# Expose common components for easier imports
from .websocket_client import WebSocketClient
from .response_processor import ResponseProcessor
from .cache import Cache
from .utils import validate_response

__all__ = [
    "WebSocketClient",
    "ResponseProcessor",
    "Cache",
    "validate_response",
]
