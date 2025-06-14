#import asyncio
#from db import engine, Base
#from models.user_location import UserLocation

#async def init_db():
#    print("📦 Модели для создания:", Base.metadata.tables.keys())
#    async with engine.begin() as conn:
#        await conn.run_sync(Base.metadata.create_all)
#    print("✅ База данных и таблицы успешно созданы.")

#if __name__ == "__main__":
#    asyncio.run(init_db())
