from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime

class ShipmentIn(BaseModel):
      sender_name: str
      sender_address: str
      receiver_name: str
      receiver_address: str
      receiver_phone: Optional[str] = None
      description: Optional[str] = None
      
class ShipmentStatus(str, Enum):
      pending = 'pending'
      in_transit = 'in_transit'
      delivered = 'delivered'
      cancelled = 'cancelled'
      
class ShipmentOut(BaseModel):
      id: str
      tracking_number: str
      sender_name: str
      sender_address: str
      receiver_name: str
      receiver_address: str
      receiver_phone: Optional[str] = None
      status: ShipmentStatus
      description: Optional[str] = None
      created_at: datetime
      updated_at: datetime
      
class ShipmentUpdateStatus(BaseModel):
      status: ShipmentStatus