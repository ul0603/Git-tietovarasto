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
        """Getteri funktio joka palauttaa nimen
        type nimi: str
        """
        return self.__nimi

    def set_nimi(self, uusinimi):
        """Setteri funktio joka asettaa nimen arvon tilalle uuden nimen
            type uusinimi: str """
            
            if uusinimi == '':
                raise ValueError("Kannattaa antaa uusi nimi.")
            else:
                self.__nimi = uusinimi

    def get_ika(self):
        """Getteri funktio joka palauttaa Asiakkaan iän
        type ika: str"""
        return self.__ika
       

    def set_ika(self, uusi_ika):
        """Setteri funktio joka asettaa iän arvon tilalle uuden iän
        type uusi_ika: str"""
        try:
            if uusi_ika != "":
                self.__ika = uusi_ika
        except ValueError:
            raise ValueError("Kannattaa antaa uusi ikä")
        
        
            
    
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
    
    def get_asiakasnro(self):
        """Getteri funktio joka palauttaa asiakasnumeron
        type asiakasnro: f-string """
        return self.__asiakasnro
   



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
        """Luo asiakasrivin käyttämällä get metodeja
        Asiakas type: class
        """
         print(f'{Asiakas.get_nimi()},{Asiakas.get_asiakasnro()}, on {Asiakas.get_ika()}-vuotias')
         

    def lisaa_asiakas(self, Asiakas):
        """Lisää annetun asiakkaan asiakkaat listaan ja nostaa ValueErrorin jos ei anneta asiakasta
        type asiakas:: str
        """
        asiakas = Asiakas
        if asiakas == None:
            raise ValueError ("Kannattaa antaa asiakas.")
        else:
            self.__asiakkaat.append(asiakas)
        
            

    def poista_asiakas(self, Asiakas):
        """Poistaa annetun asiakkaan asiakkaat-listasta. Jos ei anneta asiakasta ohitetaan virhe.
        """
        asiakas = input("Anna Asiakas: ")
        try:
            if asiakas != None:
                self.__asiakkaat.remove(asiakas)
        except:
            pass
        
        
    def tulosta_asiakkaat(self):
        """Tulostaa luodun asiakasrivin käyttämällä luo_asiakasrivi metodia
        """
        print("\nTuotteen " + self.tuotenimi + " asiakkaat ovat:")
        for x in self.__asiakkaat:
            self._luo_asiakasrivi(x)
        


class ParempiPalvelu(Palvelu):
    """Luokka, jossa käsitellään tuotenimiä ja etuja.
    """
    def __init__(self, tuotenimi, edut=[]):
        """Konstruktorissa peritään tuotenimi Palvelu luokalta ja luodaan edut lista.
        """
        super().__init__(tuotenimi)
        self.__edut = []

    def lisaa_etu(self, etu):
        """Lisää edun edut listaan ja jos ei anneta arvoa nostaa ValueErrorin
        type etu: str
        """
        if etu == False:
            raise ValueError ("Kannattaa antaa uusi etu")
        else:
            self.__edut.append(etu)

    def poista_etu(self, etu):
        """Poistaa annetun edun edut listasta ja jos etua ei anneta ohitetaan virhe.
        """
        etu = etu
        try:
            if etu == False:
                raise ValueError ("Ei voi poistaa:" + etu + ", Ei ole listassa")
            else:
                self.__edut.remove(etu)
        except:
            pass
            
            

    def tulosta_edut(self):
        """Tulostaa _edut listasta edut
            type _edut: list
            """
        print("\nTuotteen " + self.tuotenimi + " edut ovat:")
        for etu in self.__edut:
            print (f'{etu}')
