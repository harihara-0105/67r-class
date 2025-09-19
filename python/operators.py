#what are operators in python?

# Operators are special symbols that perform operations on variables and values.

# Types of Operators:

# 1. Arithmetic Operators

# Used for mathematical calculations.

# Operator	Description	 Example

# +	      Addition	             3 + 2 → 5
# -	      Subtraction	         5 - 2 → 3
# *	      Multiplication	     2 * 3 → 6
# /	      Division	           6 / 2 → 3.0
# //	  Floor Division	    7 // 2 → 3
# %	      Modulus (remainder)	 7 % 2 → 1
# **	  Exponentiation	     2 ** 3 → 8

# 2. Comparison Operators
# Used to compare values.
# Operator	Description	 Example
# ==	    Equal to	            5 == 5 → True
# !=	    Not equal to	        5 != 3 → True
# >	    Greater than	        5 > 3 → True
# <	    Less than	            3 < 5 → True
# >=	    Greater than or equal	5 >= 5 → True
# <=	    Less than or equal	3 <= 5 → True   

# 3. Logical Operators
# Used to combine conditional statements.
# Operator	Description	 Example
# and	    Returns True if both operands are true	 (5 > 3 and 2 < 4) → True
# or	    Returns True if at least one operand is true	 (5 > 3 or 2 > 4) → True
# not	    Reverses the result of the condition	 not(5 > 3) → False

# 4. Assignment Operators
# Used to assign values to variables.
# Operator	Description	 Example        
# =	    Assigns value to a variable	 x = 5
# +=	    Adds and assigns value	 x += 3 (equivalent to x = x + 3)   
# -=	    Subtracts and assigns value	 x -= 2 (equivalent to x = x - 2)
# *=	    Multiplies and assigns value	 x *= 2 (equivalent to x = x * 2)



# a = 10
# b = 4

# print(a+b)
# print(a ** b)
# print(a > b and b < 5)
# print(not (a == b))

# x = 8
# y = 5
# print("addition:", x + y)
# print("is x even?", x % 2 == 0)
# print("x > 5 and y < 10:", x > 5 and y < 10)


batch_67r={'vamsi','ramakrishna','harsha','jayasree','ramyasree'}
stu='sai'
print(stu in batch_67r)

info={"stu1":"vamsi",
      "stud2":"ramakrishna",
      "stu3":"harsha",
      "stu4":"jayasree",
      "stu5":'ramyasree'}

info1={'stu1':"kiran",'stu2':'ramyasree','stu3':'vamsi'}

print('stu1' in info1)
print('stu2' in batch_67r)
print('harsha' in info.values())
print('stu5' in info)