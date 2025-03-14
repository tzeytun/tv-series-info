import os
from openai import OpenAI

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
                "content": f"Provide details about the TV series {series_name} including its name, plot, number of seasons, number of episodes, IMDB Rating, Metacritic Score, language, and the top 5 main actors. If the series does not exist, return 'Series Not Found' error. Use '============================' to separate each detail."
            }
        ]
    )

    return response.choices[0].message.content

