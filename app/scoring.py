class Scorer:
    def evaluate(self, response):
        keywords = ["AI", "machine learning", "neural network", "dataset"]
        score = sum(word in response.lower() for word in keywords)
        feedback = "Good response" if score > 2 else "Needs improvement"
        return score, feedback
