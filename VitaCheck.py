# Weight input validation
while True: 
  try:
    weight = float(input("Enter your weight in kilograms (between 0-200) "))
    # Check if the weight is within the valid range
    if 0 <= weight <= 200:
      break
    else:
      print("Out of range!")
  except ValueError:
    print("Invalid input!")

# Height input validation
while True: 
  try:
    height = float(input("Enter your height in meters (between 0-3) "))
    # Check if the height is within the valid range
    if 0 <= height <= 3:
      break
    else:
      print("Out of range!")
  except ValueError:
    print("Invalid input!")

# Processing

# Output
print("You weigh " + str(weight) + "kgs" + " and your height is " + str(height) + " meters!")

