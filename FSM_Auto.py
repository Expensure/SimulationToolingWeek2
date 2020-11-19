from Statemachine import StateMachine

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
        newState = "Geparkeerd"
    elif situatie == "Geblokkeerd":
        newState = "Op weg"
    elif situatie == "uit garage":
        newState = "Slagboom"
    else:
        newState = "Error"
    return (newState, txt)

def geparkeerd_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if situatie == "rijden":
        newState = "Op weg"
    else:
        newState = "Error"
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
    m.add_state("Poort", poort_state_transitions)
    m.add_state("Op weg", opweg_state_transitions)
    m.add_state("Geparkeerd", geparkeerd_state_transitions)
    m.add_state("Slagboom", slagboom_state_transitions)
    m.add_state("Uit", None, end_state=1)
    m.add_state("Error", None, end_state=1)
    m.set_start("Start")

def nulonderweg(txt):
    splitted_txt = txt.split(None,1)
    situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if situatie == "in":
        newState = "eenonderweg"
    else:
        newState = "error"
    return (newState, txt)

def nulonderwegalter(txt):
    splitted_txt = txt.split(None,1)
    situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if situatie == "in":
        newState = "eenonderweg"
    else:
        newState = "error"
    return (newState, txt)

def eenonderweg(txt):
    splitted_txt = txt.split(None,1)
    situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if situatie == "in":
        newState = "tweeonderweg"
    elif situatie == "geparkeerd":
        newState = "nulonderwegalter"
    elif situatie == "uit":
        newState = "nulonderweg"
    else:
        newState = "error"
    return (newState, txt)


def tweeonderweg(txt):
    splitted_txt = txt.split(None,1)
    situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if situatie == "in":
        newState = "drieonderweg"
    elif situatie == "geparkeerd":
        newState = "eenonderweg"
    elif situatie == "uit":
        newState = "eenonderweg"
    else:
        newState = "error"
    return (newState, txt)

def drieonderweg(txt):
    splitted_txt = txt.split(None,1)
    situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if situatie == "in":
        newState = "vieronderweg"
    elif situatie == "geparkeerd":
        newState = "tweeonderweg"
    elif situatie == "uit":
        newState = "tweeonderweg"
    else:
        newState = "error"
    return (newState, txt)

def vieronderweg(txt):
    splitted_txt = txt.split(None,1)
    situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if situatie == "in":
        newState = "veelonderweg"
    elif situatie == "geparkeerd":
        newState = "drieonderweg"
    elif situatie == "uit":
        newState = "drieonderweg"
    else:
        newState = "error"
    return (newState, txt)

def veelonderweg(txt):
    splitted_txt = txt.split(None,1)
    situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if situatie == "in":
        newState = "veelonderweg"
    elif situatie == "geparkeerd":
        newState = "vieronderweg"
    elif situatie == "uit":
        newState = "vieronderweg"
    else:
        newState = "error"
    return (newState, txt)

if __name__== "__main__":
    n = StateMachine()
    n.add_state("nulonderweg", nulonderweg)
    n.add_state("nulonderwegalter", nulonderwegalter)
    n.add_state("eenonderweg", eenonderweg)
    n.add_state("tweeonderweg", tweeonderweg)
    n.add_state("drieonderweg", drieonderweg)
    n.add_state("vieronderweg", vieronderweg)
    n.add_state("veelonderweg", veelonderweg)
    n.add_state("error", None, end_state=1)
    n.set_start("nulonderweg")