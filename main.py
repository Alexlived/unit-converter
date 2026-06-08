import pick
conversions = {
    "Temperature": ["Fahrenheit", "Celsius"],
    "Length" : ["Inch", "Foot", "Yard", "Mile",
                "Milimiter","Centimeter","Meter", "Kilometer"],
    "Speed" : ["MPH", "KPH"],
    "Weight" : ["Ounce", "Pound",
                "Miligram", "Gram", "Kilogram"],
    
}


def fetch_type_of_conversion():
    title = "What conversion?"
    options = ["Temperature", "Length", "Speed", "Weight"]
    option, index = pick.pick(options, title)
    return option

def main():
    conversion = fetch_type_of_conversion()
    title = "Conversion"
    x = y = 'What'
    options = [x,y,'calculate']
    while True:
        option, index = pick.pick(options, title)
        if index == 3:
            if 'What' not in options:
                break
            else:
                pass
        else:
            value, index_v = pick.pick(conversions[conversion], "Unit?")
            options[index] = conversions[conversion][index_v]
            pass
    print(f'How many {x}s to convert into {y}')
    actual_math_input = int(input('>'))
    print(x+y)
        
        
main()
        
        


