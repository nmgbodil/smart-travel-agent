from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama

from tools import weather_tool

import asyncio

llm = ChatOllama(model="mistral", temperature=0)
system_prompt = '''You are a smart travel assistant that helps users plan short trips given the users intended destination and travel dates
by providing recommendations for activities to do each day in the city depending on
the weather that day, calculating travel cost estimates and summarizing all into a final
trip suggestion. Based on feedback from the user you update the travel plans to match
their feedback and you constantly save the plans in a markdown with a suitable name.
'''

# def get_weather(city: str) -> str:
#     '''Get weather for a given city.'''
#     return f"It is currently sunny in {city}"

async def main_agent():
    messages = [{"role": "system", "content": system_prompt}]

    agent = create_react_agent(
        model=llm,
        tools=[weather_tool.get_weather]
    )

    print("================================= Smart Travel Agent =================================")
    print("Enter quit or exit to end the chat")
    print("\nTravel Assistant: Hello, I am your smart travel assistant. How can I help you?")

    while True:
        user_input = input('\nYou: ')

        if user_input.lower() == "quit" or user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})
        responses = await agent.ainvoke({"messages": messages})
        ai_response = responses['messages'][-1].content
        print(f'\nTravel Assistant: {ai_response}')
        messages.append({"role": "assistant", "content": ai_response})


    print("================================= Smart Travel Agent =================================")

if __name__ == "__main__":
    asyncio.run(main_agent())