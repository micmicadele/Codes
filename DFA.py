class DFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.start_state = 'q0'
        self.accept_states = {'q1'}

        self.transitions = {
            'q0': {'0': 'q1', '1': 'q2'},
            'q1': {'0': 'q1', '1': 'q1'},
            'q2': {'0': 'q2', '1': 'q2'},
        }

    def process_input(self, input_string):
        current_state = self.start_state

        for symbol in input_string:
            if symbol in self.transitions[current_state]:
                current_state = self.transitions[current_state][symbol]
            else:
                return False

        return current_state in self.accept_states

if __name__ == "__main__":
    dfa = DFA()
    
    while True:
        input_string = input("Enter a string of 0s and 1s (or 'exit' to stop): ")

        if input_string.lower() == 'exit':
            break

        if dfa.process_input(input_string):
            print(f"The string '{input_string}' is accepted.")
        else:
            print(f"The string '{input_string}' is rejected.")