import asyncio
import logging

from app.config import Config
from app.utils import configure_logger
from app.errors import QuoterException

import telegram
import pymongo
from bson.json_util import dumps


conf = Config()
configure_logger()

BOT_API_TOKEN = conf.bot_api_token
CHAT_ID = conf.chat_id
DB_NAME = conf.mongo_db
SALES_COLL = conf.sales_coll
QUOTER_COLL = conf.quoter_coll

client = pymongo.MongoClient(conf.mongodb_url)
db = client[DB_NAME]
change_stream = db[SALES_COLL].watch()
bot = telegram.Bot(token=BOT_API_TOKEN)
log = logging.getLogger()


def get_sale_details(quoter_id: str) -> float:
    quoter = db[QUOTER_COLL].find_one(  
                {"_id": quoter_id}
            )
    if not quoter:
        raise ValueError("")
    return quoter.get("total")

async def main():
    log.info("Listening started")
    for change in change_stream:
        log.info("Listening ...")
        log.info(change)
        quoter_id = change.get("fullDocument").get("quoter_id")
        date = change.get("fullDocument").get("date")
        try:
            venta_total = get_sale_details(quoter_id)
            message = (f"¡Venta hecha con un total de: ${int(venta_total)} "
                   f"hecha el dia:{date}!"
            )
        except QuoterException:
            message = ("Se hizo una venta pero intentaron "
                       "alterar el sistema, reviselo porfavor"
            )
        
        await bot.sendMessage(chat_id=CHAT_ID, text=message)




if __name__ == "__main__":
    asyncio.run(main())