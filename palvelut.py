import random



class Asiakas():
    def __init__(self, nimi, ika):
        self.nimi= nimi
        self.ika = ika

    def _luo_nro(self):

        nro1 = random.randint(0, 9)
        nro2 = random.randint(0, 9)
        nro3 = random.randint(0, 9)
        nro4 = random.randint(0, 9)
        nro5 = random.randint(0, 9)
        nro6 = random.randint(0, 9)
        nro7 = random.randint(0, 9)
        nro8 = random.randint(0, 9)
        return f'{nro1}{nro2}-{nro3}{nro4}{nro5}-{nro6}{nro7}{nro8}'



class Palvelu():
    def __init__(self, tuotenimi, asiakkaat=[]):
        self.tuotenimi=tuotenimi
        self.asiakkaat=[]

    def luo_asiakasrivi(Asiakas):
        pass

    def lisaa_asiakas(Asiakas):
        pass

    def poista_asiakas(Asiakas):
        pass

    def tulosta_asiakkaat():
        pass



class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi, edut=[]):
        super().__init__(tuotenimi)
        self.edut=[]

    def lisaa_etu():
        pass

    def poista_etu():
        pass

    def tulosta_edut():
        pass
