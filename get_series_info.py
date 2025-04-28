import os
from openai import OpenAI

def clean_response(text):
    text = text.replace("\\boxed{", "")
    text = text.replace("```text", "")
    text = text.replace("```", "")
    text = text.replace("}`", "")
    text = text.replace("}", "")
    return text.strip()

def get_series_info(series_name):
    api_key = os.getenv("OPENROUTER_API_KEY")
    base_url = os.getenv("BASE_URL")
    model_key = os.getenv("MODEL")

    if not api_key or not base_url or not model_key:
        raise ValueError("API key, base URL, or model is missing. Please add them to the .env file.")

    client = OpenAI(
        base_url=base_url,
        api_key=api_key,
    )

    response = client.chat.completions.create(
        extra_body={},
        model=model_key,
        messages=[
            {
                "role": "user",
                "content": f'Provide details about the TV series "{series_name}" in the following strict format: Name: [value] ============================ Plot: [value] ============================ Genres: [value] ============================ Number of Seasons: [value] ============================ Number of Episodes: [value] ============================ IMDB Rating: [value] ============================ Metacritic Score: [value] ============================ Language: [value] ============================ Top 5 Main Actors: 1. [Actor Name] (as [Character Name]) 2. [Actor Name] (as [Character Name]) 3. [Actor Name] (as [Character Name]) 4. [Actor Name] (as [Character Name]) 5. [Actor Name] (as [Character Name]) ============================ If the series does not exist, return exactly "Series Not Found" and nothing else. Return the output strictly as raw plain text without LaTeX, markdown, boxed format, or code fences like ```text. Do not wrap the output inside any code block or mathematical environment. Only return the pure text fields separated by "============================" as instructed.'
            }
        ]
    )

    return clean_response(response.choices[0].message.content)  

