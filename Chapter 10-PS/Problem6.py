class calc:
    def __init__(sb,n):
        sb.n= n


    def square(sb):
        print (f"Square of n = {sb.n*sb.n}")   
    def cube(sb):
        print (f"Cube of n = {sb.n*sb.n*sb.n}")   
    def squareroot(sb):
        print (f"SquareRoot of n = {sb.n**1/2}")   


a=calc(10)
a.square()
a.cube()
a.squareroot()
        
