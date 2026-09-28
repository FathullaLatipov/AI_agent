from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from langchain_groq import ChatGroq

from tools.time import get_current_time

class State(TypedDict):
    messages: Annotated[list, add_messages]

llm = ChatGroq(
    model = 'openai/gpt-oss-120b',
    temperature = 0
)

tools = [get_current_time]

llm_with_tools = llm.bind_tools(tools)

def agent(state: State):
    response = llm_with_tools.invoke(
        state['messages']
    )

    return {
        'messages': [response]
    }

tool_node = ToolNode(tools)

def should_continue(state: State):

    last_message = state['messages'][-1]

    if last_message.tool_calls:
        return 'tools'

    return 'end'

builder = StateGraph(State)

builder.add_node('agent', agent)
builder.add_node('tools', tool_node)

builder.add_edge(START, 'agent')

builder.add_conditional_edges(
    'agent',
    should_continue,
    {
        'tools': 'tools',
        'end': END
    }
)

builder.add_edge('tools', 'agent')
graph = builder.compile()
