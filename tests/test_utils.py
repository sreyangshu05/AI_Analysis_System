from app.utils import validate_response

def test_valid_response():
    response = "This is a valid response."
    assert validate_response(response) is True

def test_invalid_response():
    response = "   "  # Empty or whitespace-only
    assert validate_response(response) is False
