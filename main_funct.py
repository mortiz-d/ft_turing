from dataclasses import dataclass
import sys
import json
import argparse

movements = {
    'RIGHT': 1,
    'LEFT': -1
}

#----------CLASSES--------------------

@dataclass(frozen=True)
class RESULT:
    tape: list | None
    state: str | None
    position: int | None
    valid: bool

@dataclass(frozen=True)
class ACTION :
    state : str | None
    symbol : str | None
    new_state : str | None
    write: str | None
    movement: int | None
    movement_str: str | None

    def show(self):
        print("("+self.state+", "+self.symbol+") -> (" + self.new_state+", "+self.write+", "+self.movement_str+")")

@dataclass(frozen=True)
class DATA :
    debug:int | None
    name: str | None
    file : object | None
    position : int | None
    curr_state: str | None
    blank: str | None
    transitions: dict | None
    finals: dict | None
    states: dict | None
    alphabet : dict | None

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

#-----------------------show-----------------------------    

def show_tape(tape, position):
    print("[",end="")
    for x in range(len(tape)):
        if x == position:
            print("<"+tape[x]+">",end="")
        else:
            print(tape[x],end="")
    print("]" ,end="")

def show_help():
    print("usage: ft_turing [-h] jsonfile input")
    print("positional arguments:")
    print("jsonfile     json description of the machine")
    print("input        input of the machine\n")
    print("optional arguments:")
    print("-h, --help show this help message and exit")


def show_step(result,operation):
    show_tape(result.tape, result.position)
    print( "      ", end="")
    operation.show()
    return

#--------------------------------------

def find_action(actions, state, symbol):
    return next((a for a in actions if a.state == state and a.symbol == symbol), None )

def set_tape(tape, new_symbol, position):
    new_tape = tape.copy()
    new_tape[position] = new_symbol
    return new_tape

def set_position(position , movement):
    return position + movement

# δ(q⁰,a)=(q¹,b,D)
# (State,simbol read) = (new state, symbol wrote, Movement)
def new_action(operation ,result):
    
    if operation is None:
        return RESULT(tape=None,state=None,position=None,valid=False)
   
    return RESULT(
        tape=set_tape(result.tape, operation.write, result.position),
        state=operation.new_state,
        position=set_position(result.position, operation.movement),
        valid=True)
        
    

def parse_transitions(transitions):
    actions = []

    for state, transitions_list in transitions.items():
        for t in transitions_list:
            actions.append(ACTION(
                state=state,
                symbol=t.get("read"),
                new_state=t.get("to_state"),
                write=t.get("write"),
                movement_str=t.get("action"),
                movement=movements[t.get("action")]
            ))

    return actions

def get_filedata(path):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError):
        print("Error opening "+path+ " : "+json.JSONDecodeError)
        return None

def process_tape(path, new_tape):
    return build_data(get_filedata(path), new_tape)

def build_data(file_data, new_tape):
    if file_data is None:
        return None, None
    
    return list(new_tape), DATA(name= file_data.get("name"),
                                file = file_data, 
                                position= 0, 
                                curr_state= file_data.get("initial"),
                                blank = file_data.get("blank"), 
                                transitions=  parse_transitions(file_data.get("transitions")),
                                finals= file_data.get("finals"),
                                states= file_data["states"],
                                debug= 9,
                                alphabet = file_data.get("alphabet"))



def process_arguments(argv):
    parser = argparse.ArgumentParser(prog="ft_turing",description="",usage="ft_turing [-h] jsonfile input")
    parser.add_argument("jsonfile",help="json description of the machine")
    parser.add_argument("input",help="input of the machine")
    return parser.parse_args(argv)

def check_tape_boundraries(result,blank):
    if result.position >= len(result.tape):
        return RESULT(tape = result.tape + [blank],
                    state=result.state,
                    position=result.position,
                    valid=result.valid)
    if result.position < 0:
        return RESULT(tape = [blank] + result.tape,
                    state=result.state,
                    position=0,
                    valid=result.valid)
    return result
'''
    debug:int
    name: str
    file : object
    position : int
    curr_state: str
    blank: str
    transitions: dict
    finals: dict
    states: dict
    alphabet : dict

    state : str | None
    symbol : str | None
    new_state : str | None
    write: str | None
    movement: int | None
    movement_str: str | None
    
    '''

def validate_inputs(tape, data):
    if tape is None:
        raise ValueError("Error in Tape: Tape value is None")
    elif data is None:
        raise ValueError("Error in Data: Data value is None")

    if data.file is None:
        raise ValueError("Error in Tape: File value is None")
    elif data.name is None:
        raise ValueError("Error in Tape: Name value is None")
    elif data.curr_state is None:
        raise ValueError("Error in Tape: Tape value is None")
    elif data.blank is None:
        raise ValueError("Error in Tape: Blank value is None")
    elif data.transitions is None:
        raise ValueError("Error in Tape: Transition value is None")
    elif data.finals is None:
        raise ValueError("Error in Tape: Finals value is None")
    elif data.states is None:
        raise ValueError("Error in Tape: States value is None")
    elif data.alphabet is None:
        raise ValueError("Error in Tape: Alphabet value is None")

    for transition in data.transitions:
        if transition.state is None:
            raise ValueError("Error in Transition: States value is None")
        elif transition.symbol is None:
            raise ValueError(f"Error in Transition {transition.state}: Read value is None")
        elif transition.new_state is None:
            raise ValueError(f"Error in Transition {transition.state}: to_state value is None")
        elif transition.write is None:
            raise ValueError(f"Error in Transition {transition.state}: Write value is None")
        elif transition.movement_str is None:
            raise ValueError(f"Error in Transition {transition.state}: Action value is None")



    

def main(argv=None):

    args = process_arguments(argv)
    tape, data = process_tape(args.jsonfile, args.input)

    try:
        validate_inputs(tape, data)
    except ValueError as error:
        print(error)
        return 1
    
    data.show()
    
    result = RESULT(tape=tape,state=data.curr_state,position=data.position,valid=True)
    while result.state not in data.finals and result.valid is True :

        operation = find_action(data.transitions,result.state,result.tape[result.position])
        result = new_action(operation ,result)

        if not result.valid:
            break
        result = check_tape_boundraries(result, data.blank)
        show_step(result,operation)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))