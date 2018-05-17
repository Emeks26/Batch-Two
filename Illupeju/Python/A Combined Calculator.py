#Asaolu David Babatunde
#asaoludavid234@gmail.com
#08109393720
#Ask the user to enter his or her name
name = str(input("Welcome to Asaolu David's Workspace, Enter your name"))
#Ask the user to define his or her operation
define = print("Welcome {0} kindly state your operation by inputting the number representing the operation,"
                "1 = Simple Arithmetic,  2 = Factorial, 3 = Square root of a number, 4 = Percentage Error,"
                "5 = Quadratic Equation, 6 = Simultaneous Equation, 7 = Loan Calculator and 8 = Plane Shapes" .format(name))

b = int(input("Enter your chosen number"))

if (b==1):
    print("Congrats!!! Simple Arithmetic Selected")
    #Ask user for the numbers
    number1 = float(input("Kindly enter the first number"))
    number2 = float(input("Kindly enter the second number"))
    print("Select one of the options, 1 = Addition, 2 = Subtraction, 3 = Multiplication, 4 = Division and 5 = raise to power")
    d = float(input("Enter the chose number"))
    if (d==1):
        print("Addition of the numbers is", number1 + number2)
    elif (d==2):
        print("Subtraction of the number is", number1 - number2)
    elif (d==3):
        print("Multiplication of the two numbers is,", number1*number2)
    elif(d==4):
        print("Division of the two numbers is,")
        a = number1/number2
        z = round (a,2)
        print(z)
    elif(d==5):
        print(number1, "raise to the power of", number2, "is", number1**number2)
    else:
        print("Invalid operation chosen, check the instruction for details")
        
elif (b==2):
    import time
    time.sleep(1)
    print("Congrats!!! Factorial Selected")
    #Ask the user for the number
    fact = 1
    num =int(input("Enter the number: "))
    while (num>0):
        fact = fact * num
        num = num-1
    print("The factorial is", fact)
    
elif (b==3):
    print("Congrats!!! Square Root of a number Selected")
    #Ask user for the number
    sqr = float(input("Enter the number: "))
    import math
    sr = math.sqrt(sqr)
    y = round(sr,2)
    print("The square root of", sqr, "is", y)
    
elif(b==4):
    print("Congrats!!! Percentage Error Selected")
    #Prompt the user to input the numbers
    a = float(input("Enter the wrong value"))
    b = float(input("Enter the actual value"))
    ab = ((a-b)/b)
    ba = round(ab, 1)
    print("The percentage error is", ba, "percentage")
    
elif (b==5):
    print("Congrats!!! Quadratic Equation Selected")
    #Ask the user for the coefficients
    a = float(input("Enter the coefficient of x^2"))
    b = float(input("Enter the coefficient of x"))
    c = float(input("Enter the constant"))
    D = ((b**2)- 4*a*c)
    import math
    x1 = (((-1*b) + math.sqrt(D))/(2*a))
    import math
    x2 = (((-1*b) - math.sqrt(D))/(2*a))
    print("The values of x are", x1, "and",x2)

elif(b==6):
    print("Congrats!!! Simultaneous Equation Selected")
    print("Oshe!!! You can only find two variables (x and y)")
    print("NOTE: a1 = 1st coefficient of the 1st variable, b1 = 1st coefficient of the 2nd variable, c1 = 1st constant,"
              "a2 = 2nd coefficient of the 1st variable, b2 =  2nd coefficient of the 2nd variable and c2 = 2nd constant")
    a1 = float(input("Enter the value of a1"))
    b1 = float(input("Enter the value of b1"))
    c1 = float(input("Enter the value of c1"))
    a2 = float(input("Enter the value of a2"))
    b2 = float(input("Enter the value of b2"))
    c2 = float(input("Enter the vlaue of c2"))
    a3 = b2 * a1
    b3 = b2 * b1
    c3 = b2 * c1
    _a3 = b1 * a2
    _b3 = b1 * b2
    _c3 = b1 * c2
    a = a3 - _a3
    b = b3 - _b3
    c = c3 - _c3
    x1 = c / a
    x = round(x1, 2)
    print("The first value, x is", x)
    y1 = (x * a1)
    y2 = c1 - y1
    y3 = y2/b1
    y = round(y3, 2)
    print("The second value, y is", y)
    
