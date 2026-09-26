from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

shipments_db = {}
class ShipmentIn(BaseModel):
    carrier: str
    delay_days: int
@app.get("/shipments/{shipment_id}")
def get_shipment(shipment_id: str):

    if shipment_id not in shipments_db:
        raise HTTPException(
            status_code=404,
            detail="Shipment not found"m
        )

    shipment = shipments_db[shipment_id]

    return {
        "shipment_id": shipment_id,
        "carrier": shipment["carrier"],
        "delay_days": shipment["delay_days"],
        "status": compute_status(shipment["delay_days"])
    }


@app.post("/shipments/{shipment_id}")
def create_shipment(shipment_id: str, shipment: ShipmentIn):

    shipments_db[shipment_id] = {
        "carrier": shipment.carrier,
        "delay_days": shipment.delay_days
    }

    return {
        "shipment_id": shipment_id,
        "carrier": shipment.carrier,
        "delay_days": shipment.delay_days,
        "status": compute_status(shipment.delay_days)
    }
def compute_status(delay_days: int) -> str:
    """Return shipment status based on the number of delay days required."""
    if delay_days == 0:
        return "on_time"
    elif delay_days <= 2:
        return "minor_delay"
    else:
        return "major_delay"

print(compute_status(0))
print(compute_status(1))
print(compute_status(3))

class Shipment:

    def __init__(self, shipment_id: str, carrier: str, delay_days: int):
        self.shipment_id = shipment_id
        self.carrier = carrier
        self.delay_days = delay_days

    def status(self) -> str:
        return compute_status(self.delay_days)
shipment = Shipment("S001", "FastFreight", 2)

print(shipment.shipment_id)
print(shipment.carrier)
print(shipment.delay_days)
print(shipment.status())