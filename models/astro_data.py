
from sqlalchemy import Column, Integer, String, Float, Date, Text, TIMESTAMP, func
from db import Base

class AstroData(Base):
    __tablename__ = "astro_data"

    id = Column(Integer, primary_key=True)
    location = Column(Text, nullable=False)
    date = Column(Date, nullable=False)
    moon_phase = Column(String)
    moon_illumination = Column(Integer)
    sunrise = Column(String)
    sunset = Column(String)
    moonrise = Column(String)
    moonset = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())
