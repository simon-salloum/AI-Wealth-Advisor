from app.models.advisor_context import AdvisorContext


class RecommendationEngine:
    @staticmethod
    def build(
        context: AdvisorContext,
    ) -> AdvisorContext:

        recommendations = []
        warnings = []
        discussion_topics = []

        if context.financial.score >= 90:
            recommendations.append("Client has an excellent financial position.")

        if context.risk.debt == "High":
            warnings.append("High debt exposure.")

            discussion_topics.append("Debt management")

        if context.risk.retirement == "Needs Review":
            discussion_topics.append("Retirement planning")

        if context.risk.cash_flow == "Weak":
            discussion_topics.append("Monthly cash flow")

        context.recommendations = recommendations
        context.warnings = warnings
        context.discussion_topics = discussion_topics

        return context
