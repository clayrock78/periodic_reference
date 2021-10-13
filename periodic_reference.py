import periodictable as pt
absolute_difference_function = lambda list_value : abs(list_value - given_value)

# Because .isnumeric() returns false for floats, we create this new
# function that will allow us to check for floats
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

while True:
    element = None
    user_input = input("Enter an element, atomic mass (whole number), atomic number (non-whole number), or atomic symbol:")
    if user_input in [ele.name for ele in pt.elements]:
        element = pt.elements.name(user_input)
    elif user_input.capitalize() in [ele.symbol for ele in pt.elements]:
        element = pt.elements.symbol(user_input.capitalize())
    elif user_input.isnumeric():
        element = pt.elements[int(user_input)]
    elif is_number(user_input):
        given_value = float(user_input)
        mass_list = [ele.mass for ele in pt.elements]
        closest_value_index = mass_list.index(min(mass_list, key=absolute_difference_function))
        element = pt.elements[closest_value_index]
    else:
        print(' '* 5 + 'Invalid Input')
    
    if element != None :
        print(' '* 5 + element.symbol + ' - ' + element.name.capitalize())
        print(' '* 5 + "Atomic mass : " + str(element.mass))