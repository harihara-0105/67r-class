#Butterfly Pattern 
# n=int(input("enter n value:"))
# for i in range(n,0,-1):
#     s=" "*(n-i)
#     if i==1:
#         print(""+s+""(i)+s+"")
#     else:
#         if i==n:
#             print("* "+"  "(i-1)+"")
#             print(""+s+" "+"  "(i-2)+""+s+"*")
#         else:
#             print(""+s+" "+"  "(i-2)+""+s+"*")

# for i in range(2,n+1):
#     s=" "*(n-i)
#     """if i==1:
#         print(""+s+" "*(i))
#     else:"""
#     #print(""+s+" "+"  "(i-2)+"")
#     if i==n:
#         print(""+s+" "+"  "(i-2)+""+s+"*")
#         print("* "+"  "(i-1)+"")
#     else:
#         print(""+s+" "+"  "(i-2)+""+s+"*")


# import sys
# # sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
# i=0
# def greeting():
#     global i
#     i+=1
#     print("hi all",i)
#     greeting()


n=5
for i in range(1,n+1):
    S=" "*(n-i)
    if i==1:
        print(S+"* "*(i))
    else:
        print(S+"* "+"  "*(i-2)+"*")




