# No AI program was used as help this assignment

# Function to input files
def input_files():
    # Prompt for sample input file
    user_input_file = input('Please enter the name of the input data file: ')

    # Check if the sample input file exists
    check_input = '0'
    while check_input != '1':
            try:
                sample_input = open(user_input_file, 'r')
                check_input = '1'

            # Exception for if the file is not found, reprompt
            except FileNotFoundError:
                print(f"The file {user_input_file} could not be found or opened. Please try again.")
                check_input = '0'
                user_input_file = input('Please enter the name of the input data file: ')

    # Prompt for sample output file
    user_output_file = input('Please enter the name of the output data file: ')
    sample_output = open(user_output_file, 'w')
    return sample_input, sample_output

# Define curve function
def curve():
    # Input curve amount
    curve_grade = input("Would you like to curve the grades? (Y/N) ")

    # Validate answer to be either Y or N
    if (curve_grade != "Y") and (curve_grade != "N"):
        print("Error. Please input Y for yes or N for no.")
        curve_grade = input("Would you like to curve the grades? (Y/N) ")

    # Continue program after validation
    else:

        # If Y:
        if curve_grade == "Y":
            curve_value_check = '0'
            while curve_value_check != 1:
                try:

                    # Input curve amount
                    curve_value = float(input("Please enter the score that should map to a '100%' grade: "))

                    # Check that the curve amount makes logical sense (between zero and one hundred)and revalidate
                    if curve_value <= 0 or curve_value >= 100:
                        while curve_value <= 0 or curve_value >= 100:
                            print("Error: Please input a numeric value between 0 and 100")
                            curve_value = float(input("Please enter the score that should map to a '100%' grade: "))

                    # Calculate curve
                    curve_value = float(100/(curve_value))
                    curve_value_check = '1'
                    return curve_value

                # Exception for if a numeric value between zero and one hundred is not found
                except ValueError:
                    print("Error. Please input a numeric value.")
                    curve_value_check = '0'

        # If N:
        else:

            # Set curve value to 1
            curve_value = 1
            return curve_value

# Define function for processing files
def process_files(sample_input, sample_output):

    # Call curve function
    curve_value = curve()

    # Read first line (first line of both the file and of the set of three (age/grade level))
    # The variable age_line will be referred to the line that holds GRAD/UNDERGRAD/ETC
    age_line = sample_input.readline().rstrip('\n')

    # Check if first line is empty
    if age_line == '':
                # Print successful note
                print("All data was successfully processed and saved to the requested output file.")
    else:
    # If first line does not say GRAD or UNDERGRAD:
        while age_line != '':
            if (age_line != "UNDERGRAD") and (age_line != "GRAD"):
                print("Unknown student category detected (", (str(age_line)), ").")

                # End program if unknown category found
                print("Error occurred while determining letter grade. Aborting.")

                # End program
                age_line = ''

            # Process info for UNDERGRAD and GRAD students students
            else:
                # If age_line is for an undegrad student:
                if age_line == "UNDERGRAD":

                    # Read second line (name)
                    name_line = sample_input.readline().rstrip('\n')

                    # Print name and space in output file
                    sample_output.write(name_line)
                    sample_output.write("\n")

                    # Read third line (grade)
                    grade_line = float(sample_input.readline())

                    # Apply curve
                    grade_line *= curve_value

                    # Assign letter grade and write letter in output
                    if grade_line >= 90:
                        sample_output.write("A")
                    elif grade_line >= 80:
                        sample_output.write("B")
                    elif grade_line >= 70:
                        sample_output.write("C")
                    elif grade_line >= 60:
                        sample_output.write("D")
                    else:
                        sample_output.write("F")

                # If age_line is for an undegrad student:
                elif age_line == "GRAD":

                    # Read second line (name)
                    name_line = sample_input.readline().rstrip('\n')

                    # Print name and space in output file
                    sample_output.write(name_line)
                    sample_output.write("\n")

                    # Read third line (grade)
                    grade_line = float(sample_input.readline())

                    # Apply curve
                    grade_line *= curve_value

                    # Assign letter grade and write letter in output
                    if grade_line >= 95:
                        sample_output.write("H")
                    elif grade_line >= 80:
                        sample_output.write("P")
                    elif grade_line >= 70:
                        sample_output.write("L")
                    else:
                        sample_output.write("F")

                # Write space
                sample_output.write("\n")

                # Read next line
                age_line = sample_input.readline().rstrip('\n')

                # End processing if program reaches an empty line
                if age_line == '':

                # Print successful note
                    print("All data was successfully processed and saved to the requested output file.")

# Define function to close files
def close_files(sample_input, sample_output):

    # Close input file
    sample_input.close()

    #Close output file
    sample_output.close()

# Define main function
def main():   
    # Get user input for files

    # Get sample_input and sample_output from input_files() function
    sample_input, sample_output = input_files()

    # Process files
    process_files(sample_input, sample_output)

    # Close files
    close_files(sample_input, sample_output)
    
# Call main.
main()