#מציאת משואת הקו הישר רמה קלה



import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def generate_points():
    x1, y1 = random.randint(-10, 10), random.randint(-10, 10)
    dx = random.randint(1, 10)  # difference between x coordinates
    dy = dx * random.randint(-10, 10)  # difference between y coordinates (adjusted to ensure slope is integer)
    p1 = Point(x1, y1)
    p2 = Point(x1 + dx, y1 + dy)
    return p1, p2

def calculate_slope(p1, p2):
    return (p2.y - p1.y) // (p2.x - p1.x)  # floor division to ensure integer result

def calculate_y_intercept(p, m):
    return p.y - m * p.x

def main():
    p1, p2 = generate_points()

    print(f"Point 1: ({p1.x}, {p1.y})")
    print(f"Point 2: ({p2.x}, {p2.y})")

    print("\nYou can calculate the slope (m) of the line passing through these two points using the formula: m = (y2 - y1) / (x2 - x1)")
    print("where (x1, y1) and (x2, y2) are the coordinates of the two points.\n")

    correct_slope = calculate_slope(p1, p2)

    while True:
        student_slope = int(input("Enter the slope of the line passing through these points: "))
        if correct_slope == student_slope:
            print("Correct! Your slope matches the actual slope.")
            break
        else:
            print(f"Incorrect. The actual slope of the line through the points is {correct_slope}.")

    print("\nNow you can calculate the y-intercept (b) of the line using the formula: b = y - mx")
    print("where (x, y) is any point on the line, and m is the slope.\n")

    correct_y_intercept = calculate_y_intercept(p1, correct_slope)

    while True:
        student_y_intercept = int(input("Enter the y-intercept of the line: "))
        if correct_y_intercept == student_y_intercept:
            print("Correct! Your y-intercept matches the actual y-intercept.")
            break
        else:
            print(f"Incorrect. The actual y-intercept of the line is {correct_y_intercept}.")

    print("\nThe final step is to write the equation of the line. The equation of a line is generally expressed in the form y = mx + b,")
    print("where m is the slope and b is the y-intercept.\n")

    correct_equation = f"y={correct_slope}x+{correct_y_intercept}"

    while True:
        student_equation = input("Please write down the equation of the line: ")
        if student_equation.strip().lower() == correct_equation.lower():
            print("Correct! Your equation matches the actual equation of the line.")
            break
        else:
            print("Incorrect. Try again.")

    print(f"\nThe correct equation of the line is: {correct_equation}")

if __name__ == "__main__":
    main()












    