print("""Hello!",
        "1:Perimeter and Area of circle",
        "2:Perimeter and Area of Square",
        "3:Perimeter and Area of Triangle"
        ,"4:Perimeter and Area of Trapezoid"
        ,"5:Area of Polygonal ",
        "6:Perimeter and Area of Rectangle"
        ,"7:Volume of Butter",
        "8:The Volume of the Cone",
        "9:Area of Oval """)
x=input("Enter between 1to10: ")
##########1.دايره################
#R=float(input("شعاع را وارد کنيد:"))
def circle():
    R=float(input("Enter R:"))
    A=R*R
    P=R+R
    import math
    return print(f"Area of circle{math.pi * A}",f"Perimeter of circle{math.pi * P}")
###########2.مربع######################
#a=float(input("ضلع مربع را وارد کنيد:"))
def Square():
    a=float(input("Enter the length of the side of the square:"))
    A=a*a
    P=4*a
    return print(f" Area of Square:",A,f" Perimeter of Square :",P)
#############3.مثلث######################
#a=float(input("ضلع اول مثلث را وارد کنيد:"))
#b=float(input("ضلع دوم مثلث را وارد کنيد:"))
#c=float(input("ضلع سوم مثلث را وارد کنيد:"))
def Triangle():
    import math
    a=float(input("Enter the length of the side1 of the Triangle:"))
    b=float(input("Enter the length of the side2 of the Triangle:"))
    c=float(input("Enter the length of the side3 of the Triangle:"))
    
    if ((a+b>c)and(a+c>b)and(c+b>a)):
        print("This is Triangle!")
        P=a+b+c
        p=P/2
        s=p*(p-a)*(p-b)*(p-c)
        S=math.sqrt(s)
    else:
        print("This isn't Triangle!")
    return print(f"Area of Triangle:",S,f"Perimeter of Triangle :",P)
################4.ذوزنقه##################    

def Trapezoid():
    a=float(input("Enter the length of the small side of the Trapezoid:"))
    c=float(input("Enter the length of the large side of the Trapezoid:"))
    b=float(input("Enter the length of the side of the leg1 of the Trapezoid:"))
    d=float(input("Enter the length of the side of the leg2 of the Trapezoid:"))
    h=float(input("Enter the length of the height of the Trapezoid:"))
    P=a+b+c+d
    S=(a+c)*h/2
    return print(f"Area of Trapezoid : ",P,f"Perimeter of Trapezoid: ",S)
############5.چند ضلعي#####################
def Polygonal():
    n=float(input("Enter the number of sides of the polygonal : "))
    d=float(input("Enter the size of the sides of the polygonal: "))
    h=float(input("Enter the size of the height of the polygonal: "))
    S=(n*d*h)/2
    
    return print(f"Area of Polygonal: ",S)


###########6.مستطيل########################

def Rectangle():
    a=float(input("Enter the length:"))
    b=float(input("Enter the width:"))
    P=2*(a+b)
    S=a*b
    return print(f"Area of Rectangle: ",S,f"Perimeter of Rectangle: ",P)
    
################7.کره#####################

def Butter():
    import math
    r=float(input("Enter the R:"))
    v=0.75*r*r*r
    V=math.pi * v
    
    return print(f"Volume of Butter: ",V)
###############8.مخروط#######################

def Cone():
    r=float(input("Enter the length of the base radius:"))
    h=float(input("Enter the length of the height:"))
    import math
    V=(1/3)*h*r*r*math.pi
    
    return print(f"The Volume of the Cone:",V)
###############9.بيضي#########################

def Oval():
    r1=float(input("Enter the R1:"))
    r2=float(input("Enter the R2:"))
    import math
    S=math.pi*r1*r2
    
    return print(f"Area of Oval: ",S)
#############مقدار دهي#########################
#num1 =  circle(r)
#num2 = Square(a)
#num3 = Triangle(a,b,c)
#num4 = Trapezoid(a,b,c,d,h)
#num5 = Polygonal(n)
#num6 = Rectangle(a,b)
#num7 = Butter(r)
#num8 = Cone(r,h)
#num9 = Oval(r1,r2)
#num10 = ESC

match x:
    case '1':
         circle()
    case '2':
         Square()
    case '3':
         Triangle()
    case '4':
        Trapezoid()
    case '5':
        Polygonal()
    case '6':
        Rectangle()
    case '7':
        Butter()
    case '8':
        Cone()
    case '9':
        Oval()
    case '10':
        print("Have good time")        
    case _:
        print("please enter the number between 1 to 10!")    
