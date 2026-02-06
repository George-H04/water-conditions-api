from pydantic import BaseModel


class WaterConditions(BaseModel):
    flowRate: str
    temperature: str
    waterLevel: str
    precipitation: str

    # TODO: I think I want to include variables for confidence as I
    #       begin to include more descriptive and useful variables.
    #       for example, I want to compare to the average, using
    #       historical data.
