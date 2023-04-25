from flask import Flask, request, render_template, session
from bson import ObjectId

import comandes.component1 as c
import comandes.comanda as com


from flask_session import Session

from eBayoFuncions import *

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



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
    session["idProducte"] = idProducto
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


@app.route('/addPorductCar', methods=('GET', 'POST'))
def addPorductCar():
    quantitat = request.form['idquantitat']

    p = connectar()
    productes = []
    myquery = {"_id": ObjectId(session["idProducte"])}

    mydoc = p.find(myquery)

    for x in mydoc:
        productes.append(x)

    productes = {"productes": productes}

    c1 = com.comanda(session["idProducte"], quantitat, productes.get("preu"))

    if c.UpdateObject(session["idProducte"], "comandes.bin", c1):
        pass
    else:
        c.saveObject(c1, "comandes.bin")

    contingut = implementaPlantillaInfoProducte(productes)

    return f'{contingut}'


@app.route("/yourBasket")
def mostrainformacioBasket():

    arrayCompres = c.restoreAllBasket("comandes.bin")

    basket = {"items": arrayCompres}

    contingut = implementaPlantillaBasket(basket)

    return f'{contingut}'


@app.route("/deleteProduct")
def delete_one_product_basket():
    c.removeObject(session["idProducte"], "comandes.bin")


@app.route("/deleteAllProduct")
def delete_all_product_basket():
    c.RemoveFile("comandes.bin")