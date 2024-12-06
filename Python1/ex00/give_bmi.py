from typing import Union


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[float]:
    """
    Gives your BMI based on height(meters) and weight(kg)
    """
    bmis = []
    for h, w in zip(height, weight):
        if h > 0 and w > 0:
            bmi = w / (h * h)
            bmis.append(bmi)
        else:
            bmis.append(None)
    return bmis


def apply_limit(bmi: list[Union[int, float]], limit: int) -> list[bool]:
    """
    Gives list of BMIs based on threshold(limit)
    """
    limitList = []
    for B in bmi:
        if (B > limit):
            limitList.append(True)
        else:
            limitList.append(False)
    return limitList
