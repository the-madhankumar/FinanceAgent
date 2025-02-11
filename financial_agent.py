from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

model_id = "deepseek-r1-distill-llama-70b"
# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search for information on the web",
    tools=[DuckDuckGo()],
    model=Groq(id=model_id),
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

# Financial Agent
finance_agent = Agent(
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    model=Groq(id=model_id),
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Use tables to display the data"],
    show_tools_calls=True,
    markdown=True
)

multi_ai_agent=Agent(
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources","Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
    model=Groq(id=model_id)
)

multi_ai_agent.print_response("Summarise analyst recommendation and share the latest news for NVDA",stream=True)