import json

from httpx import AsyncClient


async def test_generate_team_description(
    client: AsyncClient, httpx_mock, chatgpt_response: str
) -> None:
    httpx_mock.add_response(
        content=json.dumps(
            {
                "choices": [
                    {
                        "finish_reason": "stop",
                        "index": 0,
                        "message": {
                            "function_call": {
                                "name": "team_desctiption",
                                "arguments": '{"name":"HC Vítkovice","arena":"Ostravar Aréna","league":'
                                '"Czech Extraliga","colors":"Blue, white and red"}',
                            },
                            "role": "assistant",
                        },
                        "logprobs": None,
                    }
                ],
                "created": 1677664795,
                "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
                "model": "gpt-3.5-turbo-0613",
                "object": "chat.completion",
                "usage": {
                    "completion_tokens": 17,
                    "prompt_tokens": 57,
                    "total_tokens": 74,
                },
            }
        ).encode()
    )
    r = await client.get(
        f"/api/teamDescription",
        params={"teamName": "Vítkovice"},
    )
    assert r.status_code == 200
    response_data = r.json()

    assert response_data == {
        "name": "HC Vítkovice",
        "arena": "Ostravar Aréna",
        "league": "Czech Extraliga",
        "colors": "Blue, white and red",
    }


async def test_generate_team_desctiption_service_unavailable(
    client: AsyncClient,
    httpx_mock,
) -> None:
    httpx_mock.add_response(status_code=503)
    r = await client.get(
        f"/api/teamDescription",
        params={"teamName": "Vítkovice"},
    )
    assert r.status_code == 502


async def test_generate_team_desctiption_no_chat_response(
    client: AsyncClient,
    httpx_mock,
) -> None:
    r = await client.get(
        f"/api/teamDescription",
        params={"teamName": "Vítkovice"},
    )
    assert r.status_code == 502


async def test_generate_team_desctiption_out_of_credits(
    client: AsyncClient,
    httpx_mock,
) -> None:
    httpx_mock.add_response(status_code=429)
    r = await client.get(
        f"/api/teamDescription",
        params={"teamName": "Vítkovice"},
    )
    assert r.status_code == 502
