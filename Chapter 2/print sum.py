num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
sum = (num1 + num2)/2
print ("sum of numbers", sum)

#Requirements:Write a Python program that does the following:
# Input & Inspection:Prompt the user to enter two raw inputs (Input A and Input B).
# Keyword Validation:Check if either of the raw input strings matches a Python reserved keyword (use keyword.iskeyword()).
#  If it is a keyword, inform the user that it is a reserved word in Python.
# Smart Type Casting:Try to convert Input A and Input B into integers or floats automatically:
# If both can be numbers, print their Sum ($A + B$) and their Product ($A \times B$).If they are text/strings, 
# concatenate them together with a hyphen (-) in between.Data 
# Type Breakdown:Display the initial data type (type()) of the inputs when first read versus their data type after casting.
import keyword
print(keyword.kwlist)

import keyword
#step 1:
input_a =input("enter the value of variable a:")
input_b =input("enter the value of the variable b:")
#step 2:
if (keyword.iskeyword((input_a))):
    print(f"Yes , {input_a} is a reserved keyword")
else:
    print(f"NO, {input_a} is not a reserved keyword")  
if (keyword.iskeyword(input_b)):
    print(f"yes {input_b} is a reserved keyword:")
else:
    print(f"No, {input_b} is not a reserved keyword:")   
#step 3:
input_a = print(f"the value you entered is integer {type(input_a)}")
input_b = print(f"the value you entered is integer {type(input_b)}")

#step 4:
print("---result----")
if isinstance(input_a, (int,float)) and isinstance(input_b, (int,float)):
    sum = input_a + input_b
    product= input_a*input_b
    print(f"the sum of two numbers is {input_a} + {input_b} = {sum}")
    print(f"the product of two numbers is {input_a} * {input_b} = {product}")
else: 
    print(f"the concatenation of two strings is {input_a} - {input_b}")

