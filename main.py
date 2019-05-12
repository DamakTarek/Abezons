from client import Client
from admin import Admin
from produit import Produit
from magazin import Magazin
from loginservice import LoginService
from listmag import ListMag
# hassen = Client("Hama", "Hama", "haa", "aze","5421")
# print(hassen.get_login())
# hassen.set_login("Maha")
# print(hassen.get_login())
# print(hassen.get_cb())

tarek = Client("Tarek", "Tarek", "haa", "aze","admin")
fedy = Client("Fedy", "Fedy", "haa", "aze", "client")
l1 = LoginService()
l1.add_users(tarek)
l1.add_users(fedy)
m1 = Magazin("ABezon","Kleber")
m2 = Magazin("Amazon","USA")
p1 = Produit(1, "Iphone", "Phone", "900", 10)
p2 = Produit(2, "Sa", "Phone", "1000", 50)
p3 = Produit(3, "ISA", "Phone", "900", 0)
p4 = Produit(4, "eyo", "Phone", "900",20)

m1.add_product(p1)
m1.add_product(p3)
m2.add_product(p2)
m2.add_product(p4)

connected = 0

mag=ListMag()
mag.add_magazins(m1)
mag.add_magazins(m2)
while connected == 0:
    login=input("enter login")
    password=input("enter passs")
    connected = l1.login(login,password)

if connected == 1:
    for magazin in mag.get_mag_list():
        print(magazin.get_nom())
        magazin.list_products()
while choice != 0:
    choice = input("Choose your product")
    for

# print(hassen.get_login())
# hassen.set_login("Maha")
# print(hassen.get_login())
# print(hassen.get_grade())
# print(p1.get_magazin())

#
#
#
# m1.add_product(p1)
# m1.add_product(p2)
# m1.add_product(p3)
# m1.list_products()