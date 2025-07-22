# 📌 Context Management (OpenAI Agents SDK)

**Context** means extra information that helps your agent or tools work better. There are **two kinds of context**:


### Type
1. Local Context
2. LLM Context


## ✅ 1️⃣ Local Context

**What is it?**
A Python object (often a dataclass) that stores information or helpers needed by tools.

**Where is it used?**
- In tools (@function_tool)
- In lifecycle hooks
- Used for the entire agent run


### ✔️ Example

```
from dataclasses import dataclass

@dataclass
class UserInfo:
    name: str
    uid: int

```

```
user_info = UserInfo(name="John", uid=123)
```

Pass it to the agent run:

```
result = await Runner.run(
    starting_agent=agent,
    input="question here",
    context=user_info  # 👈 Local context!
)
```

Use it in a tool:

```
@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:
    return f"The user {wrapper.context.name} is 47 years old"

```

**Key point:**
- Local context is not sent to the LLM.
- It’s for your Python code only.



## ✅ 2️⃣ LLM Context

**What is it?**
Info that the LLM can “see” while generating a reply.

**How to share it with the AI?**

| Method                           | Description                                              |
| ---------------------------------|:--------------------------------------------------------:|
| System Prompt / Instructions     | Add info to `instructions` (like a system message).      |
| Include in Input                 | Add info directly in the input text.                     |
| Function Tools                   | AI calls a tool to get info on demand.                   |


### ✔️ System Prompt Example
```
agent = Agent(
    name="Assistant",
    instructions="You are helpful and the user's name is John."
)
```

### ✔️ Input Example
```
result = await Runner.run(
    starting_agent=agent,
    input="The user John asks: What is my age?"
)
```

### ✔️ Function Tool Example
```
@function_tool
async def get_username(wrapper: RunContextWrapper[UserInfo]) -> str:
    return f"User {wrapper.context.name}"
```

## ✅ 3️⃣ Key Differences

| Local Context                          | LLM Context                                              |
| ------------------------------------|:------------------------------------:|
| Private to your code                | Visible to the AI                      |
| Not sent anywhere                   | Sent to the AI in the conversation     |
| Same type for whole run             | Flexible per message                   |
| Useful for helpers & dependencies   | Useful for guiding the AI              |


### 📌 Final Example: Both Together

- ``UserInfo`` = ``name="John"``

- The AI doesn’t know the name yet

- You provide a tool ``get_username``

- When the AI needs the name, it calls ``get_username``

- Your Python code returns ``"John"`` — the AI uses it



