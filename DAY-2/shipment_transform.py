def transform(**kwargs):
    def decorator(func):
        return func
    return decorator
@transform(
        output="shipment_status_output",
    shipments="shipment_input"
)
def compute_shipment_status(shipments: list[dict]) -> list[dict]:
    results = []

    for shipment in shipments:
        delay_days = shipment["delay_days"]

        if delay_days == 0:
            status = "on_time"
        elif delay_days <= 2:
            status = "minor_delay"
        else:
            status = "major_delay"

        results.append({
            "shipment_id": shipment["shipment_id"],
            "carrier": shipment["carrier"],
            "delay_days": delay_days,
            "status": status
        })

    return results


shipments = [
    {
        "shipment_id": "S001",
        "carrier": "FastFreight",
        "delay_days": 0
    },
    {
        "shipment_id": "S002",
        "carrier": "QuickShip",
        "delay_days": 2
    },
    {
        "shipment_id": "S003",
        "carrier": "GlobalLogix",
        "delay_days": 5
    }
]

result = compute_shipment_status(shipments)

print(result)