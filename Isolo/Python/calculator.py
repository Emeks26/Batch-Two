# jimoh Nojimu Oluwagbenga, oflondonn@gmail.com,08060148519
'''making a simple calculator that can add using functions'''
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y


def display():
    print('The sum is', sum)
    print('The difference is', difference)
    print('the product is',product)
    print('the division is',division)
    
x= eval(input('Enter the number: '))
y= eval(input('Enter the number: '))
sum=add(x,y)
difference = subtract(x,y)
product = multiply(x,y)
division=divide(x,y)


display()
