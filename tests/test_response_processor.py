import pytest # type: ignore
import asyncio
from app.response_processor import ResponseProcessor

@pytest.mark.asyncio
async def test_valid_response_processing():
    processor = ResponseProcessor()
    student_id = "student123"
    response = "AI and machine learning are related fields."
    result = await processor.process_response(student_id, response)
    assert result["score"] > 0
    assert "feedback" in result

@pytest.mark.asyncio
async def test_invalid_response_processing():
    processor = ResponseProcessor()
    student_id = "student123"
    response = "   "  # Empty/invalid response
    result = await processor.process_response(student_id, response)
    assert "error" in result

@pytest.mark.asyncio
async def test_cached_response():
    processor = ResponseProcessor()
    student_id = "student123"
    response = "AI and machine learning are related fields."
    await processor.process_response(student_id, response)
    cached_result = await processor.process_response(student_id, response)
    assert "score" in cached_result
    assert "feedback" in cached_result
