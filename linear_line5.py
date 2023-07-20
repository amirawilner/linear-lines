#מציאת נוסחאת קו ישר רמה קשה עם שני מסםרים אחרי הנקודה העשרונית


import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def generate_points():
    x1, y1 = random.uniform(-10, 10), random.uniform(-10, 10)  # generate random float numbers
    x1, y1 = round(x1, 2), round(y1, 2)  # round to two decimal places
    dx = random.uniform(1, 10)  # difference between x coordinates
    dy = dx * random.uniform(-10, 10)  # difference between y coordinates (adjusted to ensure slope is integer)
    dx, dy = round(dx, 2), round(dy, 2)  # round to two decimal places
    p1 = Point(x1, y1)
    p2 = Point(x1 + dx, y1 + dy)
    return p1, p2

def calculate_slope(p1, p2):
    return round((p2.y - p1.y) / (p2.x - p1.x), 2)  # round to two decimal places

def calculate_y_intercept(p, m):
    return round(p.y - m * p.x, 2)  # round to two decimal places

def main():
    while True:  # exercise repetition mechanism
        p1, p2 = generate_points()
        correct_m, correct_b = calculate_slope(p1, p2), calculate_y_intercept(p1, calculate_slope(p1, p2))

        print(f"The two points are ({p1.x}, {p1.y}) and ({p2.x}, {p2.y}).")

        if correct_m is None:  # vertical line case
            print(f"The line is vertical.")
            student_b = float(input("Enter the x-intercept of the equation (b for x = b): "))
            if student_b == correct_b:
                print("Correct!")
            else:
                print(f"Incorrect. The correct x-intercept is {correct_b}.")
        else:  # normal line case
            student_m = float(input("Enter the slope of the equation (m): "))
            if student_m == correct_m:
                print("Correct!")
            else:
                print(f"Incorrect. The correct slope is {correct_m}.")

            student_b = float(input("Enter the y-intercept of the equation (b): "))
            if student_b == correct_b:
                print("Correct!")
            else:
                print(f"Incorrect. The correct y-intercept is {correct_b}.")

        student_equation = input("Now enter the equation of the line (in 'y = mx + b' or 'x = b' format): ")
        if correct_m is None and student_equation.strip().lower() == f"x={correct_b}":
            print("Correct!")
        elif correct_m is not None and student_equation.strip().lower() == f"y={correct_m}x+{correct_b}":
            print("Correct!")
        else:
            if correct_m is None:
                print(f"Incorrect. The correct equation of the line is 'x={correct_b}'.")
            else:
                print(f"Incorrect. The correct equation of the line is 'y={correct_m}x+{correct_b}'.")

        repeat = input("Do you want to try again with new points? (yes/no): ")
        if repeat.lower() != "yes":
            break

if __name__ == "__main__":
    main()




