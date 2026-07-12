import math

# INPUT
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

# PROCESSING
# Calculate BMI
BMI = math.floor(weight / (height * height))

# OUTPUT
print("You weigh " + str(weight) + "kgs" + " and your height is " + str(height) + " meters!")

if BMI < 18.5:
  print("Underweight: BMI=" + str(BMI) + " < 18.5")
elif 18.5 <= BMI < 25.0:
  print("Healthy Weight: BMI=" + str(BMI) + " <= 18.5 < 25.0")
else:
  print("Obese: BMI=" + str(BMI) + " >= 30.0")



