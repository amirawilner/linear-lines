#נקודת מפגש של שני פונקציות 
import random

def find_intersection(m1, c1, m2, c2):
    x = (c2 - c1) // (m1 - m2)
    y = m1 * x + c1
    return (x, y)

def generate_lines():
    # Start with a random intersection point
    x, y = random.randint(-10, 10), random.randint(-10, 10)

    # Generate two random slopes
    m1, m2 = random.randint(-5, 5), random.randint(-5, 5)
    while m1 == m2:  # ensure the lines aren't parallel
        m2 = random.randint(-5, 5)

    # Calculate the y-intercepts for the lines to go through the intersection point
    c1 = y - m1 * x
    c2 = y - m2 * x

    return (m1, c1), (m2, c2), (x, y)

def main():
    (m1, c1), (m2, c2), intersection = generate_lines()

    print(f"The first line is: y = {m1}x + {c1}")
    print(f"The second line is: y = {m2}x + {c2}")
    print("Please find the intersection point of these two lines.")

    user_answer = input("Enter your answer in the format (x, y): ")
    
    # Format the user answer to tuple
    try:
        user_answer = eval(user_answer)
        if isinstance(user_answer, tuple) and len(user_answer) == 2:
            user_answer = int(user_answer[0]), int(user_answer[1])
        else:
            raise ValueError
    except Exception as e:
        print("Invalid input format, please enter the answer in the format (x, y)")
        return
    
    if user_answer == intersection:
        print("Congratulations, your answer is correct!")
    else:
        print("Sorry, your answer is incorrect.")
        
    print(f"The correct intersection point is {intersection}.")

main()



