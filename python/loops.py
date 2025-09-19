"""loop--->
shouid start from one FloatingPointErrorlkg
ukg
.
.
.
ug/pg 
end at one point"""


#looping statement;
#set of statement will executes multiple times in a loop until a sepefic condition 
#reach.
#to starting value and ending value. this can be achive with help of
#predefined method range().

#for loop
#while loop

# for loop

# for x in range():
#     stat1
#     stat2
#     stat3

# for x in range (1,10):
#     print("hello world")
#     print(x)


# for x in range(2,11):
#     print(f"2x{x}={2*x}")

#     for i in range(20,51):
#         if(i%3==0):
#             print(i)


# print num from 10 to 40
#if num is divisible by 3 then print num-fizz
#if num is divisible by 5 then print num


# for y in range(10,41):
#     if(y%3==0):
#         print(f"{y}-fizz")
#     elif(y%5==0):
#         print(f"{y}-buzz")
#     elif(y%3==0):
#         print(f"{y}-fizz")        

# 1 t0 10
# 10 t0 1


# for x in range(10,0,-1):
#     print(x)

# str="fullstack"
# print(str[0])
# print(str[1])
# print(str[2])

# str="fullstack"
# for x in str:
#     print(x)

    # li=['hi','hello','some','thing']

    # for x in li:
    #     print(f"{x}-hi")

str="something"

for x in range(0,len(str),3):
    print(str[x])

    #1st-->x=0
    #2nd-->x=1

    # range-->single arg--->

    # str="something"
    # for x in range(len(str)-1,-1,-1):
    #     print(str[x])

ip="hello"

#hw to print
# o
# l
# l 
# e 
# h 

op="hello"
for x in range(len(ip)-1,-1,-1):
    op+ip[x]
    print(op)