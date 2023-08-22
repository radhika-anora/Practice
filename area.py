def areasquare():
    a=int(input("Enter side of square"))
    area=a*a
    print("Area of the given square is "+ str(area))

def areatriangle():
    c=int(input("Enter base of triangle"))
    h = int(input("Enter height of triangle"))
    area=0.5*c*h
    print("Area of the given triangle is "+ str(area))
def arearectangle():
    c=int(input("Enter length of rectangle"))
    h =int( input("Enter breadth of rectangle"))
    area=c*h
    print("Area of the given rectangle is "+ str(area))
def user_input(a):
    if a==0:
        areasquare(),
    elif a==1:
        areatriangle(),
    elif a==2:
        arearectangle()
    else:
        print("Incorrect input")



if __name__ == '__main__':
    b=int(input("Enter the shape to find area of\n(0)Square\n(1)Triangle\n(2)Rectangle"))
    user_input(b)

