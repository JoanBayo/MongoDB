

import json
from types import SimpleNamespace


class ordinador:
    def __init__(self, marca, modelo, cpu, ram):
        self.marca, self.modelo, self.cpu, self.ram  = marca, modelo, cpu, ram

if __name__ == '__main__':
    o1 = ordinador("HP", "250 G7","INTEL I3-10110U", "8")

    #objecte a json
    json_o1 = json.dumps(o1.__dict__)
    print("JSON creat des de objecte: ",json_o1)

    #json a fitxer:
    with open('ordinadors.json','w') as fitxer:
        json.dump(json_o1,fitxer)

    #fitxer a json:
    with open('ordinadors.json') as fitxer:
        json_02 = json.load(fitxer)
        print("JSON llegit des de fitxer: ",json_02)

    #json a objecte:
    o2 = json.loads(json_02,object_hook=lambda d:SimpleNamespace(**d))
    print(o2.ram)