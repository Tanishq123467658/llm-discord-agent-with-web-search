from dotenv import load_dotenv
import os
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.tools import tool
from tavily import TavilyClient

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def surfInternet(query:str):
    """Use this tool to surf the Internet and get the Latest Information"""

    response = client.search(query=query)

    return str(response)



model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

agent = create_agent(model=model,tools=[surfInternet],system_prompt="Give clean output to the user")

