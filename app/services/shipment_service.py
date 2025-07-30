from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.shipment import Shipment
from app.schemas.shipment import ShipmentIn, ShipmentUpdateStatus

async def create_shipment(db: AsyncSession, shipment_in: ShipmentIn) -> Shipment:
      shipment = Shipment(**shipment_in.dict())
      db.add(shipment)
      await db.commit()
      await db.refresh(shipment)
      return shipment

async def get_shipment_by_id(db: AsyncSession, shipment_id: str) -> Shipment:
      result = await db.execute(
            select(Shipment).where(Shipment.id==shipment_id)
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