#מציאת נוסחאת קו ישר רצה קשה עם משסםרים שלמים

import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def generate_points():
    # Generate random integer points
    p1 = Point(random.randint(-10, 10), random.randint(-10, 10))
    p2 = Point(random.randint(-10, 10), random.randint(-10, 10))
    return p1, p2

def calculate_slope(p1, p2):
    if p2.x != p1.x:
        return (p2.y - p1.y) // (p2.x - p1.x)  # Integer division
    else:
        return None  # Handle the case where the slope is undefined

def calculate_y_intercept(p, m):
    if m is not None:
        return p.y - m * p.x
    else:
        return None  # Handle the case where the y-intercept is undefined

def main():
    p1, p2 = generate_points()
    correct_m = calculate_slope(p1, p2)
    correct_b = calculate_y_intercept(p1, correct_m)

    print(f"The two points are ({p1.x}, {p1.y}) and ({p2.x}, {p2.y}).")

    student_equation = input("Enter the equation of the line (in 'y = mx + b' or 'x = b' format): ")

    if correct_m is None and student_equation.strip().lower() == f"x={correct_b}":
        print("Correct!")
    elif correct_m is not None and student_equation.strip().lower() == f"y={correct_m}x+{correct_b}":
        print("Correct!")
    else:
        print("Incorrect.")

    if correct_m is None:
        print(f"The correct equation of the line is 'x={correct_b}'.")
    else:
        print(f"The correct equation of the line is 'y={correct_m}x+{correct_b}'.")

if __name__ == "__main__":
    main()



