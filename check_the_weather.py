#  check_the_weather.py
#  This file contains the implementation for the check the weather widget

def check_the_weather():
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
    while user_input:  # While user input is invalid, keep looping
        user_input = input("Enter the city you'd like to check the weather for or leave blank to return to main menu: ").lower()
        if user_input in weather_data:
            city = user_input.title()
            temp = weather_data[user_input][0]
            conditions = weather_data[user_input][1]
            print("City: ", city)
            print("Temperature (F): ", temp)
            print("Conditions: ", conditions)
            print("")
        elif user_input == "":
            return
        else:
            print("Data currently missing. Try again later...")