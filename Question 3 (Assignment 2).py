def get_number():
    """
    Gets a valid positive integer from the user.
    Handles invalid input.
    """
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n <= 0:
                print("Please enter a number greater than 0.")
            else:
                return n
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def print_pyramid(n):
    """
    Prints the numeric pyramid using nested loops.
    """

    for i in range(1, n + 1):

        # Print spaces
        for j in range(n - i):
            print(" ", end="")

        # Print ascending numbers
        for j in range(1, i + 1):
            print(j, end="")

        # Print descending numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")

        # Move to the next line
        print()


def main():
    n = get_number()
    print_pyramid(n)


# Run the program
main()