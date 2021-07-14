

def convert_units(og_units:str, distance:int, ending_units:str) -> str:
    ''' This function will allow the conversion of any unit of distance to any other unit of distance '''
    units = {
        'feet': 0.3048,
        'miles': 1609.34,
        'meters': 1,
        'kilometer': 1000,
        'yards': 0.9144,
        'inches': 0.0254,
    }
    
    og_units = og_units.lower()
    ending_units = ending_units.lower()
    distance = int(distance)

    if og_units not in units or ending_units not in units:
        return f'''
        There seems to be an error where your unput of {og_units} 
        and/or {ending_units} was not in the list of acceptable units.'''
    
    elif og_units != 'meters': # checks if needs to be converted to meters
        return f'{distance} {og_units} is {(distance*units.get(og_units))/units.get(ending_units)} {ending_units}.'
    elif og_units == 'meters': # if no need to convert, run the below equation
        return f'{distance} {og_units} is {distance/units.get(ending_units)} {ending_units}.'


unit1 = input('starting units: ')
dist = input('distance to convert: ')
unit2 = input('units to convert to: ')
print(convert_units(unit1, dist, unit2))