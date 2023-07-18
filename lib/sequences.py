#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = []

    if length >= 1:
        fibonacci_sequence.append(0)
    if length >= 2:
        fibonacci_sequence.append(1)

    while len(fibonacci_sequence) < length:
        new_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(new_number)

    print(fibonacci_sequence)