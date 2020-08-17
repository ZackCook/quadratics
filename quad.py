import math

def main():
    a = float(input("Input coeffiecient of 'a' term: "))
    b = float(input("Input coeffiecient of 'b' term: "))
    c = float(input("Input coefficient of 'c' term: "))

    print(quadratic(a,b,c))

def quadratic(a,b,c):
     #  -b+-sqrt(b^2-4ac)/2a

     discriminant = 0

     try:
        discriminant = math.sqrt((b**2)-4*a*c)
     except ValueError:
        return "Complex answer"

     
     plus = (-b + discriminant)/(2*a)
     minus = (-b - discriminant)/(2*a)

     return (plus,minus)

main()