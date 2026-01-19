# Arithmetic Operators
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\n--- Arithmetic Operations ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# Total and Average
total = a + b
average = total / 2

print("\nTotal:", total)
print("Average:", average)

# # Comparison Operators 

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("\n--- Comparison Results ---")
print("x > y:", x > y)
print("x < y:", x < y)
print("x == y:", x == y)
print("x != y:", x != y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# # Logical Operators

age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

print("\n--- Eligibility Check ---")

# AND operator
if age >= 18 and marks >= 50:
    print("Eligible for admission")
else:
    print("Not eligible for admission")

# OR operator
if age >= 18 or marks >= 50:
    print("Eligible for special consideration")

# NOT operator
print("Not failed:", not (marks < 40))

# Assignment Operators Example

x = 10
print("Initial value:", x)

x += 5
print("After x += 5:", x)

x -= 3
print("After x -= 3:", x)

x *= 2
print("After x *= 2:", x)

x /= 4
print("After x /= 4:", x)

x %= 3
print("After x %= 3:", x)
