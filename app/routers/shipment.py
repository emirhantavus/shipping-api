from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.shipment import ShipmentIn, ShipmentOut,ShipmentUpdateStatus
from app.services.shipment_service import (
      create_shipment, delete_shipment, get_shipment_by_id ,list_shipments, update_shipment_status
)
from app.db.session import get_db

router = APIRouter()

@router.post("/shipments/", response_model=ShipmentOut,status_code=status.HTTP_201_CREATED)
async def create_shipment_endpoint(shipment_in: ShipmentIn, db: AsyncSession = Depends(get_db)):
      shipment = await create_shipment(db, shipment_in)
      return shipment

@router.get("/shipments/",response_model=list[ShipmentOut],status_code=status.HTTP_200_OK)
async def list_shipments_endpoint(db: AsyncSession = Depends(get_db)):
      return await list_shipments(db)

@router.get("/shipments/{shipment_id}/", response_model=ShipmentOut)
async def get_shipment_endpoint(shipment_id: str, db: AsyncSession = Depends(get_db)):
      shipment = await get_shipment_by_id(db, shipment_id)
      if not shipment:
            raise HTTPException(status_code=404, detail='Shipment not found')
      return shipment

@router.patch("/shipments/{shipment_id}/status/", response_model=ShipmentOut)
async def update_shipment_status_endpoint(
      shipment_id: str, status_update: ShipmentUpdateStatus ,db: AsyncSession = Depends(get_db)):
      shipment = await update_shipment_status(db, shipment_id, status_update)
      if not shipment:
            raise HTTPException(status_code=404, detail='Shipment not found')
      return shipment

@router.delete("/shipments/{shipment_id}/",status_code=status.HTTP_204_NO_CONTENT)
async def delete_shipment_endpoint(
      shipment_id: str, db: AsyncSession = Depends(get_db)):
      result = await delete_shipment(db, shipment_id)
      if not result:
            raise HTTPException(status_code=404, detail='Shipment not found')