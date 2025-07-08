import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()
POSTGRES_URL = os.getenv('POSTGRES_URL')

async def save_user(user_id: int, name: str, first_contact: str = None):
    conn = await asyncpg.connect(POSTGRES_URL)
    try:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id BIGINT PRIMARY KEY,
                name TEXT,
                first_contact TIMESTAMP
            )
        ''')
        await conn.execute('''
            INSERT INTO users(id, name, first_contact)
            VALUES($1, $2, $3)
            ON CONFLICT (id) DO NOTHING
        ''', user_id, name, first_contact)
    finally:
        await conn.close()
