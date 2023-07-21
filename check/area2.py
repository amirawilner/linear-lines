#שטח של משולש עם חיתוך של שני קוים רמה בינונית

import random

def calculate_area(base, height):
    return round(1/2 * abs(base) * abs(height), 2)

def generate_line():
    slope = random.randint(-10, 10)
    y_intercept = random.randint(-10, 10)
    while slope == 0 or y_intercept == 0:
        slope = random.randint(-10, 10)
        y_intercept = random.randint(-10, 10)

    x_intercept = round(-y_intercept/slope, 2)

    return slope, y_intercept, x_intercept

def find_intersection(line1, line2):
    slope1, y_intercept1, _ = line1
    slope2, y_intercept2, _ = line2

    x_intersection = round((y_intercept2 - y_intercept1) / (slope1 - slope2), 2)
    y_intersection = round(slope1 * x_intersection + y_intercept1, 2)

    return x_intersection, y_intersection

def display_question(line1, line2):
    slope1, y_intercept1, _ = line1
    slope2, y_intercept2, _ = line2
    print(f"The equations of the lines are y = {slope1}x + {y_intercept1} and y = {slope2}x + {y_intercept2}")
    print(f"Find the height, base and the area of the triangle formed by the x-intercepts, y-intercepts, and the intersection point of the two lines.")

def main():
    line1 = generate_line()
    line2 = generate_line()
    while line1[0] == line2[0]:  # To avoid parallel lines
        line2 = generate_line()

    x_intersection, y_intersection = find_intersection(line1, line2)

    display_question(line1, line2)

    base = round(abs(line1[2] - line2[2]), 2)
    height = round(abs(y_intersection), 2)

    answer = calculate_area(base, height)

    print("\nFirst, let's determine the height:")
    while True:
        try:
            user_height = float(input("Your height: "))
            break
        except ValueError:
            print("Invalid input, please enter a valid number.")

    print("\nNext, let's determine the base:")
    while True:
        try:
            user_base = float(input("Your base: "))
            break
        except ValueError:
            print("Invalid input, please enter a valid number.")

    print("\nFinally, let's calculate the area:")
    while True:
        try:
            user_answer = float(input("Your area: "))
            break
        except ValueError:
            print("Invalid input, please enter a valid number.")

    if abs(user_answer - answer) < 0.01 and abs(user_base - base) < 0.01 and abs(user_height - height) < 0.01:  # Considering rounding error
        print("Correct!")
    else:
        print("Incorrect.")
        
    print(f"The correct answers are base: {base}, height: {height} and area: {answer} square units.")

if __name__ == "__main__":
    main()


