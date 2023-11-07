""" get constants from .env"""
import os

from dotenv import load_dotenv

load_dotenv()


# from config import config
class config:
    """common config constants"""

    scrapestorm_api_key: str = os.getenv("scrapestorm_api_key")
    scrapestorm_api_user_profile: str = os.getenv("scrapestorm_api_user_profile")
    scrapestorm_api_media_info: str = os.getenv("scrapestorm_api_media_info")
    scrapestorm_timeout_int: int = int(os.getenv("scrapestorm_timeout"))

    insta_api_path: str = os.getenv("insta_api_path")

    db_proto: str = os.getenv("db_proto")
    db_user: str = os.getenv("db_user")
    db_pass: str = os.getenv("db_pass")
    db_host: str = os.getenv("db_host")
    db_name: str = os.getenv("db_name")
    db_port: str = os.getenv("db_port")

    redis_host = os.getenv("redis_host")
    redis_port = os.getenv("redis_port")
