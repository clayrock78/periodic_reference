"""
WRITTEN BY CLAYTON JONES - October 14, 2021

This script is a utility for chemistry; it provides easy access to information about chemical compounds

Takes in the formula of a compound or the name of it (H2O, water, or dihydrogen monoxide)
and returns relevant information. 

Do with this script what you please.
"""


import periodictable as pt
from fuzzywuzzy import process as find
from colorama import Fore


def print_chemical(compound):
    # Search for chemical compund
    chem_formula = compound[0]
    chem_name = " aka ".join(compound[1:])

    """ 
    Using periodictable to pull extra data we don't have
    i.e. molar mass, percent composition, ect.
    """
    compound = pt.formula(chem_formula)

    # Printing Compound Properties
    print(f"\n\tChemical Compound = {compound} ({chem_name})")
    print(f"\tMolar Mass = {compound.mass} g/mol")
    print("\tComposition (by mass):")

    # Printing Percent Composition
    mass_fractions = compound.mass_fraction
    padding = max(len(element.name) for element in mass_fractions)

    for element in mass_fractions:
        percent_composition = mass_fractions[element] * 100
        mass = compound.mass * mass_fractions[element]
        print(
            f"\t\t{element.name:{padding}}: {percent_composition:.4}% | {mass:.4} grams"
        )

    print("\n")


def main():

    while True:
        printed = False

        user_input = input("Input formula or chemical name: ")

        with open("datasets\\chemical_formulas.csv", newline="") as file:
            compounds = [line.replace("\r\n", "") for line in file.readlines()]
            file.close()

            name_to_properties = {}

            for line in compounds:
                properties = line.split(",")
                cur_formula = properties[0]

                # Catching Formula inputs
                if cur_formula == user_input:
                    print_chemical(properties)
                    printed = True
                    break

                for name in properties[1:]:
                    name_to_properties[name] = properties

            # If we reach this point, then we haven't caught a formula input in the above loop
            # so we are going to look for the closest compound name in the dictionary
            if not printed:

                names = name_to_properties.keys()
                closest_name, confidence = find.extractOne(user_input, names)
                closest_formula = name_to_properties[closest_name]

                if confidence == 100:

                    print_chemical(closest_formula)

                elif confidence >= 90:

                    print(
                        Fore.RED
                        + f"{user_input} was not found; assuming {closest_name}"
                        + Fore.WHITE
                    )
                    print_chemical(closest_formula)

                elif confidence >= 70:

                    print(f"Did you mean {closest_name}?")

                else:
                    print(
                        Fore.RED
                        + "Chemical compound not found. Did you enter it correctly?\n\n"
                        + Fore.WHITE
                    )


if __name__ == "__main__":
    main()
