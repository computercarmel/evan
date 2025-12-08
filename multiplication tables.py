# Loop through numbers 1 to 10
for i in range(1, 11):
    print(f"Multiplication table for {i}:")
    # Loop to print the multiples of i up to i * 10
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Blank line for separation between tables
