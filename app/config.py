from pydantic import BaseSettings


class Config(BaseSettings):
    chat_id: str
    bot_api_token: str
    mongodb_url: str
    mongo_db: str
    sales_coll: str
    quoter_coll: str
    log_level: str = "INFO"
