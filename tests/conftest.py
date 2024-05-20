from typing import AsyncIterator

import httpx
import pytest


@pytest.fixture(scope="session")
async def client() -> AsyncIterator[httpx.AsyncClient]:
    from api.main import app

    async with httpx.AsyncClient(base_url="https://test/", app=app) as c:
        yield c


@pytest.fixture(scope="session")
def chatgpt_response() -> str:
    return """Sure, here's the information about HC Vítkovice in a structured format without using markdown:

Name: HC Vítkovice
Founded: 1928
Location: Ostrava, Czech Republic
Arena: Ostravar Aréna
Capacity: 9,584
League: Czech Extraliga
Colors: Blue, white, and red
Manager: [Current manager's name]
Honors:
- Czechoslovak Extraliga: 1980–81, 1984–85, 1986–87, 1991–92
- Czech Extraliga: 1994–95
- Czechoslovak Cup: 1967, 1983
- Czech Cup: 2001, 2002, 2011, 2014
Notable Players:
- Martin Erat
- Jiří Dopita
- Jan Hlaváč
- Pavel Patera
Website: [Official Website, if available]"""
