from dataclasses import dataclass

from app.models.financial_context import FinancialContext
from app.models.risk_assessment import RiskAssessment


@dataclass
class AdvisorContext:
    financial: FinancialContext
    risk: RiskAssessment

    recommendations: list[str]

    warnings: list[str]

    discussion_topics: list[str]
