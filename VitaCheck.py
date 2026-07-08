# #Functions
# def weight_input():
#   try:
#     weight = int(input("Please enter your weight in Kgs (between 0-200) "))
#     type(weight) == int and weight >= 0 and weight <= 200
#     return weight
#   except: 
#     print("Please enter a valid weight input (Must be a number and within the specified range)")
#     weight_input()

# Weight input validation
while True: 
  try:
    weight = float(input("Enter your weight in kilograms (between 0-200) "))
    break
  except ValueError:
    print("Invalid input!")

while True: 
  try:
    height = float(input("Enter your height in meters (between 0-3) "))
    break
  except ValueError:
    print("Invalid input!")
# Processing

# Output
print("You weigh " + str(weight) + "kgs" + " and your height is " + str(height) + " meters!")

