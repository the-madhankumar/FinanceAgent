from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
import phi.api
import phi
from phi.playground import Playground, serve_playground_app
from phi.model.groq import Groq


load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

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

app=Playground(agents=[finance_agent,web_search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)