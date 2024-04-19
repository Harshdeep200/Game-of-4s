import time

def story():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a dark forest.")
    time.sleep(1)
    print("You can go left or right.")
    choice = input("Which way do you go? (left/right): ").lower()
    if choice == "left":
        print("You encounter a bear!")
        time.sleep(1)
        print("What do you do?")
        action = input("Fight or run? (fight/run): ").lower()
        if action == "fight":
            print("You fought bravely but were defeated by the bear. Game over!")
        elif action == "run":
            print("You ran away and survived. Congratulations, you win!")
        else:
            print("Invalid choice. Game over!")
    elif choice == "right":
        print("You find a treasure chest!")
        time.sleep(1)
        print("You open it and find gold. Congratulations, you win!")
    else:
        print("Invalid choice. Game over!")

if __name__ == "__main__":
    story()
