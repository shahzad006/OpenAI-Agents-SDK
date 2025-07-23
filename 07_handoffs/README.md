# OpenAI Agents SDk Handoffs

## 📌 What are Handoffs?
👉 In OpenAI Agents SDK, **handoffs** mean:
**One agent** can **pass** work to **another agent** or tool when it needs help.

Think of it like:
- A shopkeeper (agent) calls the delivery boy (another agent) to deliver your order.
- Or a teacher (agent) asks a calculator (tool) to solve a math question.



## ✅ Why use handoffs?
Because:

- One agent can’t do everything perfectly.
- Some tasks are better done by another agent or a special tool.
- It makes your app smarter and cleaner.



# Step-by-Step: How handoffs work



## Step 1: Make agents or tools
You make an agent for each job.

- Example: `OrderAgent` for taking orders.
- Example: `DeliveryAgent` for deliveries.
- Example: `MathTool` for solving sums.



## Step 2: One agent finds it needs 
The first agent runs.
It gets a request it can’t finish alone.

- Example: OrderAgent needs DeliveryAgent to arrange delivery.



## Step 3: The agent does a HANDOFF
- It says:
**“I can’t do this part, let me hand it off to DeliveryAgent.”**




## Step 4: The other agent or tool does the job
- The `DeliveryAgent` picks up the work.
- Does its task.
- Returns result if needed.




## Step 5: The first agent continues (optional)
- Sometimes the first agent waits.
- Gets the result.
- Gives final answer to the user.



## 💡 Example in real words

**Example scenario:**

> You ask: “Book me a pizza and deliver it to my home.”

1️⃣ `PizzaAgent` takes your order.   <br>
2️⃣ `PizzaAgent` can’t deliver pizza. So it does a **handoff** to `DeliveryAgent.` <br>
3️⃣ `DeliveryAgent` arranges the delivery. <br>
4️⃣ You get your pizza! 🎉 <br>

## ⚙️ How to do it in code?
In code you:

- Create multiple agents.
- Use the handoff feature:

```
from agents import Agent

pizza_agent = Agent(
    name="PizzaAgent",
    ...
)

delivery_agent = Agent(
    name="DeliveryAgent",
    ...
)


# Inside PizzaAgent’s instructions:
# If delivery needed:

agent: Agent = Agent(
    name="Assistant", 
    model="gemini-2.0-flash",
    handoffs=[delivery_agent,pizza_agent]
)

```

## ✅ Key point
**Handoffs = passing work to another helper** <br>
So your main agent stays simple. <br>
Helpers handle special tasks.
