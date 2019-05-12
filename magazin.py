
class Magazin:

    def __init__(self, nom, addresse):
        self.nom = nom
        self.addresse = addresse
        self.produits = []
    def __str__(self):
        return self.get_nom() + "  ," + self.get_addresse()
    def get_addresse(self):
        return self.addresse
    def get_nom(self):
        return self.nom
    def set_addresse(self,addresse):
        self.addresse = addresse
    def set_nom(self,nom):
        self.nom = nom
    def add_product(self,product):
        self.produits.append(product)
    def list_products(self):
        for produit in self.produits:
            print("Name "+ produit.get_nom() + " ID"  + produit.get_id() +"quantity  "+ produit.get_quantity())
