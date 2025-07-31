import pytest
from httpx import AsyncClient
from app.main import app
import uuid

@pytest.mark.asyncio
async def test_shipment_crud_flow():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Note: All shipment CRUD tests are written in a single function to avoid async context and event loop issues.
        # Will be added in seperated funs later.
        # CREATE
        payload = {
            "tracking_number": str(uuid.uuid4()),
            "sender_name": "Emirhan",
            "sender_adress": "Yalova",
            "receiver_name": "Mehmet",
            "receiver_address": "Ankara",
            "receiver_phone": "5551234567",
            "description": "Test kargo"
        }
        response = await client.post("/api/shipments/", json=payload)
        assert response.status_code == 201
        shipment_id = response.json()["id"]

        # GET ALL
        response = await client.get("/api/shipments/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert any(item["id"] == shipment_id for item in data)

        # GET BY ID
        response = await client.get(f"/api/shipments/{shipment_id}/")
        assert response.status_code == 200
        assert response.json()["id"] == shipment_id

        # UPDATE STATUS
        payload = {"status": "in_transit"}
        response = await client.patch(f"/api/shipments/{shipment_id}/status/", json=payload)
        assert response.status_code == 200
        assert response.json()["status"] == "in_transit"

        # DELETE
        response = await client.delete(f"/api/shipments/{shipment_id}/")
        assert response.status_code == 204

        # GET DELETED
        response = await client.get(f"/api/shipments/{shipment_id}/")
        assert response.status_code == 404