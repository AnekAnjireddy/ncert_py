from itertools import product

# Given digits
digits = ['0', '1', '3', '5', '7']

# Generate all possible combinations of 4 digits using repetition
possible_combinations = product(digits, repeat=4)

# Convert combinations to numbers and count total and divisible numbers
total_numbers = 0
divisible_numbers = 0

for combination in possible_combinations:
    number = int(''.join(combination))
    if number > 5000 and number % 5 == 0:
        divisible_numbers += 1
    total_numbers += 1

# Calculate the probability
probability = divisible_numbers / total_numbers

print("Total possible numbers:", total_numbers)
print("Divisible numbers:", divisible_numbers)
print("Probability:", probability)

