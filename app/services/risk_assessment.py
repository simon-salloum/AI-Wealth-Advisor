from app.models.financial_context import FinancialContext
from app.models.risk_assessment import RiskAssessment


class RiskAssessmentService:
    @staticmethod
    def analyze(
        context: FinancialContext,
    ) -> RiskAssessment:

        if context.debt_ratio < 2:
            debt = "Low"

        elif context.debt_ratio < 4:
            debt = "Moderate"

        else:
            debt = "High"

        if context.savings_ratio > 2:
            savings = "Strong"

        elif context.savings_ratio > 1:
            savings = "Healthy"

        else:
            savings = "Weak"

        if context.monthly_surplus > 30000:
            cash_flow = "Strong"

        elif context.monthly_surplus > 10000:
            cash_flow = "Healthy"

        else:
            cash_flow = "Weak"

        if context.monthly_surplus > 0:
            liquidity = "Good"
        else:
            liquidity = "Poor"

        if context.client.time_horizon >= 15 and context.score >= 80:
            retirement = "On Track"

        else:
            retirement = "Needs Review"

        if context.score >= 90:
            overall = "Excellent"

        elif context.score >= 75:
            overall = "Good"

        elif context.score >= 60:
            overall = "Average"

        else:
            overall = "High Risk"

        return RiskAssessment(
            liquidity=liquidity,
            debt=debt,
            savings=savings,
            retirement=retirement,
            cash_flow=cash_flow,
            overall=overall,
        )
