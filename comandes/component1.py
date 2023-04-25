import pickle


def saveObject(object1, fileName):
    with open(fileName, "ab") as file:
        pickle.dump(object1, file)


def restoreObject(index, fileName):
    with open(fileName, "rb") as file:
        while True:
            try:
                object1 = pickle.load(file)
            except EOFError:
                break
            if object1.id == index:
                return object1


def UpdateObject(index, fileName, newObject):
    comanda = []
    with open(fileName, "rb") as file:
        while True:
            try:
                objectevariable = pickle.load(file)
                if objectevariable.id != index:
                    comanda.append(objectevariable)
            except EOFError:
                break
        file.close()

    with open(fileName, "wb") as file:
        for objecte in comanda:
            saveObject(objecte, fileName)
        saveObject(newObject, fileName)
        file.close()

    return True


def removeObject(index, fileName):
    comanda = []
    with open(fileName, "rb") as file:
        while True:
            try:
                objectevariable = pickle.load(file)
                if objectevariable.id != index:
                    comanda.append(objectevariable)
            except EOFError:
                break
        file.close()

    with open(fileName, "wb") as file:
        for objecte in comanda:
            saveObject(objecte, fileName)
        file.close()

def RemoveFile(fileName):
    with open(fileName, "wb") as file:
        file.close()

def restoreAllBasket(fileName):
    arrayObject = []
    with open(fileName, "rb") as file:
        while True:
            try:
                object1 = pickle.load(file)
                arrayObject.append(object1)
            except EOFError:
                break
        file.close()
        return arrayObject
