from Statemachine import StateMachine

positive_adjectives = ["great","super", "fun", "entertaining", "easy"]
negative_adjectives = ["boring", "difficult", "ugly", "bad"]

def start_transitions(txt):
    splitted_txt = txt.split(None,1)
    situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if situatie == "kaart pakken":
        newState = "Poort"
    else:
        newState = "Error"
    return (newState, txt)

def poort_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if situatie == "rijden":
        newState = "Op weg"
    elif situatie == "parkeren":
        newState = "Geparkeerd"
    else:
        newState = "Error"
    return (newState, txt)

def opweg_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if situatie == "not":
        newState = "not_state"
    elif situatie in positive_adjectives:
        newState = "pos_state"
    elif situatie in negative_adjectives:
        newState = "neg_state"
    else:
        newState = "error_state"
    return (newState, txt)

def geparkeerd_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if situatie in positive_adjectives:
        newState = "neg_state"
    elif situatie in negative_adjectives:
        newState = "pos_state"
    else:
        newState = "error_state"
    return (newState, txt)

def neg_state(txt):
    print("Hallo")
    return ("neg_state", "")

if __name__== "__main__":
    m = StateMachine()
    m.add_state("Start", start_transitions)
    m.add_state("Python_state", python_state_transitions)
    m.add_state("is_state", is_state_transitions)
    m.add_state("not_state", not_state_transitions)
    m.add_state("neg_state", None, end_state=1)
    m.add_state("pos_state", None, end_state=1)
    m.add_state("error_state", None, end_state=1)
    m.set_start("Start")
    m.run("Python is great")
    m.run("Python is difficult")
    m.run("Perl is ugly")