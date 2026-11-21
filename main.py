from dataclasses import dataclass
import sys
import json

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
    return next(
        (a for a in actions
         if a.state == state and a.symbol == symbol),
        None
    )

# δ(q⁰,a)=(q¹,b,D)
# (State,simbol read) = (new state, symbol wrote, Movement)
def action(data):

    operation = find_action(data.transitions,data.curr_state,data.tape[data.position])
    data.show_tape()
    print( "      ", end="")
    operation.show()
    # print (operation)

    

    return




    # options = data.file["transitions"]
    # actions = options[state]
    # new_state = ""
    
    
    # res = [t for t in actions if t['read'] == data.tape[data.position]]
    # if len(res) == 1:
    #     res = res[0]
    #     data.tape[data.position] = res["write"] # write the new symbol on tape
    #     new_state = res["to_state"] 
    #     print(data.position)
    #     data.position += movements[res["action"]] #movemos el tapeheader a donde diga la instruccion
    #     if (new_state in data.file["finals"]):
    #         print("encontre el final!")
    #         return
    #     action(data,new_state)
    # else:
    #     print("ERROR NO HE ENCONTRADO UNA ACCION PARA UNA PARTE")
    # return


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
        alphabet = file_data["alphabet"])
    return data
    


def main(args):

    data = process_tape(str(args[0]), str(args[1]))
    data.show()
    
    action(data)
    
    return
    print("You passed:", args)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))