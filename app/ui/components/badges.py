from rich.text import Text


class Badges:
    @staticmethod
    def score(score: int) -> Text:

        if score >= 90:
            return Text(
                f"🟢 {score}/100",
                style="success",
            )

        if score >= 75:
            return Text(
                f"🟡 {score}/100",
                style="warning",
            )

        return Text(
            f"🔴 {score}/100",
            style="danger",
        )

    @staticmethod
    def risk(level: str) -> Text:

        level = level.lower()

        if level == "low":
            return Text(
                "🟢 Low",
                style="success",
            )

        if level == "medium":
            return Text(
                "🟡 Medium",
                style="warning",
            )

        return Text(
            "🔴 High",
            style="danger",
        )

    @staticmethod
    def rating(rating: str) -> Text:

        mapping = {
            "Excellent": ("🟢 Excellent", "success"),
            "Good": ("🟡 Good", "warning"),
            "Average": ("🟠 Average", "warning"),
            "Needs Attention": ("🔴 Needs Attention", "danger"),
        }

        text, style = mapping.get(
            rating,
            (rating, "value"),
        )

        return Text(
            text,
            style=style,
        )
