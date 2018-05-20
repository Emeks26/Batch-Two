# Design to calculate budget
# To recieve user budget for the new month
user_Budget = float(input("please enter your total monthly budget for this month: "))
more_Expenses = 'y'
total_Expenses = 0
while (more_Expenses == 'y'):
    user_Expense = float(input("enter an expense: "))
    total_Expenses = total_Expenses + user_Expense
    more_Expenses = input("do u have more expenses:? type y for yes n for no: ")
    if more_Expenses != 'y':
        more_Expenses = input("do you want to exit? type y to continue or x to exit")
print()

if total_Expenses > user_Budget:
    print("you were over your budget of"+user_Budget+"Naira","by"+total_Expenses - user_Budget,"Naira")

elif user_Budget > total_Expenses:
    print("you were under your budget of " , user_Budget ,"Naira", "by" , user_Budget-total_Expenses,"Naira")

else:
    print("you used your budget of"+user_Budget,"Naira",".")
