import sys

from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()

from agent.tool_agent import graph

result = graph.invoke({
    'messages': [
        {
            'role': 'user',
            'content': ' Который сейчас час?'
        }
    ]
})

print(result['messages'][-1].content)