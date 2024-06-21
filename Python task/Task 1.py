# Calculate Area with Conditions
def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width

# Input values for length and width from the user
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# Calculate and display the area or the message
result = calculate_area(length, width)
print(result)
