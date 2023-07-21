# רמה קלה שטח של משלוש עם קו ישר 
import random

def calculate_area(x, y):
    # Area of a triangle = 1/2 * base * height
    # In this case, base and height are just the x and y intercepts
    return abs(x) * abs(y) // 2

def generate_line():
    # Generate random slope and y-intercept for the line equation
    slope = random.randint(-10, 10)
    y_intercept = random.randint(-10, 10)
    # Make sure slope and y_intercept are not zero and are multiples of 2
    while slope == 0 or y_intercept == 0 or slope % 2 != 0 or y_intercept % 2 != 0:
        slope = random.randint(-10, 10)
        y_intercept = random.randint(-10, 10)

    x_intercept = -y_intercept // slope

    return slope, y_intercept, x_intercept

def display_question(slope, y_intercept, x_intercept):
    print(f"The equation of the line is y = {slope}x + {y_intercept}")
    print(f"Find the area of the triangle formed by the x-intercept ({x_intercept}, 0), y-intercept (0, {y_intercept}), and the origin (0,0).")

def main():
    slope, y_intercept, x_intercept = generate_line()
    display_question(slope, y_intercept, x_intercept)
    answer = calculate_area(x_intercept, y_intercept)
    
    while True:
        try:
            user_answer = int(input("Your answer: "))
            break
        except ValueError:
            print("Invalid input, please enter a valid number.")
    
    if user_answer == answer:
        print("Correct!")
    else:
        print("Incorrect.")
    
    print(f"The correct answer is {answer} square units.")

if __name__ == "__main__":
    main()




