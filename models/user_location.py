
from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP, func
from db import Base

class UserLocation(Base):
    __tablename__ = "user_locations"

    user_id = Column(BigInteger, primary_key=True)
    raw_location = Column(Text, nullable=False)
    resolved_location = Column(Text, nullable=False)
    timezone = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
