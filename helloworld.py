# File: complex_code.py

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def main():
    # Calculate and print the first 10 numbers in the Fibonacci sequence
    fibonacci_sequence = fibonacci(10)
    print("Fibonacci Sequence:", fibonacci_sequence)

    # Printing "Hello World" multiple times
    for _ in range(5):
        print("Hello World")

if __name__ == "__main__":
    main()
