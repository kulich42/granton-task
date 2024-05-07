# Granton interview task

This project implements REST API to provide name, arena, league and colors of hockey teams.
This information is fetched from ChatGPT.

## Running the project

* install poetry (https://python-poetry.org/)
* run `poetry install` in the project root directory
* set `OPENAI_API_KEY` environment variable to your OpenAI API key
* run `uvicorn api.main:app --reload --port 8000`
* go to `/api/teamDescription` and provide the team name as `teamName` query parameter