from openai import OpenAI
key = "KEY"
client = OpenAI(api_key = key)

def generate(system,user):
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": user}
    ]
    )

    return completion.choices[0].message