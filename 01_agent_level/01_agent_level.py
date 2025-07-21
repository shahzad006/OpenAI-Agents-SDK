from agents import Agent , Runner , OpenAIChatCompletionsModel , AsyncOpenAI , set_tracing_disabled 
import os 
from dotenv import load_dotenv



load_dotenv()


gemini_api_key = os.getenv("GOOGLE_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")



client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(disabled=True)


    # This agent will use the custom LLM provider
agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    )

result = Runner.run_sync(
        agent,
        "Tell me about recursion in programming.",
    )

print("\nCALLING AGENT\n")
print(result.final_output)






# print("\nCALLING AGENT\n")
# print(result.final_output)