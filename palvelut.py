import random



class Asiakas():
    def __init__(self, nimi, ika):
        self.nimi= nimi
        self.ika = ika

    def get_nimi(self):
        return self.nimi 

    def set_nimi(self, uusinimi):
        try:
            if uusinimi != "":
                self.nimi= uusinimi
            except ValueError:
                raise ValueError("Kannattaa antaa uusi nimi")
        

    def get_ika(self):
        return self.ika

    def set_ika(self, uusi_ika):
        try:
            if uusi_ika != "":
                self.ika = uusi_ika
            except ValueError:
                raise ValueError("Kannattaa antaa uusi ikä")
        
            
    
    def _luo_nro(self):

        nro1 = random.randint(0, 9)
        nro2 = random.randint(0, 9)
        nro3 = random.randint(0, 9)
        nro4 = random.randint(0, 9)
        nro5 = random.randint(0, 9)
        nro6 = random.randint(0, 9)
        nro7 = random.randint(0, 9)
        nro8 = random.randint(0, 9)

        asiakasnro = f'{nro1}{nro2}-{nro3}{nro4}{nro5}-{nro6}{nro7}{nro8}'
        return asiakasnro

    def get_asiakasnro(self):
        return asiakasnro



class Palvelu():
    def __init__(self, tuotenimi, asiakkaat=[]):
        self.tuotenimi=tuotenimi
        self.asiakkaat=[]

    def luo_asiakasrivi(Asiakas):
        pass

    def lisaa_asiakas(Asiakas):
        asiakas = input("Anna Asiakas: ")
        if asiakas = True:
            self.asiakkaat.append(asiakas)
        elif asiakas = False:
            except ValueError:
                raise ValueError ("Kannattaa antaa uusi asiakas")
            

    def poista_asiakas(Asiakas):
        asiakas = input("Anna Asiakas: ")
        if asiakas = True:
            self.asiakkaat.remove(asiakas)
        elif asiakas = False:
            except ValueError:
                raise ValueError ("Kannattaa antaa uusi asiakas")

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
