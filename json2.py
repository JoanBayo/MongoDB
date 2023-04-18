from tkinter import ttk, messagebox, CENTER
import tkinter as tk

import pymongo
from bson import ObjectId

productesTenda = []


class producte:
    def __init__(self, nom, preu, descripcio, longDescripcio, destacat, valoracio, imatge):
        self.nom, self.preu, self.descripcio, self.longDescripcio, self.destacat, self.valoracio, \
            self.imatge = nom, preu, descripcio, longDescripcio, destacat, valoracio, imatge


def serchProducte(valor):
    curItem = tree.focus()
    text = tree.item(curItem)["values"]

    ent_IdProducte.delete(0, tk.END)
    ent_NomProducte.delete(0, tk.END)
    ent_PreuProducte.delete(0, tk.END)
    ent_descripcio.delete(0, tk.END)
    ent_LongDescripcio.delete(0, tk.END)
    ent_DestacatProducte.delete(0, tk.END)
    ent_ValoracioProducte.delete(0, tk.END)
    ent_ImatgeProducte.delete(0, tk.END)

    ent_IdProducte.insert(0, text[0])
    ent_NomProducte.insert(0, text[1])
    ent_PreuProducte.insert(0, text[2])
    ent_descripcio.insert(0, text[3])
    ent_LongDescripcio.insert(0, text[4])
    ent_DestacatProducte.insert(0, text[5])
    ent_ValoracioProducte.insert(0, text[6])
    ent_ImatgeProducte.insert(0, text[7])


def addProducte():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["productesBayo"]
    mycol = mydb["productesBayo"]
    nomProducte = ""
    preuProducte = 0
    descripcioProducte = ""
    valoracioProducte = 0
    longDescripcioProducte = ""
    destacatProducte = ""
    imateProducte = ""

    lbl_Answer.config(text="")

    productesTenda.clear()

    try:
        nomProducte = ent_NomProducte.get()
        preuProducte = float(ent_PreuProducte.get())
        try:
            valoracioProducte = float(ent_ValoracioProducte.get())
            if valoracioProducte > 5 or valoracioProducte < 1:
                raise Exception
        except Exception:
            lbl_Answer.config(text="La valoració a de ser entre 1 i 5")
        descripcioProducte = ent_descripcio.get()

        if ent_DestacatProducte.get() == "True" or ent_DestacatProducte.get() == "False":
            destacatProducte = ent_DestacatProducte.get()
        else:
            destacatProducte = "False"

        longDescripcioProducte = ent_LongDescripcio.get()
        imateProducte = ent_ImatgeProducte.get()

        if len(nomProducte) == 0 or preuProducte < 0 or len(
                descripcioProducte) == 0:
            raise Exception
    except Exception:
        lbl_Answer.config(text="Alguna dada és incorrecta")

    producteTenda = producte(nomProducte, preuProducte, descripcioProducte, longDescripcioProducte, destacatProducte,
                             valoracioProducte, imateProducte)

    myProducte = {"nom": producteTenda.nom, "preu": producteTenda.preu, "descripcio": producteTenda.descripcio,
                  "longDescripcio": producteTenda.longDescripcio, "destacat": producteTenda.destacat,
                  "valoracio": producteTenda.valoracio, "imatge": producteTenda.imatge}

    lbl_Answer.config(text="Producte afeguit correctament")
    mycol.insert_one(myProducte)
    readProducte()


def modifyProducte():
    try:

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["productesBayo"]
        mycol = mydb["productesBayo"]
        nomProducte = ""
        preuProducte = 0
        descripcioProducte = ""
        valoracioProducte = 0
        longDescripcioProducte = ""
        destacatProducte = ""
        imateProducte = ""

        lbl_Answer.config(text="")

        productesTenda.clear()

        try:
            nomProducte = ent_NomProducte.get()
            preuProducte = float(ent_PreuProducte.get())
            try:
                valoracioProducte = float(ent_ValoracioProducte.get())
                if valoracioProducte > 5 or valoracioProducte < 1:
                    raise Exception
            except Exception:
                lbl_Answer.config(text="La valoració a de ser entre 1 i 5")

            descripcioProducte = ent_descripcio.get()

            if ent_DestacatProducte.get() == "True" or ent_DestacatProducte.get() == "False":
                destacatProducte = ent_DestacatProducte.get()
            else:
                destacatProducte = "False"

            longDescripcioProducte = ent_LongDescripcio.get()
            imateProducte = ent_ImatgeProducte.get()

            if len(nomProducte) == 0 or preuProducte < 0 or len(
                    descripcioProducte) == 0:
                raise Exception
        except Exception:
            lbl_Answer.config(text="Alguna dada és incorrecta")

        product = producte(nomProducte, preuProducte, descripcioProducte, longDescripcioProducte, destacatProducte,
                           valoracioProducte, imateProducte)
        modificarProducte = [{"$set": {"nom": product.nom}}, {"$set": {"preu": product.preu}},
                             {"$set": {"descripcio": product.descripcio}},
                             {"$set": {"longDescripcio": product.longDescripcio}},
                             {"$set": {"destacat": product.destacat}}, {"$set": {"valoracio": product.valoracio}},
                             {"$set": {"imatge": product.imatge}}]

        idProducteModificar = ent_IdProducte.get()
        myquery = {"_id": ObjectId(idProducteModificar)}
        mycol.update_one(myquery, modificarProducte)
        lbl_Answer.config(text="Producte modificat correctament")
        readProducte()
    except Exception:
        lbl_Answer.config(text="Selecciona un producte")

