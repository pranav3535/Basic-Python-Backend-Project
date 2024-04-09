from length import convert_length
from temprature import convert_temprature

def unit_converter():
    while True:
        conversion_type = input("Enter Conversion Type (length/temprature/quit) : ")
        if conversion_type == "quit":
            print("Exiting Conversion")
            break
        

        value = float(input("Enter the Value to Be Converted: "))
        from_unit = input("from unit: (Meter/Feet/Celcius/Farenheit)")
        to_unit = input("to unit: (Meter/Feet/Celcius/Farenheit)")

        if conversion_type == "length":
            result, unit= convert_length(value, from_unit, to_unit )
        elif conversion_type =="temprature":
            result, unit= convert_temprature(value, from_unit, to_unit)
        else:
            return "Invalid Conversion Type!!"
            continue
        

        print(f"Converted Value: {result} {unit}")


unit_converter()