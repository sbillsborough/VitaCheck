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

