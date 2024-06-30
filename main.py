from swarms import Agent, OpenAIChat
from dotenv import load_dotenv
import os
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")



def calculate_profit(revenue: float, expenses: float) -> float:
    """
    Calculate the profit from the revenue and expenses.
    Args:
        revenue (float): The revenue from the sales.
        expenses (float): The expenses from the sales.
    Returns:
        float: The profit from the revenue and expenses.
    """
    return revenue - expenses

def generate_report(company_name: str, profit: float) -> str:
    """
    Generates a report for a company's profit.
    Args:
        company_name (str): The name of the company.
        profit (float): The calculated profit.
    Returns:
        str: The report for the company's profit.
    """
    return f"The profit for {company_name} is ${profit}."


agent = Agent(
    agent_name="Accounting Assistant",
    system_prompt="You are the accounting agent. Your purpose is to generate a profit report for a company based on given revenue and expenses.",
    agent_description="Generate a profit report for a company!",
    llm=OpenAIChat(),
    max_loops=1,
    autosave=True,
    dynamic_temperature_enabled=True,
    dashboard=False,
    verbose=True,
    streaming_on=True,
    tools=[calculate_profit, generate_report],

)

agent.run(
        "We're the Swarm Corporation, our total revenue is $100,000 and our total expenses are $50,000."
    )