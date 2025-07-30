from sqlalchemy import Column, String, Enum, DateTime
from app.db.base import Base
import enum
import uuid
import datetime

class ShipmentStatus(str, enum.Enum):
      pending = "pending"
      in_transit = "in_transit"
      delivered = "delivered"
      cancelled = "cancelled"
      
class Shipment(Base):
      __tablename__="shipments"
      
      id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
      tracking_number = Column(String, unique=True, nullable=False)
      sender_name = Column(String, nullable=False)
      sender_adress = Column(String, nullable=False)
      receiver_name = Column(String, nullable=False)
      receiver_address = Column(String, nullable=False)
      receiver_phone = Column(String, nullable=True)
      status = Column(Enum(ShipmentStatus), nullable=False, default=ShipmentStatus.pending)
      description = Column(String, nullable=True)
      created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
      updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow, nullable=False)
      