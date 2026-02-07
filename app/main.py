from os import error
from fastapi import FastAPI
from pydantic import ValidationError
from requests import get
from app.scripts import util
from app.models import Condition, WaterConditions


app = FastAPI()


@app.get("/health")
def status():
    return {"message": "Water Conditions API", "status": "Running"}


@app.get("/conditions")
def get_conditions():

    r = get(
        "https://api.waterdata.usgs.gov/ogcapi/v0/collections/latest-continuous/items?f=json&lang=en-US&limit=10&skipGeometry=false&offset=0&monitoring_location_id=USGS-03070260"
    )

    # TODO: Think of a smarter approach, also think about how to include
    #       historical data, as that will also be vital for my purposes.

    data_dict = {}
    
    for item in r.json()["features"]:
        id = item["properties"]["parameter_code"]
        
        # Grab essential properties
        name = util.id_to_name(id)
        value = item["properties"]["value"]
        unit = util.id_to_unit(id)
        
        try:
            # Add Condition type to dictionary
            data_dict[name] = Condition(
                name=name,
                value=value,
                unit=unit
            )
        except ValidationError:
            return error("Condition could not be computed")
    
    try:
        # Build water conditions model
        conditions = WaterConditions(
            flowRate=data_dict['flow rate'],
            waterTemperature=data_dict['water temperature'],
            waterLevel=data_dict['water level'],
            precipitation=data_dict['precipitation']
        )

    except ValidationError:
        return error("Conditions could not be properly computed")

    return conditions
