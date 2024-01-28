#The program will work accordingly.

#It prompts the user to enter the length of the zander in centimeters.
#It checks if the length of the zander meets the size limit (42 centimeters).
#If the zander meets the size limit, it prints nothing the fisher.
#If the zander doesn't meet the size limit, it calculates how many centimeters below the size limit the zander is and prompts the fisher to release the fish back into the lake.


def check_zander_size(length_cm):
    if length_cm >= 42:
        return True
    else:
        return False

if __name__ == "__main__":
    # Ask the fisher for the length of the zander
    length_of_zander = float(input("Enter the length of the zander in centimeters: "))

    # Check if the zander meets the size limit
    if check_zander_size(length_of_zander):
        print("Nothing")
    else:
        # Calculate how many centimeters below the size limit the zander is
        centimeters_below_limit = 42 - length_of_zander
        print(f"The zander does not meet the size limit. Release the fish back into the lake.")
        print(f"It was {centimeters_below_limit:.2f} centimeters below the size limit.")