def deleteProducte():
    try:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["productesBayo"]
        mycol = mydb["productesBayo"]
        idProducteEliminar = ent_IdProducte.get()
        myquery = {"_id": ObjectId(idProducteEliminar)}
        mycol.delete_one(myquery)
        readProducte()
    except Exception:
        lbl_Answer.config(text="Selecciona un producte")


def deleteAll():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["productesBayo"]
    mycol = mydb["productesBayo"]

    deleteProducte = mycol.delete_many({})

    lbl_Answer.config(text=str(deleteProducte.deleted_count) + " documents deleted.")

    readProducte()

def leaveGame():
    window.destroy()


window = tk.Tk()

frameProductes = tk.Frame(window)
frameProductes.pack()

ent_DestacatProducte = ttk.Combobox(frameProductes,
                                    state="readonly",
                                    values=[True, False]
                                    )
addButton = tk.Button(frameProductes,
                      text="ADD",
                      command=addProducte,
                      width="50"
                      )
modifyButton = tk.Button(frameProductes,
                         text="MODIFY",
                         command=modifyProducte,
                         width="50"
                         )
deleteButton = tk.Button(frameProductes,
                         text="DELETE",
                         command=deleteProducte,
                         width="50"
                         )
deleteAllButton = tk.Button(frameProductes,
                            text="DELETE ALL",
                            command=deleteAll,
                            width="50"
                            )
buttonGetOut = tk.Button(frameProductes,
                         text="SORTIR",
                         command=leaveGame)

ent_NomProducte = tk.Entry(frameProductes, width="50")
ent_PreuProducte = tk.Entry(frameProductes, width="50")
ent_descripcio = tk.Entry(frameProductes, width="50")
ent_LongDescripcio = tk.Entry(frameProductes, width="50")
ent_ValoracioProducte = tk.Entry(frameProductes, width="50")
ent_ImatgeProducte = tk.Entry(frameProductes, width="50")
ent_IdProducte = tk.Entry(frameProductes, width="50")

lbl_Destacat = tk.Label(frameProductes, text="Destacat", width="50", justify=tk.LEFT)
lbl_Nom = tk.Label(frameProductes, text="Nom", width="50", justify=tk.LEFT)
lbl_Preu = tk.Label(frameProductes, text="Preu", width="50", justify=tk.LEFT)
lbl_Descripcio = tk.Label(frameProductes, text="Descripció", width="50", justify=tk.LEFT)
lbl_LongDescripcio = tk.Label(frameProductes, text="Descripció llerga", width="50", justify=tk.LEFT)
lbl_Valoracio = tk.Label(frameProductes, text="Valoracio", width="50", justify=tk.LEFT)
lbl_Imatge = tk.Label(frameProductes, text="Imatge", width="50", justify=tk.LEFT)
lbl_Answer = tk.Label(frameProductes, text="", width="50", justify=tk.LEFT)

lbl_Nom.pack()
ent_NomProducte.pack()
lbl_Preu.pack()
ent_PreuProducte.pack()
lbl_Descripcio.pack()
ent_descripcio.pack()
lbl_LongDescripcio.pack()
ent_LongDescripcio.pack()
lbl_Valoracio.pack()
ent_ValoracioProducte.pack()
lbl_Imatge.pack()
ent_ImatgeProducte.pack()

lbl_Destacat.pack()
ent_DestacatProducte.pack()

addButton.pack()
modifyButton.pack()
deleteButton.pack()
deleteAllButton.pack()

tree = ttk.Treeview(frameProductes, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings', height=10)

tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="ID")

tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Nom")

tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Preu")

tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="Descripció")

tree.column("# 5", anchor=CENTER)
tree.heading("# 5", text="Descripció llarga")

tree.column("# 6", anchor=CENTER)
tree.heading("# 6", text="Destacat")

tree.column("# 7", anchor=CENTER)
tree.heading("# 7", text="Valoració")

tree.column("# 8", anchor=CENTER)
tree.heading("# 8", text="Imatge")
tree.bind('<ButtonRelease-1>', serchProducte)
tree.pack()

lbl_Answer.pack()
buttonGetOut.pack()




def readProducte():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["productesBayo"]
    mycol = mydb["productesBayo"]
    for item in tree.get_children():
        tree.delete(item)
    for x in mycol.find():
        tree.insert('', 'end', text="1", values=(
            x.get("_id"), x.get("nom"), x.get("preu"), x.get("descripcio"), x.get("longDescripcio"),
            x.get("destacat"),
            x.get("valoracio"), x.get("imatge")
        ))


readProducte()
window.mainloop()
