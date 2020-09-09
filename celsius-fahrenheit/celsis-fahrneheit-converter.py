def print_celsius_values_with_signature(celsius):
    if celsius > 0:
        print("The celsius value you entered is positive")
    elif celsius == 0:
        print("The celsius value you entered is zero")
    else:
        print("The celsius value you entered is negative")


def compute_fahrenheit(celsius):
    result = 9 / 5 * celsius + 32
    return result


def parse_input():
    try:
        return float(input("Enter a Temperature in Celsius to convert it to Fahrenheit: \n"))
    except ValueError as e:
        print("--- ZYou have entered an invalid number. ---")
        exit(-1)


def main():
    celsius = parse_input()
    print_celsius_values_with_signature(celsius)
    fahrenheit = compute_fahrenheit(celsius)
    print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' % (celsius, fahrenheit))


main()
