import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from agents.run import RunConfig

# Load the environment variables from the .env file
load_dotenv()

set_tracing_disabled(True)

gemini_api_key = os.getenv("GOOGLE_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
) 




agent = Agent (
    name = "Assistant", 
    instructions = "You are a helpful assistant. You can cell tools to get information.",
    model = model,
    
    
)

user_input = str(input("Enter your Query: "))

result = Runner.run_sync(agent, user_input,run_config= config) 

print("\nCALLING AGENT\n")
print(result.final_output)