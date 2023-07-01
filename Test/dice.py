import random
def roll_dice():
    min_number = 1
    max_number = 6
    roll = random.randint(min_number, max_number)
    return roll


def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        input("Press Enter to roll the dice (or 'q' to quit): ")
        dice_roll = roll_dice()
        print("You rolled:", dice_roll)
        user_input = input("Roll again? (y/n): ")
        if user_input.lower() == 'n':
            break

    print("Thank you for playing!")


if __name__ == "__main__":
    main()
