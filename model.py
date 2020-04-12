from datetime import datetime

import faust

from utils import open_connection


class Classified(faust.Record):
    id: str = ''
    customer_id: str = ''
    created_at: str = ''
    text: str = ''
    ad_type: str = 'Free'
    price: float = 0.0 # To describe an optional field, provide a default value
    currency: str = 'EUR'
    payment_type: str = 'Offline'
    payment_cost: float = 0.0


class MarginModel(faust.Record):
    timestamp: datetime
    discriminator: str
    type: str
    count: int
    margin: float

class ClassifiedsTableModel:
    def __init__(self):
        self.conn = None

    async def start(self):
        self.conn = await open_connection(autocommit=False)

    async def insert_classified(self, messages=[]):
        async with self.conn.cursor() as cursor:
            print("insert {}".format(messages))
            for message in messages:
                sql = ("INSERT INTO Classifieds (id" +
                       ", customer_id, created_at, text" +
                       ", ad_type, price, currency" +
                       ", payment_type, payment_cost) "
                       + "VALUES('"
                       + message.id + "','"
                       + message.customer_id + "','"
                       + message.created_at + "','"
                       + message.text + "','"
                       + message.ad_type + "','"
                       + str(message.price) + "','"
                       + message.currency + "','"
                       + message.payment_type + "','"
                       + str(message.payment_cost) + "') "
                       + "ON DUPLICATE KEY UPDATE "
                       + "id = '" + message.id + "',"
                       + "customer_id = '" + message.customer_id + "',"
                       + "created_at = '" + message.created_at + "',"
                       + "text = '" + message.text + "',"
                       + "ad_type = '" + message.ad_type + "',"
                       + "price = '" + str(message.price) + "',"
                       + "currency = '" + message.currency + "',"
                       + "payment_type = '" + message.payment_type + "',"
                       + "payment_cost = '" + str(message.payment_cost) + "'"
                       + ";")
                await cursor.execute(sql)
            await self.conn.commit()
