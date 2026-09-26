def compute_status(delay_days: int) -> str:
    if delay_days == 0:
        return "on_time"
    elif delay_days <= 2:
        return "minor_delay"
    else:
        return "major_delay"


@transform(
    output=Output("/logistics/shipment_status"),
    shipments=Input("/logistics/raw_shipments"),
)
def compute_shipment_status(output, shipments):
    df = shipments.dataframe()
    df["status"] = df["delay_days"].apply(compute_status)
    output.write_dataframe(df)