import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def main():
    radius = float(input("Enter the radius of the circle: "))
    circle_area = calculate_circle_area(radius)
    circle_perimeter = calculate_circle_perimeter(radius)
    print(f"The area of the circle is {circle_area}")
    print(f"The perimeter of the circle is {circle_perimeter}")

    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle_area = calculate_rectangle_area(length, width)
    rectangle_perimeter = calculate_rectangle_perimeter(length, width)
    print(f"The area of the rectangle is {rectangle_area}")
    print(f"The perimeter of the rectangle is {rectangle_perimeter}")

if __name__ == "__main__":
    main()
