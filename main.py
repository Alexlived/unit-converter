
import pick
conversions = {
    "Temperature": ["Fahrenheit", "Celsius"],
    "Length" : ["Inch", "Foot", "Yard", "Mile",
                "Milimiter","Centimeter","Meter", "Kilometer"],
    "Speed" : ["MPH", "KPH"],
    "Weight" : ["Ounce", "Pound",
                "Miligram", "Gram", "Kilogram"],   
}

formulas = {
    "FahrenheitCelsius": lambda f: (f - 32) * 5/9,
    "CelsiusFahrenheit": lambda c: (c * 9/5) + 32,
    
    "InchFoot": lambda x: x / 12,
    "InchYard": lambda x: x / 36,
    "InchMile": lambda x: x / 63360,
    "InchMilimiter": lambda x: x * 25.4,
    "InchCentimeter": lambda x: x * 2.54,
    "InchMeter": lambda x: x * 0.0254,
    "InchKilometer": lambda x: x * 0.0000254,
    
    "FootInch": lambda x: x * 12,
    "FootYard": lambda x: x / 3,
    "FootMile": lambda x: x / 5280,
    "FootMilimiter": lambda x: x * 304.8,
    "FootCentimeter": lambda x: x * 30.48,
    "FootMeter": lambda x: x * 0.3048,
    "FootKilometer": lambda x: x * 0.0003048,
    
    "YardInch": lambda x: x * 36,
    "YardFoot": lambda x: x * 3,
    "YardMile": lambda x: x / 1760,
    "YardMilimiter": lambda x: x * 914.4,
    "YardCentimeter": lambda x: x * 91.44,
    "YardMeter": lambda x: x * 0.9144,
    "YardKilometer": lambda x: x * 0.0009144,
    
    "MileInch": lambda x: x * 63360,
    "MileFoot": lambda x: x * 5280,
    "MileYard": lambda x: x * 1760,
    "MileMilimiter": lambda x: x * 1609344,
    "MileCentimeter": lambda x: x * 160934.4,
    "MileMeter": lambda x: x * 1609.34,
    "MileKilometer": lambda x: x * 1.60934,
    
    "MilimiterInch": lambda x: x / 25.4,
    "MilimiterFoot": lambda x: x / 304.8,
    "MilimiterYard": lambda x: x / 914.4,
    "MilimiterMile": lambda x: x / 1609344,
    "MilimiterCentimeter": lambda x: x / 10,
    "MilimiterMeter": lambda x: x / 1000,
    "MilimiterKilometer": lambda x: x / 1000000,
    
    "CentimeterInch": lambda x: x / 2.54,
    "CentimeterFoot": lambda x: x / 30.48,
    "CentimeterYard": lambda x: x / 91.44,
    "CentimeterMile": lambda x: x / 160934.4,
    "CentimeterMilimiter": lambda x: x * 10,
    "CentimeterMeter": lambda x: x / 100,
    "CentimeterKilometer": lambda x: x / 100000,
    
    "MeterInch": lambda x: x / 0.0254,
    "MeterFoot": lambda x: x / 0.3048,
    "MeterYard": lambda x: x / 0.9144,
    "MeterMile": lambda x: x / 1609.34,
    "MeterMilimiter": lambda x: x * 1000,
    "MeterCentimeter": lambda x: x * 100,
    "MeterKilometer": lambda x: x / 1000,
    
    "KilometerInch": lambda x: x / 0.0000254,
    "KilometerFoot": lambda x: x / 0.0003048,
    "KilometerYard": lambda x: x / 0.0009144,
    "KilometerMile": lambda x: x / 1.60934,
    "KilometerMilimiter": lambda x: x * 1000000,
    "KilometerCentimeter": lambda x: x * 100000,
    "KilometerMeter": lambda x: x * 1000,
    
    "MPHKPH": lambda x: x * 1.60934,
    "KPHMPH": lambda x: x / 1.60934,
    
    "OuncePound": lambda x: x / 16,
    "OunceMiligram": lambda x: x * 28349.5,
    "OunceGram": lambda x: x * 28.3495,
    "OunceKilogram": lambda x: x * 0.0283495,
    
    "PoundOunce": lambda x: x * 16,
    "PoundMiligram": lambda x: x * 453592,
    "PoundGram": lambda x: x * 453.592,
    "PoundKilogram": lambda x: x * 0.453592,
    
    "MiligramOunce": lambda x: x / 28349.5,
    "MiligramPound": lambda x: x / 453592,
    "MiligramGram": lambda x: x / 1000,
    "MiligramKilogram": lambda x: x / 1000000,
    
    "GramOunce": lambda x: x / 28.3495,
    "GramPound": lambda x: x / 453.592,
    "GramMiligram": lambda x: x * 1000,
    "GramKilogram": lambda x: x / 1000,
    
    "KilogramOunce": lambda x: x / 0.0283495,
    "KilogramPound": lambda x: x / 0.453592,
    "KilogramMiligram": lambda x: x * 1000000,
    "KilogramGram": lambda x: x * 1000
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
        if option == 'calculate':
            if 'What' not in options:
                break
            else:
                pass
        else:
            value, index_v = pick.pick(conversions[conversion], "Unit?")
            options[index] = value
            x = options[0]
            y = options[1]
            pass
    print(f'How many {x}s to convert into {y}')
    actual_math_input = float(input('>'))
    conversion_key = x + y
    if x == y:
        result = actual_math_input
    else:
        result = formulas[conversion_key](actual_math_input)
        
    print(f'{actual_math_input} {x} is equal to {result:.2f} {y}')

        
main()

