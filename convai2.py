import openai

openai.api_key = "INSERT_YOUR_API_KEY_HERE"

def generate_response(context):
    prompt = f"Sir Dumbledore: {context}\nYou:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()
