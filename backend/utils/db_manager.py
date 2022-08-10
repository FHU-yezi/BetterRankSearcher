from pymongo import MongoClient


def init_DB():
    connection: MongoClient = MongoClient(
        "mongodb", 27017
    )
    db = connection.BRSData
    return db


db = init_DB()

data = db.data
