import random

def main():
    print("Khansole Academy")

    # Generate two random 2-digit numbers (between 10 and 99)
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)

    # Ask the user the question
    print(f"What is {num1} + {num2}?")
    user_answer = int(input("Your answer: "))

    # Calculate the correct answer
    correct_answer = num1 + num2

    # Check if the user's answer is correct
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {correct_answer}")

    
if __name__ == '__main__':
    main()