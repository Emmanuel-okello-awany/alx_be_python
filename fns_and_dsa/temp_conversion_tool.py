# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    result1 = (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    return result1

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    result2 = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return result2

# Main function for user interaction
def main():
    try:
        # Prompt the user for temperature input
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)  # Convert input to float

        # Prompt the user for the temperature unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == "C":
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Execute the main function
if __name__ == "__main__":
    main()