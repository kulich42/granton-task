import re

import openai
from fastapi import FastAPI, HTTPException, Query, status

from api.openai_client import client

app = FastAPI(root_path="/api")


@app.get("/teamDescription")
def get_team_description(team_name: str = Query(alias="teamName")) -> dict[str, str]:
    chat_prompt = f"give me information about hockey team {team_name} in structured format field:value"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": chat_prompt}]
        )
    except openai.InternalServerError:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY)
    except openai.APITimeoutError:
        raise HTTPException(status_code=status.HTTP_504_GATEWAY_TIMEOUT)
    except openai.RateLimitError:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY)
    response_text = response.choices[0].message.content
    if response_text is None:
        raise HTTPException(status_code=404)

    fields = ["Name", "Arena", "League", "Colors"]
    result = {}
    for field in fields:
        match = re.search(f"{field}: (?P<value>.*)\n", response_text)
        if match is None:
            continue
        value = match.group("value")
        result[field] = value
    return result
