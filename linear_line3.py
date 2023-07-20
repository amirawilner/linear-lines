#מציאת משואת קו ישר רמה בנינות עם שני מספרים אחרי הנקודה העשרונית


import random
import re  # Regular expressions for parsing input

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def generate_points():
    p1 = Point(random.randint(-10, 10), random.randint(-10, 10))
    p2 = Point(random.randint(-10, 10), random.randint(-10, 10))
    return p1, p2

def get_equation(p1, p2):
    if p2.x - p1.x == 0:  # vertical line case
        return None, p1.x  # slope is undefined, return x-intercept instead
    else:  # normal line case
        m = (p2.y - p1.y) / (p2.x - p1.x)
        b = p1.y - m * p1.x
        return m, b

def parse_equation(eq):
    if eq.startswith('x'):  # vertical line case
        b = float(eq.split('=')[1])
        return None, b
    
    else:  # normal line case
        m, b = re.findall(r"[-+]?\d*\.\d+|\d+", eq)  # find numbers in the string
        return float(m), float(b)

def student_answer(is_vertical):
    if is_vertical:
        b = float(input("Enter the x-intercept of the equation (b for x = b): "))
        return None, b
    else:
        m = float(input("Enter the slope of the equation (m): "))
        b = float(input("Enter the y-intercept of the equation (b): "))
        return m, b

def main():
    while True:  # exercise repetition mechanism
        p1, p2 = generate_points()
        correct_m, correct_b = get_equation(p1, p2)

        if correct_m is None:  # vertical line case
            print(f"The line is vertical passing through x = {correct_b}.")
            m, b = student_answer(True)
        else:  # normal line case
            print(f"The two points are ({p1.x}, {p1.y}) and ({p2.x}, {p2.y}).")
            m, b = student_answer(False)

        if correct_m is None and m is None:  # check answer for vertical line
            if abs(correct_b - b) <= 0.01:
                print("Correct! You've found the x-intercept.")
            else:
                print(f"Incorrect. The correct x-intercept is {correct_b:.2f}")
        elif abs(correct_m - m) <= 0.01 and abs(correct_b - b) <= 0.01:  # check answer for normal line
            print("Correct! You've found the slope and y-intercept.")
        else:
            print(f"Incorrect. The correct slope is {correct_m:.2f} and y-intercept is {correct_b:.2f}")
            
        eq = input("Now enter the equation of the line (in 'y = mx + b' or 'x = b' format): ")
        m, b = parse_equation(eq)
        
        if correct_m is None and m is None:  # check full equation for vertical line
            if abs(correct_b - b) <= 0.01:
                print("Correct! You've found the full equation of the line.")
            else:
                print(f"Incorrect. The correct equation is x = {correct_b:.2f}")
        elif abs(correct_m - m) <= 0.01 and abs(correct_b - b) <= 0.01:  # check full equation for normal line
            print("Correct! You've found the full equation of the line.")
        else:
            print(f"Incorrect. The correct equation is y = {correct_m:.2f}x + {correct_b:.2f}")

       

if __name__ == "__main__":
    main()


