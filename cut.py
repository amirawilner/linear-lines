#חיתוך של פונקציה עם הצירים

import random

# Function to generate a random linear equation.
def generate_linear_equation():
    m = random.randint(-10, 10)  # random slope
    c = random.randint(-10, 10)  # random y-intercept
    return m, c

# Function to solve the linear equation for x = 0 and y = 0.
def solve_linear_equation(m,c):
    y_when_x_is_zero = round(c,2)  # y-intercept
    if m != 0:
        x_when_y_is_zero = round(-c / m, 2)
    else:
        x_when_y_is_zero = None
    return y_when_x_is_zero, x_when_y_is_zero

m, c = generate_linear_equation()
print(f"The equation of the line is y = {m}x + {c}")

# Ask for the coordinates.
x = input("What is the point when x = 0 (in the form (0,y))? ")
y = input("What is the point when y = 0 (in the form (x,0))? ")

# Strip brackets and split by comma to get the numbers.
x = float(x.strip('()').split(',')[1])
y = float(y.strip('()').split(',')[0])

correct_y, correct_x = solve_linear_equation(m, c)

x_correct = round(correct_y,2) == x
y_correct = round(correct_x,2) == y if correct_x is not None else False

if x_correct and y_correct:
    print("Congratulations! Your answers are correct.")
else:
    print("Sorry, your answers are incorrect.")

print(f"Correct answer for the point when x = 0: (0,{correct_y})")
if correct_x is not None:
    print(f"Correct answer for the point when y = 0: ({correct_x},0)")
else:
    print("The line is parallel to the y-axis, so there is no x-intercept.")






