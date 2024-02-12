def divide(x, y):

  try:
    result = x / y
  except ZeroDivisionError:
    result = "Error: Cannot divide by zero."
  except TypeError:
    result = "Error: Invalid input types."
  return result

while True:
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    break  # Exit the loop if input is valid
  except ValueError:
    print("Invalid input. Please enter numbers only.")

result = divide(num1, num2)
print(result)