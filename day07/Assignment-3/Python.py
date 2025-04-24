import math

def circle_area(radius):
    return math.pi * radius**2

def triangle_area(a, b, c):  # Heron's formula
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"Circle area (radius = 5): {circle_area(5)}")
print(f"Triangle area (sides = 3, 4, 5): {triangle_area(3, 4, 5)}")