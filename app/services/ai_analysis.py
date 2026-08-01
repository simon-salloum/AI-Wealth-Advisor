from app.models.client import Client
from app.services.openai_service import client


class AIAnalysisService:
    @staticmethod
    def analyze(client_data: Client) -> str:

        prompt = f"""
You are a Senior Private Banking Advisor.

Analyze this client.

Client

Name: {client_data.name}

Age: {client_data.age}

Annual Income: {client_data.annual_income}

Savings: {client_data.savings}

Monthly Expenses: {client_data.monthly_expenses}

Mortgage: {client_data.mortgage}

Investment Experience: {client_data.investment_experience.value}

Risk Tolerance: {client_data.risk_tolerance.value}

Investment Goal: {client_data.investment_goal.value}

Time Horizon: {client_data.time_horizon}

Generate the report using exactly these headings.

# Executive Summary

# Financial Strengths

# Potential Risks

# Discussion Topics

# Questions To Ask

# Suggested Next Steps

Do NOT recommend financial products.

Keep the report concise and professional.
"""

        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role": "system",
                    "content": ("You are an experienced Private Banking Advisor."),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.4,
        )

        return response.choices[0].message.content or "No analysis generated."
