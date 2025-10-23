# calculator.py
# Program to perform addition, subtraction, multiplication, and division of two numbers

# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Operations
sum_result = num1 + num2
diff_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

# Display results
print("Addition:", sum_result)
print("Subtraction:", diff_result)
print("Multiplication:", mul_result)
print("Division:", div_result)