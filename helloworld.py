# File: complex_code.py

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def main():
    num = int(input("Enter a number to calculate its factorial: "))
    factorial_result = calculate_factorial(num)
    print(f"The factorial of {num} is: {factorial_result}")

    # Printing "Hello World" multiple times
    for _ in range(5):
        print("Hello World")

if __name__ == "__main__":
    main()
