# Write a Python program that generates the Fibonacci sequence up to a specified number of terms, n. The Fibonacci sequence starts with 0 and 1, and each subsequent number in the
# sequence is the sum of the two preceding numbers (e.g., 0, 1, 1, 2, 3, 5, 8, ...). Prompt the user to enter the number of terms (n) they want in the sequence and then display the
# Fibonacci sequence up to that number of terms.

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
