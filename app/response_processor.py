from app.scoring import Scorer
from app.cache import Cache

class ResponseProcessor:
    def __init__(self):
        self.scorer = Scorer()
        self.cache = Cache()

    async def process_response(self, student_id, response):
        if not response.strip():
            return {"error": "Invalid response"}

        # Check cached result
        cached_result = self.cache.get(student_id)
        if cached_result:
            return cached_result

        # Evaluate response
        score, feedback = self.scorer.evaluate(response)
        result = {"score": score, "feedback": feedback}

        # Cache the result
        self.cache.set(student_id, result)
        return result
