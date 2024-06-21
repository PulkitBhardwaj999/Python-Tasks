def fibonacci_sequence(n):
    # Initialize first two terms
    fib_sequence = [0, 1]

    # Generate Fibonacci sequence
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

# Input number of terms from user
n = int(input("Enter the number of terms in Fibonacci sequence: "))

# Check if the input is valid
if n <= 0:
    print("Please enter a positive integer.")
else:
    # Generate Fibonacci sequence
    fib_sequence = fibonacci_sequence(n)

    # Print Fibonacci sequence
    print("Fibonacci sequence up to", n, "terms:")
    print(fib_sequence)
