# OpenAI Agents SDK Streaming

## 📌 What is Streaming?

**Streaming** means:
✅ You don’t wait for the whole answer to be ready.
✅ You get small parts of the answer as they are being made.
✅ You can show them live to the user (like typing).

**Example**: Imagine you ask the agent to **tell a joke** — you see each word coming **one by one**, not waiting for the full joke.



## 📌 How does it work?
1️⃣ You use `Runner.run_streamed()` instead of `Runner.run()`.
 ➡️ This tells the agent: “Send me pieces of the answer as soon as you have them!”

2️⃣ You get a `RunResultStreaming` object.
 ➡️ This gives you a stream (like a pipeline).

3️⃣ You loop through **events** in that stream.
 ➡️ Each event is like: “Here’s a new piece of text!”



## 📌 What is a Raw Response Event?

- The LLM (Large Language Model) sends its answer in parts.
- These parts are called Raw Response Events.
- You put them together for the full answer.


## 📌 Code Example (Simple)
Let’s look at your example:


```
import asyncio
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner

async def main():
    agent = Agent(
        name="Joker",
        instructions="You are a helpful assistant.",
    )

    result = Runner.run_streamed(agent, input="Please tell me 5 jokes.")

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())

```




## 📌 Step by Step - What this does

### ✅ Step 1:
`Agent` is made.
- Its name is `"Joker"`
- Instructions: `"You are a helpful assistant."`


### ✅ Step 2:
`Runner.run_streamed()` runs the agent with input: `"Please tell me 5 jokes."`
- This starts the streaming.


### ✅ Step 3:
async for event in `result.stream_events()`:
- Loop through each piece (event).


### ✅ Step 4:
Check if it’s a Raw Response Event with `ResponseTextDeltaEvent`.


### ✅ Step 5:
Print the `delta` — the new text piece.


### ✅ Result:
You see the jokes **appearing live**, word by word.