elif (b==7):
    print ("Congrats!!! Loan Calculator Selected")
    import time
    time.sleep(1)
    print ("Select the operation you want to perform from the following")
    import time
    time.sleep(1)
    print ("Choose from the following; 1 = Interest, 2 = Interest Rate, 3 = Time, 4 = Amount, 5 = Principal")
    b = int(input("Enter the chose number"))
    if(b==1):
        print("Interest selected")
        a = float(input("Enter the interest rate"))
        b = float (input("Enter the period of time"))
        c = float(input("Enter the money in question"))
        d = ((a * b* c)/100)
        y = round (d,2)
        print("The interest on",c, "is", y)
    elif(b==2):
        print("Interest Rate Selected")
        a = float(input("Enter the interest"))
        b = float(input("Enter the period of time"))
        c = float(input("Enter the money in question"))
        d = ((100 * a)/(b*c))
        y = round (d,2)
        print("The Interest Rate on",c, "is", y)
    elif (b==3):
        print("Loan Period selected")
        a = float(input("Enter the interest"))
        b = float(input("Enter the Rate"))
        c = float(input("Enter the money in question"))
        d = ((100 * a)/(b*c))
        y = round (d,2)
        if(y<1):
            print(y * 12, "months")
        else:
            print(y, "year(s)")
    elif (b==4):
        print("Amount selected!")
        a = float(input("Enter the interest"))
        c = float(input("Enter the money in question"))
        d = a+c
        y = round (d,2)
        print("The Amount is", y)
    elif(b==5):
        print("Principal Seleected")
        a = float(input("Enter the interest"))
        b = float(input("Enter the period of time"))
        c = float(input("Enter the rate"))
        d = ((100 * a)/(b*c))
        y = round (d,2)
        print("The Principal is", y)
    else:
        print("Invalid number, check the instruction above and choose again. Thank you!!")
        
elif(b==8):
    print("Plane Shapes Selected")
    print("Select the number that represents the plane shape you want to solve; 1 = Circle, 2 = Rectangle, 3 = Square and 4 = Triangle")
    x = int(input("Enter the chosen number"))
    if (x==1):
        print("Yipee!! Circle Selected")
        print ("Choose the number that represents your operation; 1 = Area, 2 = Perimeter")
        y = int(input("Enter the number"))
        if(y==1):
            r = float(input("Enter the values of the radius"))
            f = r**2
            b = 3.142857 * f
            j = round(b,2)
            print("The Area of the Circle is",j)
        elif (b==2):
            r = float(input("Enter the values of the radius"))
            p = 6.2857 * r
            z = round(p,2)
            print("The Perimeter of the circle is",z)
        else:
            print("Invalid number chosen, check and TRY AGAIN; Thank You")
    elif (x==2):
        print("Yeah!!! RECTANGLE Selected")
        a = float(input("Enter the length of the Rectangle"))
        b = float (input("Enter the breadth of the Rectangle"))
        print("Choose the number that represents your operation; 1 = AREA, 2 = PERIMETER")
        c = int(input("Enter the chosen number"))
        if (c==1):
            print("AREA of a RECTANGLE Selected")
            d = a * b
            print("The AREA of the RECTANGLE is", d)
        elif(c==2):
            print("PERIMETER of a RECTANGLE Selected")
            d = 2*(a+b)
            print("The PERIMETER of the RECTANGLE is", d)
        else:
            print("Invalid number chosen, check and TRY AGAIN; Thank You")
    elif(x==3):
        print("GBEFUN!! SQUARE Selected")
        a = float(input("Enter the length of the square"))
        print("Choose the number that represents your operation; 1 = AREA, 2 = PERIMETER")
        c = int(input("Enter the chosen number"))
        if (c==1):
            print("AREA of a SQUARE Selected")
            d = a * a
            print("The AREA of the SQUARE is", d)
        elif(c==2):
            print("PERIMETER of a SQUARE Selected")
            d = 4 * a
            print("The PERIMETER of the SQUARE is", d)
        else:
            print("Invalid number chosen, check and TRY AGAIN; Thank You")
    elif(x==4):
        print("OSHAPRAPRA!!! TRIANGLE Chosen")
        print("You can only solve for the AREA now")
        b = float(input("Enter the value of the first side"))
        c = float(input("Enter the value of the second side"))
        d = float(input("Enter the value of the height"))
        f = 0.5*b*c*d
        print("The AREA of the TRIANGLE is", f)           
else:
    print("Invalid number, check the instruction above and choose again. Thank you!!")
