from pydantic import BaseModel


class Condition(BaseModel):
    """
    Model for the condition type. Used to individually validate each
    condition.
    """

    name: str
    value: float
    unit: str


class WaterConditions(BaseModel):
    """
    Model for water conditions
    """

    flowRate: Condition
    waterTemperature: Condition
    waterLevel: Condition
    precipitation: Condition

    # TODO: I think I want to include variables for confidence as I
    #       begin to include more descriptive and useful variables.
    #       for example, I want to compare to the average, using
    #       historical data.
