import asyncio
import os
from scrapestorm_lib import get_scrapestorm_json, test_scrapestorm
from api_lib import test_api
from log import log
from config import config
import time

INSTA_API_CHECK_PATH = "insta/api/check/"


async def collector_start():
    log_pid = f"collector-{os.getpid()}: "
    while not await test_api(config.insta_api_path + INSTA_API_CHECK_PATH, log_pid):
        await asyncio.sleep(2)
    while not await test_scrapestorm("scrapestorm.net", log_pid):
        await asyncio.sleep(2)
    log.info("has started")

    while True:
        try:
            # sync with hour
            while True:
                time.sleep(60)
                break
        except Exception as exc:
            log.error(log_pid + f"exception: {exc}")


if __name__ == "__main__":
    asyncio.run(collector_start())
