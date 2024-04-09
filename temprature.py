def convert_temprature(value, from_unit, to_unit):
    if from_unit =="Celcius" and to_unit =="Farenheit":
        return (value*9/5) + 32, "Farenheit"
    elif from_unit =="Farenheit" and to_unit =="Celcius":
        return (value - 32) * 5/9, "Celcius"
    else:
        return "Invalid Comversion"
    

    