class FSM:
    def __init__(self):
        self.state = 'Locked'  # Start state

    def push(self):
        if self.state == 'Locked':
            print("You pushed but the system remains LOCKED.")
        elif self.state == 'Unlocked':
            self.state = 'Locked'
            print("You pushed. The system is now LOCKED.")

    def coin(self):
        if self.state == 'Locked':
            self.state = 'Unlocked'
            print("You inserted a coin. The system is now UNLOCKED.")
        elif self.state == 'Unlocked':
            print("You inserted a coin but the system remains UNLOCKED.")

    def print_locked_state(self):
        if self.state == 'Locked':
            print("The system is currently LOCKED.")


def main():
    fsm = FSM()
    print(f"Enter a command (Push and Coin) or Exit: ")

    while True:
        command = input().strip().lower()

        if command == 'push':
            fsm.push()
            fsm.print_locked_state()
        elif command == 'coin':
            fsm.coin()
        elif command == 'exit':
            break
        else:
            print("Unknown command. Please enter 'Push', 'Coin', or 'Exit'.")

if __name__ == "__main__":
    main()
