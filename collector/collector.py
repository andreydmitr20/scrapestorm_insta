import asyncio
import os
from scrapestorm_lib import get_scrapestorm_json, test_scrapestorm
from api_lib import test_api
from log import log
from config import config

INSTA_API_CHECH_PATH = "insta/api/check/"


async def collector_start():
    log_pid = f"collector-{os.getpid()}: "
    while not await test_api(config.insta_api_path + INSTA_API_CHECH_PATH, log_pid):
        await asyncio.sleep(2)
    while not await test_scrapestorm("scrapestorm.net", log_pid):
        await asyncio.sleep(2)
    log.info("has started")


if __name__ == "__main__":
    asyncio.run(collector_start())
