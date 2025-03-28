class NFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4'}
        self.start_state = 'q0'
        self.accept_states = {'q4'}  

        self.transitions = {
            'q0': {'1': 'q1'},
            'q1': {'0': 'q2', '1': 'q2'}, 
            'q2': {'0': 'q3', '1': 'q3'},  
            'q3': {'0': 'q4', '1': 'q4'},  
            'q4': {} 
        }

    def process_input(self, input_string):
        current_states = {self.start_state}  

        for symbol in input_string:
            next_states = set() 

            for state in current_states:
                if symbol in self.transitions[state]:
                    next_states.add(self.transitions[state][symbol])

            current_states = next_states  

            if not current_states:
                return False

        return any(state in self.accept_states for state in current_states)


if __name__ == "__main__":
    nfa = NFA()
    
    while True:
        input_string = input("Enter a string of 0s and 1s (or 'exit' to stop): ")

        if input_string.lower() == 'exit':
            break

        if nfa.process_input(input_string):
            print(f"The string '{input_string}' is accepted.")
        else:
            print(f"The string '{input_string}' is rejected.")
