import os
import pymongo

client = pymongo.MongoClient("mongodb+srv://jesusjavieralbino:mongojesus@cotiz-app.zpvjrqx.mongodb.net/?retryWrites=true&w=majority")
data = {
    "date": "2023-06-29T02:10:21.256315",
    "quoter_id": "2023-06-29T02:10:21.256315"
}
print(client.changestream.business.sales.insert_one(data).inserted_id)