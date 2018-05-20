# NAME; KAYODE SHITTU, PROJECT NAME; AUTOMATED PROFIT AND LOSS CALCULATOR
# EMAIL; knscode45@yahoo.com, MOBILE NUMBER; 09092167244

display_activity="CALCULATE SALES"
print(display_activity)
unit_price=eval(input("enter price per unit:"))
TQS=eval(input("enter total quantity sold:"))
sales_revenue = unit_price*TQS
print(sales_revenue)
display_act2="CALCULATE COSTS"
print(display_act2)
unit_costs=eval(input("enter cost per unit:"))
TQP=eval(input("enter total quantity purchased:"))
other_costs=eval(input("enter other costs:"))
total_costs=(unit_costs*TQP)+ other_costs
print(total_costs)
display_act3="SALES LESS COSTS"
print(display_act3)
business_outcome=sales_revenue-total_costs
print(business_outcome)
outcome_interpreted=["PROFIT", "BREAKEVEN", "LOSS"]
if sales_revenue > total_costs:
 print(outcome_interpreted[0:1])
elif sales_revenue==total_costs:
 print(outcome_interpreted[1:2])
else:
 print(outcome_interpreted[2:3])
