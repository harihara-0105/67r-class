# oop
# # # object oriented programing
# # procedural programing  is step by step Process 
#                          ex :step 1 to find next prime len >1
#                              step 2 to do sum of digits of step 1 ans
#                              step 3 check ans of step 2 is prime or not 
#                              here code redundancy increase and no code reusability
#  functional programming 
#              combing group of code in method or function....
#                         #ex: s-1 func: to check prime..
#                              s-2  to get next prime len>1 (we use s-1)
#                             s-3 to sum of digits of ans s-2.
#                             s-4 to check ans s-3 is prime or not (we use s-1)
#                             here we cannot categorise group of functions.
# object oriented programming
# to map our programming lang with real world scenarios, we use oop in code.....
#  to reduce to redundancy
# to reducr reusability
# to abstarct data 
# to combine same type of operations
# to same application in different ways...
# oops:-
# object ; instance of class
# class: 
#    blue print of an object...
# syntax: classs class name:
        #    data...

# object: instance of class....

# syntax: we need create class 
# obj name= class()

# constructor:
#            it is a type of funtion which is initiated when an object is created....

# types of constructor:
#                 1: default constructor
                    # ex: def __init__(self):
                            # pass
#                 2: parameterized constructor
                        # ex def __init__(self,name,marks):

# self: 
#  it is used as reference of the obj data to use in diff methods of our class...
# every method of function's first arugemt is self...
        #  ex: class student:
    #  def newad(self)



# class student():
#     name="hari"
# s1=student()
# print(s1.name)

# class student():
#   def __init__(abcd,name,age):
#     abcd.name=name
#     abcd.age=age
#   def whoisshe(self):
#       print(self.name)
#   def heisage()   

    


# class car:
#     car_brand="bmw"
#     eng=1
#     speed=100
#     mileage=15
#     color="blue"
# car1=car()
# print(car1.color)
# car2=car()
# car3=car()
# car3.color='red'
# print(car3.color)



# class car:
#     car_brand="bmw"
#     eng=1
#     speed=100
#     mileage=15
#     color="red"
#     def __inti__(self,color):
#         # self.eng=eng 
#         # self.speed=speed
#         # self.mileage=mileage
#         self.color=color       
# car1=car("white")
# car2=car("red")
# car3=car("black")
# car3.color='red'
# print(car.color,car2.color)


# class tencoders:
#     batch="67R"
#     def __init__(self,name,course,phone):
#         self.name=name
#         self.course=course
#         self.phone=phone
#         print(f"student {name} admitted")
    
#25/09/2025

# class greeting:
#     def visit(self):
#         print("hello sir")
#     def exit(self):
#         print("thank you visit again")
# g1=greeting()
# g1.exit()

#to crate a class greeting to give the instructions to greeet the customer at vist the shop


# class greeting:
#     def __init__(self,name):
#         self.name=name

#     def visit(self,name):
#         print(f"hello sir {name}")
#     def exit(self):
#         print(f"thank you {self.name}! visit again")
# g1=greeting("sravan")
# g1.visit("Rudra")
# g1.exit()


# Ex

# class clasi:
#     def __init__(self,first,second):
#         self.first=first
#         self.second=second
#     def addition(self):
#         return self.first+self.second
    
#     def substraction





# calsi=calsi(10,20)
# print(calsi.addition())
# print(calsi1.substraction(199,29))


        