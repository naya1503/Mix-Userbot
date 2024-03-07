from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")

api_id = int(getenv("api_id", None))
api_hash = getenv("api_hash", None)
session = getenv("session", None)
bot_token = getenv("bot_token", None)
db_name = getenv("db_name", None)
mongo_uri = getenv("mongo_uri", None)
def_bahasa = getenv("def_bahasa", "en")
log_pic = getenv("log_pic", "https://telegra.ph//file/43cec0ae0ded594b55247.jpg")
heroku_api = getenv("heroku_api")
heroku_app_name = getenv("heroku_app_name")
upstream_repo = getenv(
    "upstream_repo",
    "https://github.com/naya1503/Mix-Userbot",
)
upstream_branch = getenv("upstream_branch", "dev")
git_token = getenv("git_token", None)
alive_pic = getenv("alive_pic", "https://telegra.ph//file/43cec0ae0ded594b55247.jpg")
log_channel = getenv("log_channel", "")
