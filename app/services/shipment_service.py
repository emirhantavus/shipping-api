from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.shipment import Shipment
from app.schemas.shipment import ShipmentIn, ShipmentUpdateStatus
import uuid

def generate_tracking_number():
      return f"T-{uuid.uuid4().hex[:8]}"

async def create_shipment(db: AsyncSession, shipment_in: ShipmentIn) -> Shipment:
      tracking_number = generate_tracking_number()
      shipment_data = shipment_in.dict()
      shipment_data['tracking_number'] = tracking_number
      
      shipment = Shipment(**shipment_data)
      db.add(shipment)
      await db.commit()
      await db.refresh(shipment)
      return shipment

async def get_shipment_by_id(db: AsyncSession, shipment_id: str) -> Shipment:
      result = await db.execute(
            select(Shipment).where(Shipment.id==shipment_id)
      )
      return result.scalar_one_or_none()

async def get_tracking_number(db: AsyncSession, tracking_number: str) -> Shipment:
      result = await db.execute(
            select(Shipment).where(Shipment.tracking_number == tracking_number)
      )
      return result.scalar_one_or_none()

async def update_shipment_status(db: AsyncSession, shipment_id: str, status_update: ShipmentUpdateStatus) -> Shipment:
      result = await db.execute(
            select(Shipment).where(Shipment.id==shipment_id)
      )
      shipment = result.scalar_one_or_none()
      if not shipment:
            return None
      shipment.status = status_update.status
      await db.commit()
      await db.refresh(shipment)
      return shipment

async def list_shipments(db: AsyncSession):
      result = await db.execute(select(Shipment))
      return result.scalars().all()

async def delete_shipment(db: AsyncSession, shipment_id: str) -> bool:
      result = await db.execute(
            select(Shipment).where(Shipment.id==shipment_id)
      )
      shipment = result.scalar_one_or_none()
      if not shipment:
            return False
      await db.delete(shipment)
      await db.commit()
      return True