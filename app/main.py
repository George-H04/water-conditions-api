from os import error
from fastapi import FastAPI
from pydantic import ValidationError
from requests import get
from app.scripts import util
from app.models import WaterConditions

app = FastAPI()


@app.get("/health")
def status():
    return {"message": "Water Conditions API", "status": "Running"}


@app.get("/conditions")
def get_conditions():
    r = get(
        "https://api.waterdata.usgs.gov/ogcapi/v0/collections/latest-continuous/items?f=json&lang=en-US&limit=10&skipGeometry=false&offset=0&monitoring_location_id=USGS-03070260"
    )

    data_dict = {}

    # TODO: Think of a smarter approach, also think about how to include
    #       historical data, as that will also be vital for my purposes.

    for item in r.json()["features"]:
        id = item["properties"]["parameter_code"]
        value = item["properties"]["value"]

        name = util.id_to_name(id)
        unit = util.id_to_unit(id)

        if "°C" in unit:
            value = util.c_to_f(value)
            unit = "°F"

        data_dict[name] = {"value": value, "unit": unit}
        print(data_dict[name])

    try:
        conditions = WaterConditions(
            flowRate=data_dict["Flow rate"],
            temperature=data_dict["Water temperature"],
            waterLevel=data_dict["Water level"],
            precipitation=data_dict["Precipitation"],
        )

    except ValidationError:
        return error("Conditions could not be computed")

    return conditions
