# print("true statement") if True else print("false statement")

# username_matched = True
# password_matched = False
# print("Login successful") if username_matched and password_matched else print("Login failed")
# print("Login successful") if username_matched or password_matched else print("Login failed due to incorrect username")

# age = 25
# person="adult" if age>=18 else  "minor"

# login_as="owner"

# won_last_match = False
# total_wins = 4
# net_runrate = 0.6

# if(won_last_match):
#     if(total_wins > 5):
#         if(net_runrate >0.75):
#             print("Team qualifies for the playoffs")
#         else:
#             print("Team does not qualify for the playoffs due to insufficient net run rate")
#     else:
#         print("Team does not qualify for the playoffs due to insufficient wins")
# else:
#     print("Team does not qualify for the playoffs due to loss in last match")       


#terinary operator
#it is also known as conditional expression

# """if(False):
#     print("true statement")
# else:
#     print("false statement")"""


# print("true statement") if True else print("false statement")
# print("true statement") if False else print("false statement")


# username_matched = True
# password_matched = False
# print("login success") if username_matched and password_matched else print("login failed")

# print("login success") if username_matched or password_matched else print("login failed due to incorrect username")   if not username_matched else print("login failed due to incorrect password")


# age=25
# person="adult" if age>=18 else "minor"
# print(person)


login_as="owner"

user="customer" if login_as=='customer'else 'owner'
print(user)

