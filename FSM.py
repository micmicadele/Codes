class FSM:
    def __init__(self):
        self.states = ['Locked', 'Unlocked']
        self.current_state = 'Locked'

    def process_input(self, action):
        if self.current_state == 'Locked':
            if action == 'Coin':
                self.current_state = 'Unlocked'
            elif action == 'Push':
                self.current_state = 'Locked'
        elif self.current_state == 'Unlocked':
            if action == 'Coin':
                self.current_state = 'Unlocked'
            elif action == 'Push':
                self.current_state = 'Locked'

    def get_state(self):
        return self.current_state


if __name__ == "__main__":
    fsm = FSM()
    
    while True:
        action = input("Enter an action (Push, Coin) or 'exit' to stop: ")

        if action.lower() == 'exit':
            break

        fsm.process_input(action)
        print(f"Current state: {fsm.get_state()}")
