import pymongo
from jinja2 import Environment, FileSystemLoader


def connectar():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["productesBayo"]
    mycol = mydb["productesBayo"]
    return mycol


def implementaPlantilla(productes):
    enviroment = Environment(loader=FileSystemLoader("template/"))
    template = enviroment.get_template("botigaBayo.html")
    contingut = template.render(productes)
    return contingut


def implementaPlantillaInfoProducte(productes):
    enviroment = Environment(loader=FileSystemLoader("template/"))
    template = enviroment.get_template("infoProducte.html")
    contingut = template.render(productes)
    return contingut


def implementaPlantillaAbout(productes):
    enviroment = Environment(loader=FileSystemLoader("template/"))
    template = enviroment.get_template("about.html")
    contingut = template.render(productes)
    return contingut
