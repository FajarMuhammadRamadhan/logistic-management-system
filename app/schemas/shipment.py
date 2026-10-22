from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ShipmentCourierResponse(BaseModel):
    id: int
    tracking_number: str
    status: str
    recipient_name: str
    recipient_phone: str
    destination_address: str
    package_description: str
    weight_kg: float
    created_at: datetime

    class Config:
        from_attributes = True