"""
Task Completed: Calculator by Me.
"""

print("\n################################ CALCULATOR BY GENOS #################################\n\n")

num1 = input("Enter the first number: ");
print("\n");
num2 = input("Enter the second number: ");
print("\n");
num1 = int(num1);
num2 = int(num2);

# Arithmetic operators in Python
sum = num1 + num2; # Addition operator
sub = num1 - num2; # Subtraction operator
div = num1 / num2; # Divide operator
mul = num1 * num2; # Multiplication operator
exp = num1 ** num2; # Exponential operator
mod = num1 % num2; # Modulus operator (It finds the remainder)

calculate = input("Enter the operation do you want to perform? i.e\nAddition \'+\',  Subtraction \'-\', Multiplication \'*\', Division \'/\', modulus \'%\' or exponent \'**\': ");
print("\n");

if calculate == "+":
    print("Sum of", num1, "and", num2, "is equal to:", sum);

elif calculate == "-":
    print("Difference of", num1, "and", num2, "is equal to:", sub);

elif calculate == "*":
    print("Product of", num1, "and", num2, "is equal to:", mul);

elif calculate == "/":
    print(num1, "divided by", num2, "is equal to:", div);

elif calculate == "**":
    print(num1, "raise to the power", num2, "is equal to:", exp);

elif calculate == "%":
    print("Remainder o", num1, "and", num2, "is equal to:", mod);

else:
    print("Error: Invalid operator");