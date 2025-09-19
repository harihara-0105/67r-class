# x=5
# print(id(x))
# y=2.5
# print(id(y))
# z='hello'
# print(id(z))
#id() is a predefined method to get the memory id/address of a value/object

# x=5
# y='hello'
# z=True
# c=2.5

# #primitive--->int,float,bool,str


# print(type(x))
# print(type(y))
# print(type(z))
# print(type(c))

# x = 5
# x = 20
# print(id(x))  



# x=5
# y=2.5
# z='hello'
# string:-group of characters enclosed in b/w''or ""
# len() - to find

#what is a variable?

#A variable is like a container that holds data. in python, you dont't need to decalre the type of variable - it's dynamically assigned


# name = "hari"
# age = 23
# height = 5.9
# is_student = True

#common data types in python:


# Type	Example	        Description

# int	25	            Integer numbers
# float	5.9	            Decimal numbers
# str	"Hello"	        Text
# bool	True / False	Boolean values
# list	[1, 2, 3]	   Ordered, mutable collection
# tuple	(1, 2, 3)	   Ordered, immutable collection
# dict	{"a": 1}	   Key-value pair


# print("Name:", name)
# print("Age:", age)
# print("Height:", height)
# print("Student:", is_student)

# x = 10
# print(type(x))  # Output: <class 'int'>

# y = 3.14
# print(type(y))  # Output: <class 'float'>

# z = "python"
# print(type(z))  # Output: <class 'str'>

# my_name = "hari hara reddy"
# my_age = 23
# my_city = "Hyderabad"

# print(type(my_name))
# print(type(my_age))
# print(type(my_city))


ott_data = [ 
{"platform": "Netflix", "shows": ["Stranger Things", "Wednesday"]}, 
{"platform": "Prime", "shows": ["Mirzapur", "Farzi"]}, 
{"platform": "Hotstar", "shows": ["Special Ops", "The Freelancer"]} 
] 

print(ott_data[2]['shows'])
new_dat=ott_data[1]['shows']+['Mirzapur-2']
print(new_dat)
ott_data[1]['shows']=new_dat
print(ott_data[1]['shows'])