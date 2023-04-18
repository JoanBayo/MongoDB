from flask import Flask
from bson import ObjectId

from eBayoFuncions import connectar, implementaPlantilla, implementaPlantillaInfoProducte, implementaPlantillaAbout

app = Flask(__name__)


@app.route("/")
def mostrarPerNomHome():
    p = connectar()
    productes = []
    docs = p.find().collation({'locale': 'en', 'strength': 2}).sort([('nom', 1)])
    for x in docs:
        productes.append(x)

    productes = {"productes": productes}

    contingut = implementaPlantilla(productes)

    return f'{contingut}'


@app.route("/nom")
def mostrarPerNom():
    p = connectar()
    productes = []
    docs = p.find().collation({'locale': 'en', 'strength': 2}).sort([('nom', 1)])
    for x in docs:
        productes.append(x)

    productes = {"productes": productes}

    contingut = implementaPlantilla(productes)

    return f'{contingut}'


@app.route("/preuAscendent")
def mostrarPerPreuAscendent():
    p = connectar()
    productes = []
    for x in p.find().sort("preu"):
        productes.append(x)

    productes = {"productes": productes}

    contingut = implementaPlantilla(productes)

    return f'{contingut}'


@app.route("/preuDescendent")
def mostrarPerPreuDescendent():
    p = connectar()
    productes = []
    for x in p.find().sort("preu", -1):
        productes.append(x)

    productes = {"productes": productes}

    contingut = implementaPlantilla(productes)

    return f'{contingut}'


@app.route("/valoracióAscendent")
def mostrarPerValoracioAscendent():
    p = connectar()
    productes = []
    for x in p.find().sort("valoracio"):
        productes.append(x)

    productes = {"productes": productes}

    contingut = implementaPlantilla(productes)

    return f'{contingut}'


@app.route("/valoracioDescendent")
def mostrarPerValoracioDescendent():
    p = connectar()
    productes = []
    for x in p.find().sort("valoracio", -1):
        productes.append(x)

    productes = {"productes": productes}

    contingut = implementaPlantilla(productes)

    return f'{contingut}'

@app.route("/idDescendent")
def mostrarPerIdDescendent():
    p = connectar()
    productes = []
    for x in p.find().sort("_id", -1):
        productes.append(x)

    productes = {"productes": productes}

    contingut = implementaPlantilla(productes)

    return f'{contingut}'
@app.route("/producto/<idProducto>")
def mostrainformacioProducte(idProducto):
    p = connectar()
    productes = []

    myquery = {"_id": ObjectId(idProducto)}

    mydoc = p.find(myquery)

    for x in mydoc:
        productes.append(x)

    productes = {"productes": productes}

    contingut = implementaPlantillaInfoProducte(productes)

    return f'{contingut}'


@app.route("/about")
def mostrainformacioAbout():
    productes = []

    contingut = implementaPlantillaAbout(productes)

    return f'{contingut}'

