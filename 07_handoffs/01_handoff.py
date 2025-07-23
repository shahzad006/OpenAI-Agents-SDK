from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api , ModelSettings, RunConfig
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_default_openai_client(external_client)

config = RunConfig(
  model_settings=ModelSettings(
       temperature=0.5,
        max_tokens=150,
        top_p=0.9,
  )
)


#? ===================== Handoffs Example =====================
#! ---------------------------------- Agent_1 --------------------------------- #

english_teacher_agent = Agent(
    name="English Teacher",
    instructions = "You are help full Assistant. and you are a teacher of english language. You will help user to learn english language.",
    model="gemini-2.0-flash",
    handoff_description = "You are english Expert language Teacher.",
    
)

#! ---------------------------------- Agent_2 --------------------------------- #

math_teacher_agent = Agent(
    name="Math Teacher",
    instructions = "You are help full Assistant. and you are a teacher of math. You will help user to learn math. and solve math problems.",
    model="gemini-2.0-flash",
    handoff_description = "You are math Expert Teacher.",
)


#! ---------------------------------- Agent_3 --------------------------------- #

history_teacher_agent = Agent(
    name="History Teacher",
    instructions = "You are help full Assistant. and you are a teacher of history. You will help user to learn history.",
    model="gemini-2.0-flash",
    handoff_description = "You are history Expert Teacher.",
)
  


#! ---------------------------------- Main Agent --------------------------------- #

main_agent = Agent(
    name="Main Teacher",
    instructions="You are a helpful assistant that can handoff to other agents based on the subject.",
    model="gemini-2.0-flash",
    handoffs=[english_teacher_agent, math_teacher_agent, history_teacher_agent],
 

)

user_input = str(input("Enter your question: "))

result = Runner.run_sync(
    starting_agent=main_agent,
    input=user_input,
    run_config = config
    

)

print("Final Output:", result.final_output)
print("🤖",result.last_agent)