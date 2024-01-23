# Generates the first 10 numbers of the Fibonacci sequence and prints "Hello World" a number of times equal to the count of even Fibonacci numbers in the sequence


def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def count_even_fibonacci(sequence):
    return sum(1 for num in sequence if num % 2 == 0)

def main():
    # Calculate and print the first 10 numbers in the Fibonacci sequence
    fibonacci_sequence = fibonacci(10)
    print("Fibonacci Sequence:", fibonacci_sequence)

    # Count the number of even Fibonacci numbers
    even_count = count_even_fibonacci(fibonacci_sequence)

    # Printing "Hello World" based on the count of even Fibonacci numbers
    for _ in range(even_count):
        print("Hello World")

if __name__ == "__main__":
    main()