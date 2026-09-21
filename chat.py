#The input token increases everytime as the history grows and is sent back to the model

from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()  # picks up ANTHROPIC_API_KEY from .env on its own

SYSTEM = "You are a concise assistant. Answer in at most three sentences."
history = []

while True:
    user = input("\nyou> ")
    if user.strip().lower() in ("quit", "exit"):
        break

    history.append({"role": "user", "content": user})

    resp = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=400,
        system=SYSTEM,
        messages=history,
    )

    reply = "".join(b.text for b in resp.content if b.type == "text")
    history.append({"role": "assistant", "content": reply}) 
    print(history)
    print(f"\nclaude> {reply}")
    print(f"[in: {resp.usage.input_tokens}  out: {resp.usage.output_tokens}]")