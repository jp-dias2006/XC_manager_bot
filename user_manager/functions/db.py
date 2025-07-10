import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()
POSTGRES_URL = os.getenv('POSTGRES_URL')

async def save_user(user_id: int, name: str, first_contact: str = None):
    conn = await asyncpg.connect(POSTGRES_URL)
    try:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id BIGINT PRIMARY KEY,
                name TEXT,
                first_contact TIMESTAMP
            )
        ''')
        await conn.execute('''
            INSERT INTO usuarios(id, nome, data_contato)
            VALUES($1, $2, $3)
            ON CONFLICT (id) DO NOTHING
        ''', user_id, name, first_contact)
    finally:
        await conn.close()

async def user_exists(user_id: int) -> bool:
    conn = await asyncpg.connect(POSTGRES_URL)
    try:
        row = await conn.fetchrow('SELECT id FROM usuarios WHERE id = $1', user_id)
        return row is not None
    finally:
        await conn.close()
