import math 

def is_triangle(a, b, c):
    if math.hypot(a, b) == c:
        return True
    return False


print("The program checks if three sides form a right-angled triangle.")
inp1 = float(input("Enter first side value: "))
inp2 = float(input("Enter second side value: "))
inp3 = float(input("Enter third side value: "))
print("Is triangle?", is_triangle(inp1, inp2, inp3))
