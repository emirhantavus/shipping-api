from pydantic import BaseModel
from typing import Optional
from enum import Enum

class ShipmentIn(BaseModel):
      order_id: int
      sender: str
      reciever: str
      reciever_phone: Optional[str] = None
      description: Optional[str] = None
      
class ShipmentOut(BaseModel):
      id: int
      order_id: int
      sender: str
      reciever: str
      status: str
      
class ShipmentStatus(str, Enum):
      pending = 'pending'
      in_transit = 'in_transit'
      delivered = 'delivered'
      cancelled = 'cancelled'
      
class ShipmentUpdateStatus(BaseModel):
      status: ShipmentStatus