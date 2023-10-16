def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def get_valid_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius): "))
            if choice in [1, 2]:
                return choice
            else:
                print("Invalid choice. Please select 1 or 2.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_temperature():
    while True:
        try:
            value = float(input("Enter the temperature value: "))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def temperature_converter():
    print("Temperature Converter")
    choice = get_valid_choice()
    value = get_valid_temperature()

    if choice == 1:
        result = celsius_to_fahrenheit(value)
        print(f"{value}°C is equal to {result}°F")
    else:
        result = fahrenheit_to_celsius(value)
        print(f"{value}°F is equal to {result}°C")

if __name__ == "__main__":
    while True:
        temperature_converter()
        another_conversion = input("Do you want to perform another conversion? (yes/no): ")
        if another_conversion.lower() != "yes":
            break
