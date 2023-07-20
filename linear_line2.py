#מציאת  משואת קו ישר רמה בינונית עם משפרים שלמים



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
    while True:  # exercise repetition mechanism
        p1, p2 = generate_points()
        correct_m, correct_b = calculate_slope(p1, p2), calculate_y_intercept(p1, calculate_slope(p1, p2))

        if correct_m is None:  # vertical line case
            print(f"The line is vertical.")
            student_b = int(input("Enter the x-intercept of the equation (b for x = b): "))
            if student_b == correct_b:
                print("Correct! You've found the x-intercept.")
            else:
                print(f"Incorrect. The correct x-intercept is {correct_b}.")
        else:  # normal line case
            print(f"The two points are ({p1.x}, {p1.y}) and ({p2.x}, {p2.y}).")
            student_m = int(input("Enter the slope of the equation (m): "))
            student_b = int(input("Enter the y-intercept of the equation (b): "))
            if student_m == correct_m and student_b == correct_b:
                print("Correct! You've found the slope and y-intercept.")
            else:
                print(f"Incorrect. The correct slope is {correct_m} and the correct y-intercept is {correct_b}.")

        student_equation = input("Now enter the equation of the line (in 'y=mx+b' or 'x=b' format): ")
        if correct_m is None and student_equation.strip().lower() == f"x={correct_b}":
            print("Correct! You've found the full equation of the line.")
        elif correct_m is not None and student_equation.strip().lower() == f"y={correct_m}x+{correct_b}":
            print("Correct! You've found the full equation of the line.")
        else:
            if correct_m is None:
                print(f"Incorrect. The correct equation of the line is 'x={correct_b}'.")
            else:
                print(f"Incorrect. The correct equation of the line is 'y={correct_m}x+{correct_b}'.")

       

if __name__ == "__main__":
    main()
 
 