from time import sleep

#random

def main_calculator():

    print("")
    print("Choose what you need: +, *, -, /")
    print("Exit Calculator: -done")
    print("")
    user_calculator = input("User: ")
    sleep(1)

    if user_calculator == "+":
        print("")
        Z1 = int(input("Number 1: "))
        Z2 = int(input("Number 2: "))
        print("")

        result_0 = (Z1+Z2)

        print("The Result Is: ", result_0)
        print("")
        sleep(1)
        return main_calculator()

    if user_calculator == "-":
        print("")
        Z3 = int(input("Number 1: "))
        Z4 = int(input("Number 2: "))
        print("")

        result_1 = (Z3-Z4)

        print("The Result Is: ", result_1)
        print("")
        sleep(1)
        return main_calculator()

    if user_calculator == "*":
        print("")
        Z5 = int(input("Number 1: "))
        Z6 = int(input("Number 2: "))
        print("")

        result_2 = (Z5*Z6)

        print("The Result Is: ", result_2)
        print("")
        sleep(1)
        return main_calculator()

    if user_calculator == "/":
        print("")
        Z7 = int(input("Number 1: "))
        Z8 = int(input("Number 2: "))
        print("")

        result_3 = (Z7*Z8)

        print("The Result Is: ", result_3)
        print("")
        sleep(1)
        return main_calculator()

    elif user_calculator == "-done":
        print("")
        print("")
        print("")
        print("")

    else:
        print("")
        print("Not found: " + user_calculator)
        sleep(1)
        return main_calculator()

main_calculator()

def main_weather_calculator():
    print("")
    print("Choose what you need: Kelvin/Fahrenheit")
    print("")

    user_1 = input("User: ")

    if user_1 == "Fahrenheit":
        print("")
        print("Celsius to Fahrenheit")
        print("")
        sleep(1)
        Celsius = int(input("Celsius: "))
        Fahrenheit = (Celsius + 1.8 + 32)
        sleep(1)
        print("Fahrenheit: " + str(Fahrenheit))
        print("")
        sleep(1)
        return main_weather_calculator()

    if user_1 == "Kelvin":
        print("")
        print("Celsius to Kelvin")
        print("")
        sleep(1)
        Celsius2 = int(input("Celsius: "))
        Kelvin = (Celsius2 + 273.15)
        sleep(1)
        print("Kelvin: " + str(Kelvin))
        print("")
        sleep(1)
        return main_weather_calculator()

    else:
        print("")
        print("Not found: ", user_1)
        print("")
        sleep(1)
        return main_weather_calculator()


main_weather_calculator()
