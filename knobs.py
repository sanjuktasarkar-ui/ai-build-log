from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()


def ask(prompt, max_tokens=500, stop=None, effort=None):
    extra = {}
    if stop:
        extra["stop_sequences"] = stop
    if effort:
        extra["output_config"] = {"effort": effort}

    resp = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
        **extra,
    )

    text = "".join(b.text for b in resp.content if b.type == "text")
    print("blocks:     ", [b.type for b in resp.content])
    print("stop_reason:", resp.stop_reason)
    print("tokens:      in", resp.usage.input_tokens, "out", resp.usage.output_tokens)
    print("text:       ", text)
    print("-" * 50)
    return text

#ask("How should a mid-size company decide whether to build or buy a CRM?", max_tokens=1500, effort="low")
ask("How should a mid-size company decide whether to build or buy a CRM?", max_tokens=8000, effort="max")