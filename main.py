import openai

openai.api_key="" #PUT YOUR KEY HERE

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5
    )

    message = completions.choices[0].text
    return message.strip()

prompt="What is the fastest car in the world?"
print(generate_text(prompt))