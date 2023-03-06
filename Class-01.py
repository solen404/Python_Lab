# This is Class-01 File 

# My First code.

print("------------------------- My First Python Code ----------------------- ")

print('Hello World')
print('Well Come To Craftnowledge.net')
print ('Hello Student This is Our First Python code')

# Python Comment
print("------------------------- Python Comment----------------------- ")

 
    # Comments are lines that exist in computer programs that are ignored by compilers and interpreters.

    # Two Type of Comment in Python
        # starts with #,
    # 1.Single line comment Comments 

    # 2.Multiline Comments
        #To add a multiline comment you could insert a # for each line:
       # or
       #Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code,
    # The main function will parse arguments via the parser variable.  These
    # arguments will be defined by the user on the console.  This will pass
    # the word argument the user wants to parse along with the filename the
    # user wants to use, and also provide help text if the user does not
    # correctly pass the arguments.
line=""" 
    This is a comment
    written in
    more than just one line
"""
print(line,"This is Multiline comment")

# Variable And Assignment
print("------------------------- Variable And Assignment ----------------------- ")


Name='ICraft'
Age=14
price=200.34
is_Paid=True

print(Name)
print(Age)
print(price)
print(is_Paid)


# Data Type
print("Python Data Type ")

# 1. Text Type: String (str)
print("------------------------- String Data Type ----------------------- ")
str = 'Hello World!'
print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

# 2. Numeric Types:

# A. int (Integer)
print("------------------------- Python Integer Data Type ----------------------- ")


int_1 = 0
int_2 = 100
int_3=-10
int_4= 1234567890

print(int_1)
print(int_2)
print(int_3)
print(int_4)

# B. float
print("------------------------- Python Float Data Type ----------------------- ")


float_1=1234.56
float_2=3.142
float_3=- 1.55
float_4=0.23

print(float_1)
print(float_1)
print(float_1)
print(float_1)

# C. Complex
print("------------------------- Python Complex Data Type ----------------------- ")
complex__num = 5 + 6j

# 3.Sequence Types:

# A. Python List
print("------------------------- Python List Data Type ----------------------- ")


Student_List= ["Abebe","Kebed","Chala"]
print(Student_List[0])
print(Student_List[1])
print(Student_List[2])
print(Student_List)

# B. Python Tuple
print("------------------------- Python Tuple Data Type ----------------------- ")

names_tuple = ('Abebe', 'Kebed', 'Chala') # string tuple
print(names_tuple[0])
print(names_tuple[1])
print(names_tuple[2])
print(names_tuple)

print ('---------------------The Different of Tuple and  List --------------------')

# names_tuple[0]='new_data'
Student_List[0]='new_data'
print(names_tuple)
print(Student_List)
 
# C. Python Dictionary:
print("------------------------- Python Dictionary ----------------------- ")

capitals = {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}
print(capitals['USA'])
print(capitals['France'])
print(capitals['India'])
print(capitals)

# 4.Python Boolean Data type 
print("------------------------- Python Boolean Data type  ----------------------- ")
print(10 > 9)
print(10 == 9)
print(10 < 9)


# Python Operators

print("------------------------- Python Operators  ----------------------- ")

# a. Addition Operators
print("------------------------- Python Addition Operators  ----------------------- ")
x=5; y=10
z=x + y 
print(z)
import operator
z=operator.add(x, y)
print(z)

# b. Subtraction Operators
print("------------------------- Python Subtraction Operators  ----------------------- ")

x=5; y=10
z=x - y 
print(z)
import operator
z=operator.sub(x, y)
print(z)

# c. Multiplication   Operators
print("------------------------- Python Multiplication  Operators  ----------------------- ")

x=5; y=10
z=x * y 
print(z)
import operator
z=operator.mul(x, y)
print(z)

# d. Division Operators
print("------------------------- Python Division  Operators  ----------------------- ")
x=5; y=10
z=x / y 
print(z)
import operator
operator.truediv(6, 3)
print(z)

# e. Modulus Operators
print("------------------------- Python Modulus Operators  ----------------------- ")
x=5; y=10
z=x % y 
print(z)
import operator
operator.mod(6, 3)
print(z)

# f. Exponentiation Operators
print("------------------------- Python Exponentiation  Operators  ----------------------- ")
x=5; y=10
z=x ** y 
print(z)
import operator
operator.pow(6, 3)
print(z)


# g. Floor division Operators
print("------------------------- Python Floor Division Operators  ----------------------- ")
x=5; y=10
z=x // y 
print(z)
import operator
operator.floordiv(6, 3)
print(z)

# Floor division with negative numbers
print(-15 // 4)

# Operator Precedence
print("------------------------- Python  Operator Precedence ----------------------- ")

print(43 + 13 − 9/3 ∗ 7)