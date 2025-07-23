from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

gemini_api_key = os.getenv("GOOGLE_API_KEY")
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_default_openai_client(external_client)

#? ===================== Handoffs Example =====================

#! ---------------------------------- Agent_1 --------------------------------- #
urdu_agent = Agent(
    name="Urdu Assistant",
    instructions="You are a helpful assistant that user input to convert to  responds in Urdu.",
    model="gemini-2.0-flash",
    handoff_description="Translate the user input to Urdu and respond accordingly.",
)
#! ---------------------------------- Agent_2 --------------------------------- #
english_agent = Agent(
    name="English Assistant",
    instructions="You are a helpful assistant that user input to convert to  responds in English.",
    model="gemini-2.0-flash",
)
#! ---------------------------------- Agent_3 --------------------------------- #
arabic_agent = Agent(
    name="Arabic Assistant",
    instructions="You are a helpful assistant that user input to convert to  responds in Arabic.",
    model="gemini-2.0-flash",
)
#! ---------------------------------- Agent_4 --------------------------------- #
french_agent = Agent(
    name="French Assistant",
    instructions="You are a helpful assistant that user input to convert to  responds in French.",
    model="gemini-2.0-flash",
)
#! ---------------------------------- Agent_5 --------------------------------- #
spanish_agent = Agent(
    name="Spanish Assistant",
    instructions="You are a helpful assistant that user input to convert to  responds in Spanish.",
    model="gemini-2.0-flash",
)
#! ---------------------------------- Agent_6 --------------------------------- #
german_agent = Agent(
    name="German Assistant",
    instructions="You are a helpful assistant that user input to convert to  responds in German.",
    model="gemini-2.0-flash",
)
#! ---------------------------------- Agent_7 --------------------------------- #
japanese_agent = Agent(
    name="Japanese Assistant",
    instructions="You are a helpful assistant that user input to convert to  responds in Japanese.",
    model="gemini-2.0-flash",
)
#! ---------------------------------- Agent_8 --------------------------------- #
korean_agent = Agent(
    name="Korean Assistant",
    instructions="You are a helpful assistant that user input to convert to  responds in Korean.",
    model="gemini-2.0-flash",
)
#! ---------------------------------- Agent_9 --------------------------------- #
italian_agent = Agent(
    name="Italian Assistant",
    instructions="You are a helpful assistant that user input to convert to  responds in Italian.",
    model="gemini-2.0-flash",
)
#! ---------------------------------- Agent_10 --------------------------------- #
portuguese_agent = Agent(
    name="Portuguese Assistant",
    instructions="You are a helpful assistant that user input to convert to  responds in Portuguese.",
    model="gemini-2.0-flash",
)



#! ----------------------------------- Main Agent ---------------------------------- #

agent: Agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant that can handle multiple languages and handoffs.", 
    model="gemini-2.0-flash",
    handoffs=[
        urdu_agent,
        english_agent,
        arabic_agent,
        french_agent,
        spanish_agent,
        german_agent,
        japanese_agent,
        korean_agent,
        italian_agent,
        portuguese_agent,
        
        
    ]
)

result = Runner.run_sync(
    agent,
    "Hello, how are you? I would like to know the weather in Paris translate to Urdu.",
)


print("Starting handoff process...")
# print("Starting with agent:", result.)
print("Final output agent",result.final_output)
print("🤖",result.last_agent)
