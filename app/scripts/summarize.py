"""
File that turns retrieved information into an easy to understand summary based
on various criteria and rules. Turns numbers into something actionable.
"""

from models import WaterConditions  # Imports Pydantic models for validation


def create_summary(conditions: WaterConditions):
    # TODO: Here, the goal is to create a smart summary for users.
    #       At first, this will be a simple rule based algorithm
    #       that generalizes to most fishing
    pass
