from Statemachine import StateMachine

opstopredenen = ["great","super", "fun", "entertaining", "easy"]

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
    if situatie == "parkeerplaats gevonden":
        newState = "geparkeerd"
    elif situatie in opstopredenen:
        newState = "Op weg"
    elif situatie == "uit garage":
        newState = "Slagboom"
    else:
        newState = "error_state"
    return (newState, txt)

def geparkeerd_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if situatie == "rijden":
        newState = "Op weg"
    else:
        newState = "error_state"
    return (newState, txt)

def slagboom_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if situatie == "Error":
        newState = "Op weg"
    else:
        newState = "Uit"
    return (newState, txt)

if __name__== "__main__":
    m = StateMachine()
    m.add_state("Start", start_transitions)
    m.add_state("Python_state", python_state_transitions)
    m.add_state("is_state", is_state_transitions)
    m.add_state("not_state", not_state_transitions)
    m.add_state("Uit", None, end_state=1)
    m.add_state("Error", None, end_state=1)
    m.set_start("Start")
    m.run("Python is great")
    m.run("Python is difficult")
    m.run("Perl is ugly")