from app.models.financial_context import FinancialContext
from app.models.risk_assessment import RiskAssessment
from app.services.openai_service import client


class AdvisorCopilot:
    @staticmethod
    def ask(
        context: FinancialContext,
        risk: RiskAssessment,
        question: str,
    ) -> str:

        prompt = f"""
You are an experienced Private Banking Advisor.

Use the information below to answer the advisor's question.

CLIENT

Name: {context.client.name}
Age: {context.client.age}

Annual Income: {context.client.annual_income:,.0f} SEK
Savings: {context.client.savings:,.0f} SEK
Mortgage: {context.client.mortgage:,.0f} SEK

Investment Experience:
{context.client.investment_experience.value}

Risk Tolerance:
{context.client.risk_tolerance.value}

Investment Goal:
{context.client.investment_goal.value}

Time Horizon:
{context.client.time_horizon}

FINANCIAL METRICS

Financial Score:
{context.score}

Rating:
{context.rating}

Monthly Surplus:
{context.monthly_surplus:,.0f}

Savings Ratio:
{context.savings_ratio}

Debt Ratio:
{context.debt_ratio}

Savings Rate:
{context.savings_rate} %

RISK ASSESSMENT

Liquidity:
{risk.liquidity}

Debt:
{risk.debt}

Savings:
{risk.savings}

Cash Flow:
{risk.cash_flow}

Retirement:
{risk.retirement}

Overall:
{risk.overall}

Advisor Question

{question}

Answer professionally.

Never recommend specific investment products.

Keep the answer concise.
"""

        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role": "system",
                    "content": ("You are a Senior Private Banking Advisor."),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.3,
        )

        return response.choices[0].message.content or "No response generated."
