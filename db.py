import asyncpg
from config import DB_URL

async def init_db():
    conn = await asyncpg.connect(DB_URL)
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            telegram_id BIGINT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            birth_date DATE NOT NULL,
            birth_time TIME,
            birth_place TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    await conn.close()

async def save_user(telegram_id, name, birth_date, birth_time, birth_place):
    conn = await asyncpg.connect(DB_URL)
    await conn.execute("""
        INSERT INTO users (telegram_id, name, birth_date, birth_time, birth_place)
        VALUES ($1, $2, $3, $4, $5)
        ON CONFLICT (telegram_id) DO UPDATE SET
            name = EXCLUDED.name,
            birth_date = EXCLUDED.birth_date,
            birth_time = EXCLUDED.birth_time,
            birth_place = EXCLUDED.birth_place;
    """, telegram_id, name, birth_date, birth_time, birth_place)
    await conn.close()
