class Critic:

    @staticmethod
    def check_empty_context(
        chunks
    ):

        return len(chunks) > 0

    @staticmethod
    def check_citations(
        answer
    ):

        citation_patterns = [
            "[1]",
            "[2]",
            "[3]",
            "[4]",
            "[5]"
        ]

        return any(
            c in answer
            for c in citation_patterns
        )

    @staticmethod
    def review(
        answer,
        chunks
    ):

        issues = []

        if not Critic.check_empty_context(
            chunks
        ):
            issues.append(
                "No supporting context found."
            )

        if not Critic.check_citations(
            answer
        ):
            issues.append(
                "Missing citations."
            )

        return {
            "passed": len(issues) == 0,
            "issues": issues
        }