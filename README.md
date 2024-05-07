# Granton interview task

This project implements REST API to provide name, arena, league and colors of hockey teams.
This information is fetched from ChatGPT and extracted from the response using regular expressions.

## Running the project

* install poetry (https://python-poetry.org/)
* run `poetry install` in the project root directory
* set `OPENAI_API_KEY` environment variable to your OpenAI API key
* run `uvicorn api.main:app --reload --port 8000`
* go to `/api/teamDescription` and provide the team name as `teamName` query parameter

## Running in Docker
Note: I haven't been able to make this work, possibly due to WSL not  allowing ChatGPT to contact it's API
* run `docker build -t api .` in the project root
* run `docker run -p 8000:8000 api`