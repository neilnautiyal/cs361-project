#  ui.py
#  This file contains the code for the user interface for the program

# Import statements
import time
import check_the_weather
import compare_the_weather
import snow_day_calculator

# Functions
def print_menu():
    """
    This function prints the main menu UI that the user can navigate to select their relevant option
    :return:
    """
    print("")
    print("Please Select the widget you would like to use!")
    print("1: Check-the-Weather Widget")
    print("2: Compare-the-Weather Widget")
    print("3: Snow-Day-Calculator Widget")
    print("4: Quit :(")


# Main Menu
valid_inputs = [1, 2, 3, 4]
user_input = 5
print("The Wonderful Weather App!")
print("Check out the README to learn more about the current and upcoming features!")

while user_input:  # While user input is invalid, keep looping
    print_menu()
    user_input = int(input("Select your menu option: "))  # Take user input
    if user_input == 1:  # Option 1: Enter a location to retrieve the weather
        print("")
        check_the_weather.check_the_weather()
        print("")
    elif user_input == 2:  # Option 2: Compare weather for two locations
        print("")
        compare_the_weather.compare_the_weather()
        print("")
    elif user_input == 3:  # Option 3: Snow day calculator
        print("")
        snow_day_calculator.snow_day_calculator()
        print("")
    elif user_input == 4:  # Option 4: Quit Program
        print("")
        print("Goodbye, app will close in 3 seconds")
        print("")
        time.sleep(3)
        break
    else:
        print("")
        print("Please select a valid option")
        print("")
