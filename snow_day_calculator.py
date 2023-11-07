# snow_day_calculator.py
# This file contains the implementation for the snow day calculator widget

import random

def snow_day_calculator():
    """
    prints the chances of a snow day for a given city
    :return:
    """
    snow_day_chance = random.randint(1, 100)
    city = input("Enter the city you'd like to check for the chance of a snow day tomorrow: ")
    if city == "":
        return
    else:
        print("The chance of a snow day in", city, "is", str(snow_day_chance)+"%")
