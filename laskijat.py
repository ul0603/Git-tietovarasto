class Laskija:
    """Luokka, joka toteuttaa eri laskutoimituksia.
    Julkiset metodit:
        summaa(Union[int, float], Union[int, float])
        kerro(Union[int, float], Union[int, float])
    """

    def summaa(self, *numerot):
        """Palauttaa kahden luvun summan.
        :param a: summan ensimmäinen luku
        :type a: Union[int, float]
        :param b: summan toinen luku
        :type b: Union[int, float]
        :return: lukujen a ja b summa
        :rtype: Union[int, float]
        """
        return sum([*numerot])

    def kerro(self, *numerot):
        """Palauttaa kahden luvun tulon.
        :param a: tulon ensimmäinen luku
        :type a: Union[int, float]
        :param b: tulon toinen luku
        :type b: Union[int, float]
        :return: lukujen a ja b tulo
        :rtype: Union[int, float]
        """
        tulo = 1
        for luku in [*numerot]:
            tulo *= luku
        return tulo


### Lisää MonenLaskija ja argumenttien_tulostaja tähän.
class MonenLaskija(Laskija):
    """Luokka, joka toteuttaa eri laskutoimituksia mille tahansa määrälle lukuja.
    Julkiset metodit:
        summaa(Union[int, float], Union[int, float])
        kerro(Union[int, float], Union[int, float])
    """

    def summaa(self, *numerot):
        """Palauttaa annettujen lukujen summan.

        :type numerot: tuple[Union[int, float]
        :return: numeroiden summa
        :rtype: Union[int, float]
        """
        return sum(numerot)

    def kerro(self, *numerot):
        """Palauttaa annettujen luvut kerrottuna.

        :param numerot: tulon numerot
        :type numerot: tuple[Union[int, float]
        :return: numeroiden tulo
        :rtype: Union[int, float]
        """
        tulo = 1
        for luku in [*numerot]:
            tulo *= luku
        return tulo


def argumenttien_tulostaja(**kwargs):
    """Tulostaa annetut tiedot"""
    for k, v in kwargs.items():
        print(f'Argumentin "{k}" arvo on {v}.')
    




### Seuraavat rivit tekevät tarkistustulostukset. Älä koske niihin.

l = Laskija()
ml = MonenLaskija()

print(l.summaa(11, 31))
print(l.kerro(3, 12))
print()
print(ml.summaa(1, 2, 3, 4, 5))
print(ml.kerro(1, 2, 3, 4, 5))
print()
print(ml.summaa(1, 2, 3, 4, 5, 6, 7))
print(ml.kerro(1, 2, 3, 4, 5, 6 ,7))
print()
argumenttien_tulostaja(eka=42, toka='foo', kolmas=[0, 1, 2])
print()
argumenttien_tulostaja(nimi='Tero', ika=41, kaupunki='Turku', oppilaitos='TAI')

