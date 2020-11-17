import asyncpg
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

PSQL_CONNECTION_URL = os.getenv('PSQL_CONNECTION_URL')


async def test():
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    await conn.close()

async def get_all_users():
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("SELECT * FROM users WHERE user_id='124668192948748288'")
    print(await stmt.fetch())
    await conn.close()

async def create_user(id: int):
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("INSERT INTO users(user_id) VALUES ($1) RETURNING user_id, essence, currency, stage")
    result = await stmt.fetch(id)
    await conn.close()
    return result

async def get_user(id: int):
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("SELECT * FROM users WHERE user_id=$1")
    result = await stmt.fetch(id)
    if not result:
        result = await create_user(id)
    await conn.close()
    user_data = {}
    for field, value in result[0].items():
        user_data[field] = value
    print(user_data)
    return user_data

#TODO: add elo field to users, add position field to units

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(get_user(487291708846112779))
