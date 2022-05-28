import random




class Asiakas():
    """Luokka asettaa asiakkaalle numeron, nimen, iän ja luo asiakasnumeron.
        Julkiset metodit
        set_nimi()
        set_ika()
        get_nimi()
        get_ika()
        get_asiakasnumero()
    """
    
    def __init__(self, nimi, ika):
        """Asiakas-luokan konstruktori, jossa annetaan muuttujat, jotka peritään myöhemmin.
        :ivar asiakasnumero: asiakkaan asiakasnumero
        :type asiakasnumero: int[]
        :ivar nimi: asiakkaan nimi
        :type nimi: str
        :ivar ika: asiakkaan ikä
        :type ika: int
        """
        self.__nimi= str(nimi)
        self.__ika = int(ika)
        self.__asiakasnro = self.__luo_nro()

    def get_nimi(self):
        return self.__nimi
        """Getteri funktio joka palauttaa nimen
        type nimi: str
        """

    def set_nimi(self, uusinimi):
            
            if uusinimi == '':
                raise ValueError("Kannattaa antaa uusi nimi.")
            else:
                self.__nimi = uusinimi
            """Setteri funktio joka asettaa nimen arvon tilalle uuden nimen
            type uusinimi: str """
        

    def get_ika(self):
        return self.__ika
        """Getteri funktio joka palauttaa Asiakkaan iän
        type ika: str"""

    def set_ika(self, uusi_ika):
        try:
            if uusi_ika != "":
                self.__ika = uusi_ika
        except ValueError:
            raise ValueError("Kannattaa antaa uusi ikä")
        """Setteri funktio joka asettaa iän arvon tilalle uuden iän
        type uusi_ika: str"""
        
            
    
    def __luo_nro(self):
        """Muodostaa kolmesta koknaisluvusta muodostuvan satunnaisen asiakasnumeron
        :ivar numerolista: lista jossa satunnaisesti generoitu asiakasnumero
        :type numerolista: int[]
        """
        nro1 = []
        nro2 = []
        nro3 = []
     
        nro1.append(random.randint(0, 99))
        nro2.append(random.randint(0, 999))
        nro3.append(random.randint(0, 999))
        
        numerolista = f'{nro1}-{nro2}-{nro3}'
        return numerolista
        """Funktio joka palauttaa 3 eri numeroa satunnaisesti 0-99 väliltä nro1 kohdalla ja 0-999 väliltä nro2 ja 3 kohdalla väliltä
        type nro1-nro8: int""" 

    def get_asiakasnro(self):
        return self.__asiakasnro
        """Getteri funktio joka palauttaa asiakasnumeron
        type asiakasnro: f-str """



class Palvelu():
    """Luokka, joka hallitsee asiakas listaa.
        Julkiset metodit
        lisaa_asiakas()
        poista_asiakas()
        tulosta_asiakkaat()
    """
    def __init__(self, tuotenimi, asiakkaat=[]):
        """Konstruktori, jossa luodaan asikkaiden tiedoille lista.
        :ivar __asiakkaat: Muuttujaan tallennetaan kaikki asiakkaiden tiedot.
        :type __asiakkaat: list
        :ivar tuotenimi: Tuotenimi tallennetaan tähän muuttujaan.
        :type tuotenimi: str
        """
        self.tuotenimi = str(tuotenimi)
        self.__asiakkaat = []

    def _luo_asiakasrivi(self, Asiakas):
         print(f'{Asiakas.get_nimi()},{Asiakas.get_asiakasnro()}, on {Asiakas.get_ika()}-vuotias')
         
         """Luo asiakasrivin käyttämällä get metodeja
        Asiakas type: class
        """

    def lisaa_asiakas(self, Asiakas):
        asiakas = Asiakas
        if asiakas == None:
            raise ValueError ("Kannattaa antaa asiakas.")
        else:
            self.__asiakkaat.append(asiakas)
        """Lisää annetun asiakkaan asiakkaat listaan ja nostaa ValueErrorin jos ei anneta asiakasta
        type asiakas:: str
        """
            

    def poista_asiakas(self, Asiakas):
        asiakas = input("Anna Asiakas: ")
        try:
            if asiakas != None:
                self.__asiakkaat.remove(asiakas)
        except:
            pass
        """Poistaa kutsuttuna asiakkaan asiakkaat-listasta. Jos ei anneta asiakasta ohitetaan virhe.
        """
        
    def tulosta_asiakkaat(self):
        print("\nTuotteen " + self.tuotenimi + " asiakkaat ovat:")
        for x in self.__asiakkaat:
            self._luo_asiakasrivi(x)
        """Tulostaa luodun asiakasrivin käyttämällä luo_asiakasrivi metodia
        """


class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi, edut=[]):
        """Konstruktori
        """
        super().__init__(tuotenimi)
        self.__edut = []

    def lisaa_etu(self, etu):
        if etu == False:
            raise ValueError ("Kannattaa antaa uusi etu")
        else:
            self.__edut.append(etu)
        """Lisää edun edut listaan ja jos ei anneta arvoa nostaa ValueErrorin
        type etu: str
        """

    def poista_etu(self, etu):
        etu = etu
        try:
            if etu == False:
                raise ValueError ("Ei voi poistaa:" + etu + ", Ei ole listassa")
            else:
                self.__edut.remove(etu)
        except:
            pass
            
            

    def tulosta_edut(self):
        print("\nTuotteen " + self.tuotenimi + " edut ovat:")
        for etu in self.__edut:
            print (f'{etu}')
            """Tulostaa _edut listasta edut
            type _edut: list
            """
