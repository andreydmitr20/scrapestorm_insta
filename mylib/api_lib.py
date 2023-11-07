import asyncio
import aiohttp
from config import config
from log import log, d, log_service_is_not_ready


async def api_get(url, params=None, data=None, token=None):
    headers = None
    if token:
        headers = {"Authorization": f"Bearer {token}"}

    async with aiohttp.ClientSession() as api_session:
        async with api_session.get(
            url, params=params, data=data, headers=headers
        ) as response:
            if "application/json" in response.headers.get("Content-Type", ""):
                return await response.json()
            else:
                # Handle unexpected Content-Type
                raise ValueError(
                    # f"Unexpected Content-Type: {response.headers.get('Content-Type')}"
                    f"Unexpected Content-Type: {response}"
                )


async def api_put(url, params=None, data=None):
    async with aiohttp.ClientSession() as api_session:
        async with api_session.put(url, params=params, data=data) as response:
            if "application/json" in response.headers.get("Content-Type", ""):
                return await response.json()
            else:
                # Handle unexpected Content-Type
                raise ValueError(
                    # f"Unexpected Content-Type: {response.headers.get('Content-Type')}"
                    f"Unexpected Content-Type: {response}"
                )


async def api_post(url, params=None, data=None):
    async with aiohttp.ClientSession() as api_session:
        async with api_session.post(url, params=params, data=data) as response:
            if "application/json" in response.headers.get("Content-Type", ""):
                return await response.json()
            else:
                # Handle unexpected Content-Type
                raise ValueError(
                    # f"Unexpected Content-Type: {response.headers.get('Content-Type')}"
                    f"Unexpected Content-Type: {response}"
                )


async def api_delete(url, params=None, data=None):
    async with aiohttp.ClientSession() as api_session:
        async with api_session.delete(url, params=params, data=data) as response:
            if "application/json" in response.headers.get("Content-Type", ""):
                return await response.json()
            else:
                # Handle unexpected Content-Type
                raise ValueError(
                    # f"Unexpected Content-Type: {response.headers.get('Content-Type')}"
                    f"Unexpected Content-Type: {response}"
                )


async def test_api(service: str, log_pid: str):
    response = None
    try:
        response = await api_get(url=service)
        # print(f"{response}")
        if response and type(response) == list and response[0]["api_status"] == "ok":
            return True
    except Exception as exception:
        log_service_is_not_ready(service, log_pid)
        # print(f"{exception}")
    return False
