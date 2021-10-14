"""
This script parses through a CSV file of formulas, compounds, and names
and creates a new, cleaned CSV file to be used in formula_parser.py script

Output looks like:
    formula, chemical name (, optional names)

For example:
    H2O, dihydrogen monoxide, water
"""

def main():
    input_file = "datasets\\raw_source.csv"
    # \/ Source (Not amazing but good enough for this use) \/ 
    # https://www.downloadexcelfiles.com/sites/default/files/docs/list_of_chemical_formulas-1246j.csv

    with open(input_file, "r") as file:

        lines = file.read()
        file.close()

    # * Begin cleaning and writing * #

    # Putting other names on the same line
    lines = lines.replace("\n,",",").split("\n")

    with open("datasets\\chemical_formulas.csv", "w") as write_to:

        # Iterating through source file
        for line in lines:

            line = line.split(",")

            # Removing unwanted things from source file
            new_line = ','.join([term for term in line
                                if not "-" in term and term])
            
            # More removing unwanted things
            if new_line.count(",") > 0 :

                # Writing the line
                spacing = "\n" if line != lines[-1] else ""
                write_to.write(new_line + spacing)

if __name__ == "__main__":
    main()
