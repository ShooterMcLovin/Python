from typing import Union


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[float]:

    bmis = []
    for h, w in zip(height, weight):
        if h > 0:
            bmi = w / (h * h)
            bmis.append(bmi)
        else:
            bmis.append(None)
    return bmis


def apply_limit(bmi: list[Union[int, float]], limit: int) -> list[bool]:
    limitList = []
    for B in bmi:
        if (B > limit):
            limitList.append(True)
        else:
            limitList.append(False)
    return limitList
