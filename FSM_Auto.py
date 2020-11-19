import simpy
import random
import matplotlib.pyplot as plt
from Statemachine import StateMachine

def car(env, name, weg, plekken, vrij, driving_time, charge_duration):
    def start_transitions(txt):
        splitted_txt = txt.split(None, 1)
        situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
        if situatie == "kaart pakken":
            newState = "Poort"

        else:
            newState = "Error"
        return newState, txt


    def poort_state_transitions(txt):
        splitted_txt = txt.split(None, 1)
        situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
        if situatie == "rijden":
            newState = "Op weg"
        elif situatie == "parkeren":
            newState = "Geparkeerd"

        else:
            newState = "Error"
        return newState, txt


    def opweg_state_transitions(txt):
        splitted_txt = txt.split(None, 1)
        situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
        if situatie == "parkeerplaats gevonden":
            newState = "Geparkeerd"
        elif situatie == "Geblokkeerd":
            newState = "Op weg"
        elif situatie == "uit garage":
            newState = "Slagboom"
        else:
            newState = "Error"
        return newState, txt


    def geparkeerd_state_transitions(txt):
        splitted_txt = txt.split(None, 1)
        situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
        # Time 'geparkeerd'
        if situatie == "rijden":
            newState = "Op weg"
        else:
            newState = "Error"
        return newState, txt


    def slagboom_state_transitions(txt):
        splitted_txt = txt.split(None, 1)
        situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
        if situatie == "Error":
            newState = "Op weg"
        else:
            newState = "Uit"
            #Time 'uit'
        return newState, txt


    if __name__ == "__main__":
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
        splitted_txt = txt.split(None, 1)
        situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
        if situatie == "in":
            newState = "eenonderweg"
        else:
            newState = "error"
        return newState, txt


    def nulonderwegalter(txt):
        splitted_txt = txt.split(None, 1)
        situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
        if situatie == "in":
            newState = "eenonderweg"
        else:
            newState = "error"
        return newState, txt


    def eenonderweg(txt):
        splitted_txt = txt.split(None, 1)
        situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
        if situatie == "in":
            newState = "tweeonderweg"
        elif situatie == "geparkeerd":
            newState = "nulonderwegalter"
        elif situatie == "uit":
            newState = "nulonderweg"
        else:
            newState = "error"
        return newState, txt


    def tweeonderweg(txt):
        splitted_txt = txt.split(None, 1)
        situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
        if situatie == "in":
            newState = "drieonderweg"
        elif situatie == "geparkeerd":
            newState = "eenonderweg"
        elif situatie == "uit":
            newState = "eenonderweg"
        else:
            newState = "error"
        return newState, txt


    def drieonderweg(txt):
        splitted_txt = txt.split(None, 1)
        situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
        if situatie == "in":
            newState = "vieronderweg"
        elif situatie == "geparkeerd":
            newState = "tweeonderweg"
        elif situatie == "uit":
            newState = "tweeonderweg"
        else:
            newState = "error"
        return newState, txt


    def vieronderweg(txt):
        splitted_txt = txt.split(None, 1)
        situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
        if situatie == "in":
            newState = "veelonderweg"
        elif situatie == "geparkeerd":
            newState = "drieonderweg"
        elif situatie == "uit":
            newState = "drieonderweg"
        else:
            newState = "error"
        return newState, txt


    def veelonderweg(txt):
        splitted_txt = txt.split(None, 1)
        situatie, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
        if situatie == "in":
            newState = "veelonderweg"
        elif situatie == "geparkeerd":
            newState = "vieronderweg"
        elif situatie == "uit":
            newState = "vieronderweg"
        else:
            newState = "error"
        return newState, txt


    if __name__ == "__main__":
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

    yield env.timeout(driving_time)  # Wanneer komt de auto aan op de parkeerplaats
    number = int(name.split(' ')[1])

    auto_paths[number].append(env.now)

    yield env.timeout(random.randint(1, 3))  # Hij rijdt naar voren

    with vrij.request() as vrij:
        yield vrij  # Als er plaats is op de oprit dan komt daar deze auto te staan

    auto_paths[number].append(env.now)
    while weg.count == 5 or plekken.count == 20:
        yield env.timeout(1)  # Als er geen parkeerplekken zijn of het is druk op de parkeerplaats,
        # dan blijf je wachten op de oprit tot dit niet zo is

    auto_paths[number].append(env.now)

    with weg.request() as weg1:
        yield weg1  # Je rijdt naar een parkeerplek toe

    yield env.timeout(weg.count * 2 + 3)  # Je rijdt naar een parkeerplek toe. Hier is in meegerekent dat
    # je tegenliggers kan hebben of andere problemen met tijd.

    auto_paths[number].append(env.now)

    with plekken.request() as parkeer:
        print('%s parking at %s' % (name, env.now))
        yield parkeer  # Je zoekt een parkeerplek
        auto_paths[number].append(env.now)
        yield env.timeout(charge_duration)  # Je staat geparkeerd tot je weg gaat
        auto_paths[number].append(env.now)

    while weg.count == 5:
        yield env.timeout(1)  # Als het druk is en je niet weg kan uit je parkeerplek moet je even wachten

    auto_paths[number].append(env.now)

    with weg.request() as weg:
        yield weg  # Vervolgens rij je de parkeerplaats uit

    yield env.timeout(random.randint(3, 15))  # Je moet soms op andere mensen wachten als je wegrijdt,
    # dus die hoeveelheid tijd hebben we hier meegerekend

    auto_paths[number].append(env.now)

    print('%s is gone %s' % (name, env.now))



env = simpy.Environment()
parkeer_plekken = simpy.Resource(env, capacity=10)
parkeer_weg = simpy.Resource(env, capacity=5)
plek_vrij = simpy.Resource(env, capacity=1)

aantal_autos = 30

auto_paths = []

for i in range(aantal_autos):
    auto_paths.append([])
    env.process(car(env, 'car %d' % i, parkeer_weg, parkeer_plekken, plek_vrij, i*random.randint(2, 10), random.randint(30, 100)))
env.run()

for i in auto_paths:
    plt.plot(i, range(0, len(i)))

plt.xlabel('Tijd')
plt.ylabel('Waar op de parkeerplaats (zie de readme)')
plt.title("Verloop van auto's op een parkeerplaats")
plt.show()
