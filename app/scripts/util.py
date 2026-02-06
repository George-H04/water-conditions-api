"""
Basic utility helper functions with a variety of responsibilities
"""

from .. import constants


def c_to_f(temp: float) -> float:
    return (float(temp) * 1.8) + 32


def f_to_c(temp: float) -> float:
    return (float(temp) - 32) / 1.8


def id_to_name(id: int) -> str:
    return constants.USGS_IDS[id]


def id_to_unit(id: int) -> str:
    return constants.UNITS[id]


def find_locations(location: tuple[int, int], radius: int) -> list[str]:
    """
    Algorithm that finds nearby locations to query for conditions

    :param location: The user's current location, or an alternatively specified location
    :type location: tuple[int, int]
    
    :param radius: The search radius
    :type radius: int
    
    :return: Returns a list of strings, where each element is the monitoring location's ID
    :rtype: list[str]
    """
    pass

    # TODO: Specifically, must add all monitoring locations to a database, so that the API queries the DATABASE, NOT external APIs.
    #       The goal is to reduce API calls as much as possible---if I can cache, I cache. If I can store in a databse, I do just that.

def store() -> None:
    pass

    # TODO: The specific function for storing something in my future database.
    #       Will utilize SQLAlchemy I suppose, but this is part of the next phase.
