import unittest
from labyrintti import Labyrintti
from seinanseuraaja import Seinanseuraaja

class Seinanseuraaja(unittest.TestCase):
    '''Testataan, että leveyshaku-algoritmi toimii kuten kuuluu'''
    def setUp(self):
        laby = Labyrintti(['#A#',
                           '# B',
                           '###'])
        self.haku = Seinanseuraaja(laby.grafiikka)
        self.haku.hae_polku()

    def test_haku_suoritetaan(self):
        '''Testaa, että haun suorituksen seurauksena ilmestyy tietorakenne löydetystä polusta'''
        self.assertGreater(len(self.haku.polku), 0)

    def test_haku_tuottaa_kayttoliittymalle_esitysta_varten_seinakosketukset(self):
        '''Tarkistaa, että graafista käyttöliittymää varten luodussa seinäkosketukset
        tietorakenteessa on olemassa tieto että jotain seiniä on hipelöity'''
        self.assertGreater(len(self.haku.seinakosketukset), 1)

    def test_algoritmin_ajankaytto_mitataan(self):
        '''Varmistaa, että algoritmin reaaliaikainen ajankäyttö on mitattu'''
        self.assertNotEqual(len(self.haku.aika), 0)

    def test_algoritmin_kierrokset_mitataan(self):
        '''Varmistaa, että algoritmin käymät kierrokset sisimmärrä for-loopissa lasketaan jotenkin'''
        self.assertNotEqual(len(self.haku.kierrokset), 0)