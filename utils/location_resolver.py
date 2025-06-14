
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable, GeocoderTimedOut

geolocator = Nominatim(user_agent="dream-sense-bot")

async def resolve_location_russian_to_english(location_ru: str) -> str:
    try:
        location = geolocator.geocode(location_ru, language="en")
        if location:
            return location.address
    except (GeocoderUnavailable, GeocoderTimedOut):
        pass
    return location_ru
