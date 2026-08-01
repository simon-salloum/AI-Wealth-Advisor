from app.models.client import Client
from app.models.financial_context import FinancialContext


class FinancialAnalysisService:
    @staticmethod
    def analyze(client: Client) -> FinancialContext:

        monthly_income = client.annual_income / 12

        monthly_surplus = monthly_income - client.monthly_expenses

        savings_ratio = client.savings / client.annual_income

        debt_ratio = client.mortgage / client.annual_income

        savings_rate = monthly_surplus / monthly_income

        score = 100

        if debt_ratio > 5:
            score -= 25
        elif debt_ratio > 3:
            score -= 15
        elif debt_ratio > 2:
            score -= 5

        if savings_ratio < 0.5:
            score -= 20
        elif savings_ratio < 1:
            score -= 10

        if savings_rate < 0:
            score -= 25
        elif savings_rate < 0.20:
            score -= 10

        score = max(score, 0)

        if score >= 90:
            rating = "Excellent"
        elif score >= 75:
            rating = "Good"
        elif score >= 60:
            rating = "Average"
        else:
            rating = "Needs Attention"

        return FinancialContext(
            client=client,
            score=score,
            rating=rating,
            monthly_income=round(monthly_income),
            monthly_surplus=round(monthly_surplus),
            savings_ratio=round(savings_ratio, 2),
            debt_ratio=round(debt_ratio, 2),
            savings_rate=round(
                savings_rate * 100,
                1,
            ),
        )
