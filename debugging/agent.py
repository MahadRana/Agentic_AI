from typing import Annotated
from typing_extensions import TypedDict
import os
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from IPython.display import Image, display
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import BaseMessage
from langchain_core.tools import tool

load_dotenv()

os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = "Test_Project"

llm = ChatAnthropic(model='claude-sonnet-4-6')
llm

class State(TypedDict):
    messages:Annotated[list[BaseMessage], add_messages]

def make_tool_graph():
    @tool
    def add(a:float, b:float) -> float:
        """Add 2 Numbers"""
        return a + b

    tool_node = ToolNode([add])

    llm_w_tools = llm.bind_tools([add])


    def call_llm_model(state:State):
        return {"messages":[llm_w_tools.invoke(state["messages"])]}    
    
    builder = StateGraph(State)
    builder.add_node("llm_w_tools", call_llm_model)
    builder.add_node("tools", tool_node)

    builder.add_edge(START, "llm_w_tools")
    builder.add_conditional_edges("llm_w_tools", tools_condition)
    builder.add_edge("tools", "llm_w_tools")
    builder.add_edge("llm_w_tools", END)
    
    graph = builder.compile()

    try:
        display(Image(graph.get_graph().draw_mermaid_png()))
    except Exception:
        print("issue")
    return graph

tool_agent = make_tool_graph()


