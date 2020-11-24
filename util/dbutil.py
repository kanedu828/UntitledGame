import asyncpg
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

PSQL_CONNECTION_URL = os.getenv('PSQL_CONNECTION_URL')

async def get_all_users():
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("SELECT * FROM users WHERE user_id='124668192948748288'")
    print(await stmt.fetch())
    await conn.close()

async def insert_user(id: int):
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("INSERT INTO users(user_id) VALUES ($1) RETURNING user_id, essence, currency, stage, elo")
    result = await stmt.fetch(id)
    await conn.close()
    return result

async def get_user(id: int):
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("SELECT * FROM users WHERE user_id=$1")
    result = await stmt.fetch(id)
    if not result:
        result = await insert_user(id)
    await conn.close()
    user_data = {}
    for field, value in result[0].items():
        user_data[field] = value
    return user_data

async def insert_unit(unit_id: int, user_id: int, location: int):
    await get_user(user_id)
    unit = await get_unit(unit_id, user_id)
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    if unit:
        stmt = await conn.prepare("UPDATE units SET stars=stars + 1 WHERE unit_id=$1 AND user_id=$2 RETURNING unit_id, user_id, location, level, stars")
        result = await stmt.fetch(unit_id, user_id)
    else:
        stmt = await conn.prepare("INSERT INTO units(unit_id, user_id, location) VALUES ($1, $2, $3) RETURNING unit_id, user_id, location, level, stars")
        result = await stmt.fetch(unit_id, user_id, location)
    await conn.close()
    return result

async def get_unit(unit_id: int, user_id: int):
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("SELECT * FROM units WHERE unit_id=$1 AND user_id=$2")
    result = await stmt.fetch(unit_id, user_id)
    return result

async def get_units(user_id: int, location: int):
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("SELECT * FROM units WHERE user_id=$1 AND location=$2")
    result = await stmt.fetch(user_id, location)
    units = {}
    for unit in result:
        units[unit.get('unit_id')] = {}
        for field, value in unit.items():
            if not field == 'unit_id':
                units[unit.get('unit_id')][field] = value
    return units

async def update_user_essence(user_id: int, amount: int):
    await get_user(user_id)
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("UPDATE users SET essence=essence + $2 WHERE user_id=$1 RETURNING user_id, essence, currency, stage, elo")
    result = await stmt.fetch(user_id, amount)
    await conn.close()
    return result

async def update_user_currency(user_id: int, amount: int):
    await get_user(user_id)
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("UPDATE users SET currency=currency + $2 WHERE user_id=$1 RETURNING user_id, essence, currency, stage, elo")
    result = await stmt.fetch(user_id, amount)
    await conn.close()
    return result

async def update_user_stage(user_id: int, amount: int):
    await get_user(user_id)
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("UPDATE users SET stage=stage + $2 WHERE user_id=$1 RETURNING user_id, essence, currency, stage, elo")
    result = await stmt.fetch(user_id, amount)
    await conn.close()
    return result

async def update_user_elo(user_id: int, amount: int):
    await get_user(user_id)
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("UPDATE users SET elo=elo + $2 WHERE user_id=$1 RETURNING user_id, essence, currency, stage, elo")
    result = await stmt.fetch(user_id, amount)
    await conn.close()
    return result

async def update_unit_level(unit_id: int, user_id: int, amount: int):
    unit = await get_unit(unit_id, user_id)
    if not unit:
        return None
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("UPDATE units SET level=level + $3 WHERE unit_id=$1 AND user_id=$2 RETURNING unit_id, user_id, location, level, stars")
    result = await stmt.fetch(unit_id, user_id, amount)
    await conn.close()
    return result

async def update_unit_location(unit_id: int, user_id: int, location: int):
    unit = await get_unit(unit_id, user_id)
    if not unit:
        return None
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("UPDATE units SET location=$3 WHERE unit_id=$1 AND user_id=$2 RETURNING unit_id, user_id, location, level, stars")
    result = await stmt.fetch(unit_id, user_id, location)
    await conn.close()
    return result

if __name__ == '__main__':
    print(asyncio.get_event_loop().run_until_complete(update_user_stage(124668192948748288, 1)))
