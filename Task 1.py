# Calculate Area with Conditions

# Write a Python function calculate_area that takes two parameters: length and width. Itshould calculate and return the area of a rectangle. However, add a condition: if the length
# is equal to the width, return "This is a square!" instead of the area. Then, write a program toinput values for length and width from the user and call the calculate_area function to
# display either the area or the message.

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
