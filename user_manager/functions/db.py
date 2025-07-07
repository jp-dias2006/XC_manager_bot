import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()
POSTGRES_URL = os.getenv('POSTGRES_URL')

async def save_user(user_id: int, name: str, phone: str = None, first_contact: str = None):
    conn = await asyncpg.connect(POSTGRES_URL)
    try:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id BIGINT PRIMARY KEY,
                name TEXT,
                phone TEXT,
                first_contact TIMESTAMP
            )
        ''')
        await conn.execute('''
            INSERT INTO users(id, name, phone, first_contact)
            VALUES($1, $2, $3, $4)
            ON CONFLICT (id) DO NOTHING
        ''', user_id, name, phone, first_contact)
    finally:
        await conn.close()
