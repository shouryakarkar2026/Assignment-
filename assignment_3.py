def is_right_triangle(a, b, c):

    hypotenuse = max(a, b, c)
    
    
    legs_sq_sum = (a**2 + b**2 + c**2) - hypotenuse**2
    
    return legs_sq_sum == hypotenuse**2


side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))


if is_right_triangle(side1, side2, side3):
    print("It is a right-angled triangle.")
else:
    print("It is NOT a right-angled triangle.")