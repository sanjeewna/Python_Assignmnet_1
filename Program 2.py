def square_meters_to_square_feet(area_sq_meters):
    #Defining function_name(Parameters)
    #1 square meter is equal to approximately 10.7639 square feet
    square_feet = area_sq_meters * 10.7639
    return square_feet
    #Return:It calculates the square_feet and return the result

if __name__ == "__main__":
    # Input area in square meters
    area_sq_meters = float(input("Enter the area of a house in square meters: "))

    # Convert square meters to square feet
    area_sq_feet = square_meters_to_square_feet(area_sq_meters)

    # Print the result up to two decimal points(i.e=.2f)
    print(f"The area of the house is {area_sq_feet:.2f} square feet.")