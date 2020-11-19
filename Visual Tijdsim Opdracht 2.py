import simpy
import random
import matplotlib.pyplot as plt


def car(env, name, weg, plekken, vrij, driving_time, charge_duration):
    yield env.timeout(driving_time)
    number = int(name.split(' ')[1])
    auto_paths[number].append(env.now)

    yield env.timeout(random.randint(1,3))

    with vrij.request() as vrij:
        yield vrij

    auto_paths[number].append(env.now)
    while weg.count == 5 or plekken.count == 20:
        yield env.timeout(1)

    auto_paths[number].append(env.now)

    yield env.timeout(weg.count * 2 + 3)

    auto_paths[number].append(env.now)

    with weg.request() as weg1:
        yield weg1

    auto_paths[number].append(env.now)

    with plekken.request() as parkeer:
        print('%s parking at %s' % (name, env.now))
        yield parkeer
        auto_paths[number].append(env.now)
        yield env.timeout(charge_duration)
        auto_paths[number].append(env.now)

    while weg.count == 5:
        yield env.timeout(1)

    auto_paths[number].append(env.now)

    with weg.request() as weg:
        yield weg

    yield env.timeout(random.randint(3, 15))

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
print(auto_paths)

for i in auto_paths:

    plt.plot(i, range(0, len(i)))
plt.show()
