#Name: Ojo Sodeeq Adeshina
#Phone Number: 08020597948
#Project description: To calculate the area and perimeter of polygons

n =l=r =0

def check_sides(polygon):
    if polygon <=2:
        print('this is not a polygon')
    elif polygon==3:
       print('Triangle')
    elif polygon==4:
       print('quadrilateral') 
    elif polygon==5:
       print('Pentagon') 
    elif polygon==6:
       print('Hexagon')
    elif polygon==7:
       print('Hexagon')
    elif polygon==8:
       print('Octagon')       
    elif polygon==9:
       print('Nonagon')
    elif polygon==10:
       print('Decagon')

def get_input():
    global n
    global l
    global r
    n=int(input('enter the number of sides of the polygon')) #the number of sides of the polygon is inputed here
    check_sides(n)
    
    l=int(input('enter the border length of the polygon')) #the length of sides of the polygon is inputed here
    r=int(input('enter radius of the polygon')) #the radius of sides of the polygon is inputed here


def get_area_and_perimeter():
    global n
    global l
    global r
    get_input()    
    area =(n* (l * r))/2 #this calculate the area of the polygon
    perimeter=n*l #this calculate the perimeter of the polygon

    print('the area of polygon with side', n, 'length', l, 'radius', r, 'is', area)
    print('the perimeter of polygon with side', n, 'length', l, 'is', perimeter)

get_area_and_perimeter()
