import component1 as c
import comanda

c1 = comanda.comanda(1, 100, 5)
c2 = comanda.comanda(2, 1, 1)
c3 = comanda.comanda(3, 2, 2)
#
# c.saveObject(c1, "comandes.bin")
# c.saveObject(c2, "comandes.bin")
# c.saveObject(c3, "comandes.bin")
a = c.restoreObject(1, "comandes.bin")
c4 = comanda.comanda(1, 10, 10)

# a = c.UpdateObject(1, "comandes.bin", c4)
print(a.idproducte)


# a = c.removeObject(1, "comandes.bin")


# a = c.RemoveFile("comandes.bin")
# a.totalprice()
