from dataclasses import dataclass
import sys
import json
import argparse

movements = {
    'RIGHT': 1,
    'LEFT': -1
}

@dataclass
class ACTION :
    state : str
    symbol : str
    new_state : str
    write: str
    movement: int
    movement_str: str

    def show(self):
        print("("+self.state+", "+self.symbol+") -> (" + self.new_state+", "+self.write+", "+self.movement_str+")")

@dataclass
class DATA :
    debug:int
    name: str
    tape : list
    file : object
    position : int
    curr_state: str
    blank: str
    transitions: dict
    finals: dict
    states: dict
    alphabet : dict

    def show(self):
        print("==========================")
        print("         ",self.name)
        print("==========================")
        print(f"Alphabet:    {self.alphabet}")
        print(f"States:      {self.states}")
        print(f"State:        {self.curr_state}")
        print(f"Finals:      {self.finals}")
        print(f"Transitions:")
        for t in self.transitions:
            t.show()
        print("==========================")

    def show_tape(self):
        print("[",end="")
        for x in range(len(self.tape)):
            if x == self.position:
                print("<"+self.tape[x]+">",end="")
            else:
                print(self.tape[x],end="")
        print("]" ,end="")


def find_action(actions, state, symbol):
    return next((a for a in actions if a.state == state and a.symbol == symbol), None )

# δ(q⁰,a)=(q¹,b,D)
# (State,simbol read) = (new state, symbol wrote, Movement)
def action(data):
    operation = find_action(data.transitions,data.curr_state,data.tape[data.position])

    if operation is not None:
        nsym = operation.write
        nstat = operation.new_state
        data.tape[data.position] = nsym
        data.position += operation.movement
        if data.position >= len(data.tape):
            data.tape.append(data.blank)
        data.curr_state = nstat
        data.show_tape()
        print( "      ", end="")
        operation.show()
        
        if data.curr_state not in data.finals:
            action(data)
    else :
        print ("aqui no hay nada que hacer")
    return


def parse_transitions(transitions):
    actions = []

    for state, transitions_list in transitions.items():
        for t in transitions_list:
            actions.append(ACTION(
                state=state,
                symbol=t["read"],
                new_state=t["to_state"],
                write=t["write"],
                movement_str=t["action"],
                movement=movements[t["action"]]
            ))

    return actions

def process_tape(path, new_tape):
    with open(path, "r") as file:
        file_data = json.load(file)

    data = DATA(name= file_data["name"],
        tape= list(new_tape), 
        file = file_data, 
        position= 0, 
        curr_state= file_data["initial"],
        blank = file_data["blank"], 
        transitions=  parse_transitions(file_data["transitions"]),
        finals= file_data["finals"],
        states= file_data["states"],
        debug= 9,
        alphabet = file_data["alphabet"])
    return data

def show_help():
    print("usage: ft_turing [-h] jsonfile input")
    print("positional arguments:")
    print("jsonfile     json description of the machine")
    print("input        input of the machine\n")
    print("optional arguments:")
    print("-h, --help show this help message and exit")


def main(argv=None):

    parser = argparse.ArgumentParser(prog="ft_turing",description="",usage="ft_turing [-h] jsonfile input")
    parser.add_argument("jsonfile",help="json description of the machine")
    parser.add_argument("input",help="input of the machine")

    args = parser.parse_args(argv)


    data = process_tape(str(args.jsonfile), str(args.input))
    data.show()
    
    action(data)
    
    return
    print("You passed:", args)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))