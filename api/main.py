import json

import openai
from fastapi import FastAPI, HTTPException, Query, status

from api.openai_client import client

app = FastAPI(root_path="/api")


@app.get("/teamDescription")
def get_team_description(team_name: str = Query(alias="teamName")) -> dict[str, str]:
    chat_prompt = f"give me information about hockey team {team_name}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": chat_prompt}],
            functions=[
                {
                    "name": "team_description",
                    "description": "generate JSON description of a team",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "arena": {"type": "string"},
                            "league": {"type": "string"},
                            "colors": {
                                "type": "string",
                            },
                        },
                        "required": ["name", "arena", "league", "colors"],
                    },
                }
            ],
            function_call="auto",
        )
    except openai.InternalServerError:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY)
    except openai.APITimeoutError:
        raise HTTPException(status_code=status.HTTP_504_GATEWAY_TIMEOUT)
    except openai.RateLimitError:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY)
    function_call = response.choices[0].message.function_call
    if function_call is None:
        raise HTTPException(status_code=404)

    return json.loads(function_call.arguments)
