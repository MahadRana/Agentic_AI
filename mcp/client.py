from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command": "python3",
                "args":["/Users/mahadrana/Documents/Python/agentic_ai/mcp/mathserver.py"],
                "transport":"stdio"
            },
            "weather":{
                "url": "http://localhost:8000/mcp",
                "transport":"http"
            }
        }
    )

    model = ChatAnthropic(model='claude-sonnet-4-6')
    tools = await client.get_tools()
    
    agent = create_agent(model, tools)

    math_response = await agent.ainvoke(
        {"messages":[{"role":"user", "content": "what is the weather in London and what is 3+5x4"}]}
    )
    print("Math response: ", math_response["messages"][-1].content)

asyncio.run(main())