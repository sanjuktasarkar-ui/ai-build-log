import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

resp = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=300,
    messages=[{"role": "user", "content": "In two sentences: what is a token?"}],
)

print(resp.content[0].text)
print(f"\nin: {resp.usage.input_tokens}  out: {resp.usage.output_tokens}")