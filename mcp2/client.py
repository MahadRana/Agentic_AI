from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "calc":{
                "command":"python3",
                "args":["/Users/mahadrana/Documents/Python/agentic_ai/mcp2/calc.py"],
                "transport":"stdio"
            },
            "internet":{
                "url": "http://localhost:8000/mcp",
                "transport":"http"
            }
        }
    )

    model = ChatAnthropic(model='claude-sonnet-4-6')
    tools = await client.get_tools()

    agent = create_agent(model, tools)

    res = await agent.ainvoke(
        {"messages":[{"role":"user", "content": "What is 3+5*2 and what is the tallest building in Saudi Arabia"}]}
    )

    print("Math response: ", res["messages"][-1].content)

asyncio.run(main())