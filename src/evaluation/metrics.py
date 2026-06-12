from dataclasses import dataclass
from typing import Dict


@dataclass
class EvaluationResult:
    faithfulness: float
    answer_relevancy: float
    context_precision: float
    context_recall: float


class MetricsReporter:

    @staticmethod
    def to_dict(
        result: EvaluationResult
    ) -> Dict:

        return {
            "faithfulness": result.faithfulness,
            "answer_relevancy": result.answer_relevancy,
            "context_precision": result.context_precision,
            "context_recall": result.context_recall
        }

    @staticmethod
    def print_report(
        result: EvaluationResult
    ):

        print("\n===== Evaluation Report =====")

        print(
            f"Faithfulness: {result.faithfulness:.3f}"
        )

        print(
            f"Answer Relevancy: {result.answer_relevancy:.3f}"
        )

        print(
            f"Context Precision: {result.context_precision:.3f}"
        )

        print(
            f"Context Recall: {result.context_recall:.3f}"
        )

        print("=============================\n")