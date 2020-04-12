import aiomysql
from configuration import HOST, USER, PASSWORD, DB

async def open_connection(host=HOST, user=USER, password=PASSWORD, db=DB, autocommit=True):
    return await aiomysql.connect(host=host, user=user, password=password, db=db, autocommit=autocommit)

async def execute_single_query(query):
    conn = await open_connection()
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(query)
            await cursor.close()
            await conn.commit()
    except aiomysql.Error as e:
        print(e)