# AI Analysis System

A WebSocket-based system for real-time scoring and feedback of student responses on AI concepts.

## Features
- **WebSocket Integration**: Real-time communication.
- **Response Scoring**: AI-related keyword analysis.
- **Caching**: Prevent duplicate evaluations.
- **Concurrency Support**: Handles multiple connections simultaneously.

## Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install websockets pydantic aiocache pytest pytest-asyncio fastapi uvicorn
   python run_server.py
3. Testing: [This will automatically discover all test files in the tests directory (files starting with test_) and execute them.]
   ```bash
   pytest tests/
4. Run a Specific Test:
   ```bash
   pytest tests/test_websocket_client.py
5. View the Test Output:
  -- After running the tests, pytest will display the test results, including:
  -- Passed tests: Indicated with a. 
  -- Failed tests: Indicated with an F and details of the failure.
  ```bash
  ================== test session starts ==================
  collected 12 items
  tests/test_cache.py ..                                   [ 16%]
  tests/test_response_processor.py ..                     [ 33%]
  tests/test_utils.py ..                                  [ 50%]
  tests/test_websocket_client.py ..                      [100%]
  ================== 12 passed in 0.55s ===================
6. Debugging Failing Tests:
-- Read the error message and traceback provided by pytest.
-- Open the corresponding test file and inspect the failing test function.
-- Fix any bugs in the implementation or test logic, and re-run the tests.
7. Run with Verbose Output:
```bash
pytest -v
================== test session starts ==================
collected 12 items

tests/test_cache.py::test_cache_set_and_get PASSED       [ 16%]
tests/test_cache.py::test_cache_expiry PASSED            [ 33%]
tests/test_cache.py::test_cache_cleanup PASSED           [ 50%]
...
================== 12 passed in 0.42s ===================
