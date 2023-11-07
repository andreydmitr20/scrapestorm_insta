import asyncio

import aiohttp
from log import log, log_service_is_not_ready

from config import config

SCRAPESTORM_CREDITS_API_PATH = "https://scrapestorm.net/api/token/status"


async def get_scrapestorm_json(api_path: str, api_params: dict = {}) -> dict:
    """get_scrapestorm_json"""
    headers = {
        "accept": "application/json",
    }

    params = {
        "token": config.scrapestorm_api_key,
    }
    params.update(api_params)

    async with aiohttp.ClientSession() as api_session:
        async with api_session.get(
            api_path,
            params=params,
            headers=headers,
            timeout=aiohttp.ClientTimeout(total=config.scrapestorm_timeout_int),
        ) as response:
            if "application/json" in response.headers.get("Content-Type", ""):
                return await response.json()
            else:
                # Handle unexpected Content-Type
                raise ValueError(
                    # f"Unexpected Content-Type: {response.headers.get('Content-Type')}"
                    f"Unexpected Content-Type: {response}"
                )


async def test_scrapestorm(service: str, log_pid: str):
    response = None
    try:
        response = await get_scrapestorm_json(SCRAPESTORM_CREDITS_API_PATH)
        # print(f"{response}")
        if response and type(response) == dict and response["credits"] > 0:
            return True
    except Exception as exception:
        log_service_is_not_ready(service, log_pid)
        # print(f"{exception}")
    return False


async def test():
    credits = await get_scrapestorm_json(SCRAPESTORM_CREDITS_API_PATH)
    log.info(f"Scrapestorm.net credits: {credits}")


if __name__ == "__main__":
    asyncio.run(test())
