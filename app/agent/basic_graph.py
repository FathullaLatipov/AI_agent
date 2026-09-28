from typing_extensions  import TypedDict
from typing import Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# STATE
class State(TypedDict):
    messages: Annotated[list, add_messages]

# NODE
def greeting(state: State):
    return {
        "name": f"Привет!, {state['name']}! Это мой первый LangGraph"
    }

# END
builder = StateGraph(State)

builder.add_node('hello world', greeting)

builder.add_edge(START, 'hello world')
builder.add_edge('hello world', END)

graph = builder.compile()

result = graph.invoke({
    'name': "Fathullaxon"
})

# @tool
# def get_current_time():
#     pass

print(result)