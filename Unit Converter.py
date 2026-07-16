def length_converter():
    print("\n--- Length Converter ---")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    choice = input("Choose option (1-2): ")
    
    if choice == "1":
        m = float(input("Enter meters: "))
        print(f"-> {m} meters = {m * 3.28084:.2f} feet")
    elif choice == "2":
        ft = float(input("Enter feet: "))
        print(f"-> {ft} feet = {ft / 3.28084:.2f} meters")

def weight_converter():
    print("\n--- Weight Converter ---")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Choose option (1-2): ")
    
    if choice == "1":
        kg = float(input("Enter kg: "))
        print(f"-> {kg} kg = {kg * 2.20462:.2f} lbs")
    elif choice == "2":
        lbs = float(input("Enter lbs: "))
        print(f"-> {lbs} lbs = {lbs / 2.20462:.2f} kg")

def temp_converter():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose option (1-2): ")
    
    if choice == "1":
        c = float(input("Enter Celsius: "))
        print(f"-> {c}°C = {(c * 9/5) + 32:.2f}°F")
    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        print(f"-> {f}°F = {(f - 32) * 5/9:.2f}°C")

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        
        choice = input("Select category (1-4): ").strip()
        
        try:
            if choice == "1":
                length_converter()
            elif choice == "2":
                weight_converter()
            elif choice == "3":
                temp_converter()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid numeric value.")

if __name__ == "__main__":
    main()
