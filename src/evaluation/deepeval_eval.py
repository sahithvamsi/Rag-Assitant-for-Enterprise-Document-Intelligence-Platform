from deepeval.metrics import (
    AnswerRelevancyMetric
)

from deepeval.test_case import (
    LLMTestCase
)


class DeepEvalEvaluator:

    @staticmethod
    def evaluate_answer(
        question,
        answer
    ):

        metric = AnswerRelevancyMetric(
            threshold=0.7
        )

        test_case = LLMTestCase(
            input=question,
            actual_output=answer
        )

        metric.measure(
            test_case
        )

        return {
            "score": metric.score,
            "passed": metric.success
        }