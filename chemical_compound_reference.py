import periodictable as pt
import csv

while True:
    formula = input("Input formula or chemical name: ")

    with open("list_of_chemical_formulas-1246j.csv", newline="") as file:
        compounds = csv.reader(file)
        found = False
        for compound in compounds:

            if formula in compound:
                # Search for chemical compund 
                found = True
                chem_formula = compound[0]
                chem_name = compound[1]
                compound = pt.formula(chem_formula)

                # Printing Compound Properties
                print(f"\n\tChemical Compound = {compound} ({chem_name})")
                print(f"\tMolar Mass = {compound.mass}")
                print("\tComposition (by mass):")
                # Printing Percent Composition
                CMF = {k: v for k,v in sorted(compound.mass_fraction, key=lambda item: item[1])}
                align = ""
                padding = max(len(element.name) for element in CMF)
                for element in CMF:
                    print(f"\t\t{element.name:{align}{padding}}: {round(CMF[element]*100,3)}%")

                print("\n")
                break

        if not found:
            print("Chemical compound not found. Did you enter it correctly?\n\n")
