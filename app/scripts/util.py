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
