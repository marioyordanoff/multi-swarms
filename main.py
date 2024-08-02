import os

from dotenv import load_dotenv
from swarms import Agent, AgentRearrange, OpenAIChat

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


cash_flow_analyzer = Agent(
    agent_name="Cash Flow Analyzer",
    system_prompt="You analyze the cash flow of the company, ensuring that all revenue and expenses are accounted for accurately.",
    agent_description="Analyze the company's cash flow.",
    llm=OpenAIChat(),
    max_loops=1,
    autosave=True,
    dynamic_temperature_enabled=True,
    dashboard=False,
    verbose=True,
    streaming_on=True,
    tools=[calculate_profit],
)

expenses_analyst = Agent(
    agent_name="Expenses Analyst Agent",
    system_prompt="You are responsible for analyzing the company's expenses to ensure they are categorized correctly and identify any discrepancies.",
    agent_description="Analyze and categorize the company's expenses.",
    llm=OpenAIChat(),
    max_loops=1,
    autosave=True,
    dynamic_temperature_enabled=True,
    dashboard=False,
    verbose=True,
    streaming_on=True,
    tools=[calculate_profit],
)
report_generator = Agent(
    agent_name="Report Generator",
    system_prompt="You generate a comprehensive financial report based on the analyzed data from other agents.",
    agent_description="Generate a comprehensive financial report.",
    llm=OpenAIChat(),
    max_loops=1,
    autosave=True,
    dynamic_temperature_enabled=True,
    dashboard=False,
    verbose=True,
    streaming_on=True,
    tools=[generate_report],
)
# Create a list of agents
agents = [cash_flow_analyzer, expenses_analyst, report_generator]

# Define the flow pattern
flow = "Cash Flow Analyzer -> Expenses Analyst Agent -> Report Generator"

# Using AgentRearrange class
agent_system = AgentRearrange(agents=agents, flow=flow)
output = agent_system.run(
    "Analyze the financial health of the startup and generate a report."
)

print(output)
