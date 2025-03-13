def display_menu() -> None:
    """
    Displays the menu options to the user.
    """
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")


def greet_user() -> None:
    """
    Prints a greeting message.
    """
    print("Hello! Welcome!")


def check_even_odd(number: int) -> str:
    """
    Determines if a given number is even or odd.

    Args:
        number (int): The integer to check.

    Returns:
        str: A message stating whether the number is even or odd.
    """
    return f"{number} is an Even number." if number % 2 == 0 else f"{number} is an Odd number."


def even_odd_checker_action() -> None:
    """
    Prompts the user for an integer and checks if it's even or odd.
    """
    while True:
        try:
            num = int(input("Enter an integer: "))
            print(check_even_odd(num))
            break  # Exit loop after valid input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def handle_menu_choice(choice: int) -> bool:
    """
    Executes the corresponding action based on the user's menu choice.

    Args:
        choice (int): The selected menu option.

    Returns:
        bool: True if the user chooses to exit, False otherwise.
    """
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True  # Signal to terminate loop
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
    return False  # Continue loop


def main() -> None:
    """
    Main function that controls the program flow.
    Uses a loop to display the menu and process user choices.
    """
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))
            if handle_menu_choice(choice):
                break  # Exit loop if choice is 3
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")


if __name__ == "__main__":
    main()
