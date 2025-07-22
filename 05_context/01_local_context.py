from agents import Agent,Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api  , function_tool ,RunContextWrapper
from dataclasses import dataclass
import os
from dotenv import load_dotenv
import asyncio



load_dotenv()

gemini_api_key = os.getenv("GOOGLE_API_KEY")
set_tracing_disabled(True)

set_default_openai_api("chat_completions")
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)



#! -------------------------------- data_class -------------------------------- #
@dataclass
class MyDataClass:
    name: str
    age: int


#! -------------------------------- function_tool -------------------------------- #
@function_tool
async def fetch_my_data(wrapper : RunContextWrapper[MyDataClass]) -> str :
    return f"Hello {wrapper.context.name}, you are {wrapper.context.age} years old."



#! -------------------------------- agent -------------------------------- #

async def main():
    my_data = MyDataClass(name="Shahzad", age=21)

    agent: Agent = Agent[MyDataClass](
        name="Assistant", 
        instructions="Use the `fetch_my_data` tool to get name and age.", 
        model="gemini-2.0-flash",
        tools = [fetch_my_data],
        
    )

    result = await Runner.run(
        starting_agent=agent,
        input="What is my name and age?",
        context=my_data
    )

    print("\nCALLING AGENT\n")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
    


