from app.models.client import Client
from app.services.openai_service import client


class MeetingPreparationService:
    @staticmethod
    def prepare(client_data: Client) -> str:
        prompt = f"""
You are a Senior Private Banking Advisor.

Prepare for an upcoming client meeting.

Client Information

Name: {client_data.name}
Age: {client_data.age}
Annual Income: {client_data.annual_income:,.0f} SEK
Savings: {client_data.savings:,.0f} SEK
Monthly Expenses: {client_data.monthly_expenses:,.0f} SEK
Mortgage: {client_data.mortgage:,.0f} SEK
Investment Experience: {client_data.investment_experience.value}
Risk Tolerance: {client_data.risk_tolerance.value}
Investment Goal: {client_data.investment_goal.value}
Time Horizon: {client_data.time_horizon} years

Generate the preparation using these sections.

# Meeting Objective

# Suggested Agenda

# Important Questions

# Potential Risks

# Recommended Follow-up

Keep the response concise and professional.

Do not recommend specific investment products.
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

        return response.choices[0].message.content or (
            "No meeting preparation generated."
        )
