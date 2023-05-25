#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_numbers = []
    for i in range(length):
        if i == 0 or i == 1:
            fibonacci_numbers.append(i)
        else:
            fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])
    print(fibonacci_numbers)