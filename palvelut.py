import random



class Asiakas():
    """Luokka, joka kuvaa Asiakkaan.
    :ivar nimi: Asiakkaan nimi
    :type nimi: str
    :ivar ika: Asiakkaan ikä
    :type ika: int
    """
    
    def __init__(self, nimi, ika):
        """Konstruktori
        """
        self.nimi= str(nimi)
        self.ika = int(ika)
        self.asiakasnro = []

    def get_nimi(self):
        return self.nimi
        """Getteri funktio joka palauttaa nimen
        type nimi: str
        """

    def set_nimi(self, uusinimi):
        try:
            if uusinimi != "":
                self.nimi= uusinimi
        except ValueError:
            raise ValueError("Kannattaa antaa uusi nimi")
        """Setteri funktio joka asettaa nimen arvon tilalle uuden nimen
        type uusinimi: str
        """
        

    def get_ika(self):
        return self.ika
        """Getteri funktio joka palauttaa Asiakkaan iän
        type ika: str"""

    def set_ika(self, uusi_ika):
        try:
            if uusi_ika != "":
                self.ika = uusi_ika
        except ValueError:
            raise ValueError("Kannattaa antaa uusi ikä")
        """Setteri funktio joka asettaa iän arvon tilalle uuden iän
        type uusi_ika: str"""
        
            
    
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
        """Funktio joka palauttaa 8 eri numeroa satunnaisesti 0 ja 9 väliltä
        type nro1-nro8: int""" 

    def get_asiakasnro(self):
        return self.asiakasnro
        """Getteri funktio joka palauttaa asiakasnumeron
        type asiakasnro: str f"""



class Palvelu():
    def __init__(self, tuotenimi, asiakkaat=[]):
        """Konstruktori
        """
        self.tuotenimi = str(tuotenimi)
        self.asiakkaat = []

    def _luo_asiakasrivi(self, Asiakas):
         print(f'{Asiakas.get_nimi()},{Asiakas.get_asiakasnro()}, on {Asiakas.get_ika()}-vuotias')
         
         """Luo asiakasrivin käyttämällä get metodeja
        Asiakas type: class
        """

    def lisaa_asiakas(self, Asiakas):
        asiakas = Asiakas
        try:
            if asiakas != None:
                self.asiakkaat.append(asiakas)
        except ValueError:
            raise ValueError ("Kannattaa antaa uusi asiakas")
        """Lisää annetun asiakkaan asiakkaat listaan ja nostaa ValueErrorin jos ei anneta asiakasta
        type asiakas:: str
        """
            

    def poista_asiakas(self, Asiakas):
        asiakas = input("Anna Asiakas: ")
        try:
            if asiakas != None:
                self.asiakkaat.remove(asiakas)
        except ValueError:
            raise ValueError ("Kannattaa antaa uusi asiakas")
        """Poistaan annetun asiakkaan asiakaat listasta ja nostee ValueErrorin jos ei anneta asiakasta
        type asiakas: str
        """

    def tulosta_asiakkaat(self):
        for x in self.asiakkaat:
            self._luo_asiakasrivi(x)
        """Tulostaa luodun asiakasrivin käyttämällä luo_asiakasrivi metodia
        """


class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi, edut=[]):
        """Konstruktori
        """
        super().__init__(tuotenimi)
        self.edut = []

    def lisaa_etu(self, etu):
        try:
            if etu == True:
                self.edut.append(self, etu)
        except ValueError:
            raise ValueError ("Kannattaa antaa uusi etu")
        """Lisää edun edut listaan ja jos ei anneta arvoa nostaa ValueErrorin
        type etu: str
        """

    def poista_etu(self, etu):
        etu = etu
        try:
            if etu == True:
                self.edut.remove(asiakas)
        except ValueError:
            raise ValueError ("Kannattaa antaa uusi etu")
        """Poistaa edun edut listasta ja jos ei anneta arvoa nostaa ValueErrorin
        type etu: str
        """

    def tulosta_edut(self):
        for etu in self.edut:
            print(etu)
        """Tulostaa edut listan
        type edut: list
        """

