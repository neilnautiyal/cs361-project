#  compare_the_weather.py
#  This file contains the implementation for the compare the weather widget

def compare_the_weather():
    """
    This app allows the user to check the weather for the entered location
    :return:
    """
    weather_data = {
        "new york": [72, "Sunny"],
        "los angeles": [85, "Clear"],
        "chicago": [60, "Partly Cloudy"],
        "houston": [88, "Sunny"],
        "miami": [82, "Rainy"],
        "san francisco": [68, "Foggy"],
        "seattle": [62, "Cloudy"],
        "denver": [70, "Partly Cloudy"],
        "boston": [75, "Sunny"],
        "las vegas": [90, "Sunny"]
    }

    user_input = " "
    city1 = ""
    temp1 = ""
    conditions1 = ""
    while user_input:  # While user input is invalid, keep looping
        user_input = input("Enter the first city you'd like to check the weather for or leave blank to return to main menu: ").lower()
        if user_input in weather_data:
            city1 = user_input.title()
            temp1 = weather_data[user_input][0]
            conditions1 = weather_data[user_input][1]
            break
        elif user_input == "":
            return
        else:
            print("Data currently missing. Try another city...")

    user_input = " "
    while user_input:  # While user input is invalid, keep looping
        user_input = input("Enter the second city you'd like to check the weather for or leave blank to return to main menu: ").lower()
        if user_input in weather_data:
            city2 = user_input.title()
            temp2 = weather_data[user_input][0]
            conditions2 = weather_data[user_input][1]
            print("City 1: ", city1, " | City 2: ", city2)
            print("Temperature (F) 1: ", temp1, " | Temperature (F) 2: ", temp2)
            print("Conditions 1: ", conditions1, " | Conditions 2: ", conditions2)
            print("")
            break
        elif user_input == "":
            return
        else:
            print("Data currently missing. Try another city...")
    return
