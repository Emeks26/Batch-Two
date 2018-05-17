#calendar to determine day of the week your next event falls on
#group TESA
#Kazeem Temitope oluwatosintemitope@gmail.com
#Sarafa	Olaleka	sarafaolalekan7@gmail.com

#github: www.github.com/musharaf1

from datetime import date
import datetime, calendar
print("HI! would you like to know what day of the week will your next event fall on?\n")
print("if YES press 1\nif NO press 2\n  ")
x=int(input("select an option\n"))
if x is 1:

    year=int(input("please input the year in view: eg 2012, 2018, 2030 etc  "))
    month=int(input("please input the month: eg 1 for jan., 2 for feb.,etc  "))
    day=int(input("please input day:  "))
    my_date=datetime.datetime(year,month,day)
    day_in_week=calendar.day_name[my_date.weekday()]

    print(day_in_week)
elif x is 2:
    print("why not? it is good to know your next event day. it helps you prepare ahead")
