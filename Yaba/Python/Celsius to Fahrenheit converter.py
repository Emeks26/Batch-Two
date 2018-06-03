#Omole Wale +2348075296681
#Celsius to Fahrenheit converter
def convert():
    c = int(input("Enter current temperature in Celsius > "))
    f = c * 9/5 + 32
    return f

def main():
    f = convert()
    print("The temperature in Fahrenheit is {}.". format(f))


main()
