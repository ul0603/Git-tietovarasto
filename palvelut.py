import random



class Asiakas():
    def __init__(self, nimi, ika):
        self.nimi= nimi
        self.ika = ika
        



class Palvelu():
    def __init__(self, tuotenimi, asiakkaat=[]):
        self.tuotenimi=tuotenimi
        self.asiakkaat=[]



class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi, edut=[]):
        super().__init__(tuotenimi)
        self.edut=[]
