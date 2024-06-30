# pattern_drawing.py

def main():
    # Prompt the user to enter a positive integer for the size of the pattern
    size = int(input("Enter the size of the pattern: "))

    # Validate the input to ensure it is a positive integer
    if size <= 0:
        print("Please enter a positive integer.")
        return

    # Initialize the row counter
    row = 0

    # Use a while loop to iterate through each row
    while row < size:
        # Use a for loop to print asterisks side by side
        for _ in range(size):
            print("*", end="")
        # Print a newline character after each row
        print()
        # Move to the next row
        row += 1

if name == "__main__":
    main()
