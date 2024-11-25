import pytest # type: ignore
from app.scoring import Scorer

def test_evaluate():
    scorer = Scorer()
    response = "AI is a subset of machine learning."
    score, feedback = scorer.evaluate(response)
    assert score > 0
    assert feedback == "Good response"
