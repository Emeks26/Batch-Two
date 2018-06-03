#Adebayo Okanlawon 08077834625
print("Bill Cost of a meal at Jade Palace Chinese Restaurant")

print("Tax on Food and drinks is 5.25%")
print("and tip is 15% of your Meal cost")


cost_of_food =int(input("Enter Cost of Foods: "))
cost_of_drinks =int(input("Enter Cost of Drinks: "))

total_cost= cost_of_food+ cost_of_drinks

tax=4.25/100

tax= tax* total_cost

print("Your tax is",tax)

total = total_cost + tax

print("Your Bill after tax is", total)
    
tip=15*total/100

print("Your tip is", tip)

final_total = total + tip

print("Thank you for your patronage. Please come again. Your bill is:  " +str(final_total))

