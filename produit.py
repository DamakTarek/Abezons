class Produit:
    def __init__(self,id, nom, categorie, prix, quantity ):
        self.nom = nom
        self.categorie = categorie
        self.prix = prix
        self.id = id
        self.quantity=quantity
        self.magazin = ""
    def get_categorie(self):
        return self.categorie
    def get_prix(self):
        return self.prix
    def set_prix(self,prix):
        self.prix = prix
    def set_categorie(self,categorie):
        self.categorie = categorie
    def get_nom(self):
        return self.nom
    def set_nom(self,nom):
        self.nom = nom
    def set_magazin(self, magazin):
        self.magazin= magazin
    def get_magazin(self):
        return self.magazin
    def get_quantity(self):
        return self.quantity
    def get_id(self):
        return self.id
    def set_quantity(self,quantity):
        self.quantity = quantity

