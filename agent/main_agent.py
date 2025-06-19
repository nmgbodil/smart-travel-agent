from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama

from tools import weather_tool

import asyncio

llm = ChatOllama(model="mistral", temperature=0)
system_prompt = '''You are a smart travel assistant that helps users plan short trips given the users intended destination and travel dates.
You do this by retrieving all the required information then providing recommendations for activities to do on each day in the city depending on
the weather that day, calculating travel cost estimates and summarizing all into a final
trip suggestion. Based on feedback from the user you update the travel plans to match
their feedback and you constantly save the plans in a markdown with a suitable name.
'''

messages = [{"role": "system", "content": system_prompt}]
end_chat_flag = False

def get_user_response() -> str:
    '''This function prompts the user for input then returns it as a string'''
    global end_chat_flag
    user_input = input("\nYou: ")
    messages.append({"role": "user", "content": user_input})
    end_chat_flag = True
    return user_input

async def main_agent():

    global end_chat_flag

    agent = create_react_agent(
        model=llm,
        tools=[get_user_response, weather_tool.get_weather]
    )

    print("================================= Smart Travel Agent =================================")
    print("Enter quit or exit to end the chat")
    print("\nTravel Assistant: Hello, I am your smart travel assistant. How can I help you?")

    user_input = input("\nYou: ")
    while not end_chat_flag:

        if user_input.lower() == "quit" or user_input.lower() == "exit":
            end_chat_flag = True
            continue

        messages.append({"role": "user", "content": user_input})
        responses = await agent.ainvoke({"messages": messages})
        ai_response = responses['messages'][-1].content
        print(f'\nTravel Assistant: {ai_response}')
        messages.append({"role": "assistant", "content": ai_response})
        user_input = input("\nYou: ")


    print("================================= Smart Travel Agent =================================")

if __name__ == "__main__":
    asyncio.run(main_agent())