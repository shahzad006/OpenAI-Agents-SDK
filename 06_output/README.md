## 📌 1️⃣ Normal output = plain text

When you use an **Agent**, it normally talks back in **simple sentences** — like a chat message.

**Example**:
```
""The meeting is called Team Sync, it’s on Friday, and Alice and Bob will join."
"
```
This is just **text** — you can read it, but your code can’t easily pick out each piece.


## 📌 **2️⃣ But sometimes you want the AI to give you organized data

**👉 Example**:
You don’t want one long line.
You want:
- 📌 The name of the event
- 🗓️ The date
- 👥 The 

Separate and clear.


## 📌 3️⃣ This is what output_type does
When you use ``output_type``=, you tell the Agent:
**"Don’t give me messy text — give me neat data with labels."**

So instead of:

```
"The meeting is Team Sync..."
```

You get:

```
{
  "name": "Team Sync",
  "date": "Friday",
  "participants": ["Alice", "Bob"]
}
```


## 📌 4️⃣ How do you tell the Agent what the data should look like?

👉 You **make a model** — like a **template**.

Example:

```
from pydantic import BaseModel

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]
```

You just told the Agent:
**“I want:

- a name (text),
- a date (text),
- a list of names (people).”**

## 📌 5️⃣ How to use it

When you make your agent, add ``output_type``:
```
agent = Agent(
  name="Calendar Extractor",
  instructions="Extract calendar events from text",
  output_type=CalendarEvent  # 👈 Use my model!
)
```

Now the Agent knows: **“I must reply in this format!”**

## 📌 6️⃣ What do you get back?
When you ask:
```
"Schedule Team Sync on Friday with Alice and Bob."
```

You get:

```
CalendarEvent(
  name="Team Sync",
  date="Friday",
  participants=["Alice", "Bob"]
)
```

👉 This is **organized** data — your code can **save** , **edit** , or send it easily.


## 📌 7️⃣ Super simple takeaway

| Without `output_type`               |  	With `output_type`
| ------------------------------------|:-------------------------------------:|
| Just words (one block of text)      | Neat data you can trust               |
| Hard for code to split              | Hard for code to split                |
| Can be messy                        | Always same shape                     |

## ✅ Why use it?

- 📦 Makes AI answers neat.
- 🧩 Easier for your program.
- 🔒 Less mistakes.



## ⭐️ One line summary

👉 `output_type` = **“Hey AI, give me data in a clear box, not random text.”**




