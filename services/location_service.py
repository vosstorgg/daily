
from models.user_location import UserLocation
from db import SessionLocal
from utils.location_resolver import resolve_location_russian_to_english

async def save_user_location(user_id: int, raw_location: str):
    resolved = await resolve_location_russian_to_english(raw_location)
    async with SessionLocal() as session:
        loc = UserLocation(
            user_id=user_id,
            raw_location=raw_location,
            resolved_location=resolved
        )
        session.add(loc)
        await session.commit()
