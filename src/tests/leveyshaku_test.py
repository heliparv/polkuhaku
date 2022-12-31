import unittest
from labyrintti import Labyrintti
from leveyshaku import Leveyshaku

class testLeveyshaku(unittest.TestCase):
    '''Testataan, että leveyshaku-algoritmi toimii kuten kuuluu'''
    def setUp(self):
        laby = Labyrintti(['#A#',
                           '# B',
                           '###'])
        self.haku = Leveyshaku(laby.grafiikka)
        self.haku.hae_polku()

    def test_haku_suoritetaan(self):
        '''Tarkistaa, että haun jälkeen on olemassa tietorakenne mahdollisia polkuja'''
        self.assertGreater(len(self.haku.polut), 0)

    def test_haku_tuottaa_kayttoliittymalle_esitysta_varten_tarkistetut_solmut(self):
        '''Tarkistaa, että haun jälkeen graafista esitystä varten on tallennettu että joissain solmuissa on vierailtu'''
        self.assertGreater(len(self.haku.esitys), 0)

    def test_haku_tuottaa_kayttoliittymalle_esitysta_varten_valitun_polun(self):
        '''Tarkistaa, että haun jälkeen graafista esitystä varten on olemassa esitys mikä polku valittiin'''
        self.assertGreater(len(self.haku.oikea_polku), 0)

    def test_algoritmin_ajankaytto_mitataan(self):
        '''Varmistaa, että algoritmin reaaliaikainen ajankäyttö on mitattu'''
        self.assertNotEqual(self.haku.aika, 0)

    def test_algoritmin_kierrokset_mitataan(self):
        '''Varmistaa, että algoritmin käymät kierrokset sisimmärrä for-loopissa lasketaan jotenkin'''
        self.assertNotEqual(self.haku.kierrokset, 0)