from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api
import os
from dotenv import load_dotenv
import asyncio
from openai.types.responses import ResponseTextDeltaEvent

load_dotenv()

gemini_api_key = os.getenv("GOOGLE_API_KEY")
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_default_openai_client(external_client)


agent: Agent = Agent(
        name="Assistant", 
        instructions="You are a helpful assistant", 
        model="gemini-2.0-flash"
    )


async def main():
    

    result =Runner.run_streamed(
        agent,
        "Hi Write a short story about a cat who learns to code."
    )

   
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta , end="", flush=True)

        


asyncio.run(main())