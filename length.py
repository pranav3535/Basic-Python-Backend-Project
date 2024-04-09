def convert_length(value, from_unit, to_unit):
    if from_unit =="Meter" and to_unit =="Feet":
        return value * 3.28084, "Feet"
    elif from_unit =="Feet" and to_unit =="Meter":
        return value/ 3.28084, "Meter"
    else: return "Invalid Length conversion"


