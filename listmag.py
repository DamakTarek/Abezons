from produit import Produit
from magazin import Magazin

class ListMag:
    def __init__(self):
        self.magazin_list=[]
    def add_magazins(self, magazin):
        self.magazin_list.append(magazin)
    def get_mag_list(self):
        return self.magazin_list