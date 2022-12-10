import unittest
from labyrintti import Labyrintti

class testLabyrintti(unittest.TestCase):
    '''Testaa labyrintteja käsittelevää luokkaa'''

    def setUp(self):
        '''Luo testattavan luokan mukaisen olion'''
        self.laby = Labyrintti()
    
    def test_tyhja_alustus_luo_labyrintin_grafiikan(self):
        '''Tarkistaa, että alustetulla luokalla on labyrintin
        grafiikka testaamalla että vasemmassa yläkulmassa on
        seinäruutu'''
        self.assertEqual(self.laby.grafiikka[0][0], '#')
    
    def test_tyhja_alustus_luo_labyrintin_verkkoesityksen(self):
        '''Kun alustetaan luokka antamatta grafiikkaa, luo luokka
        sen olemassaolevasta labyrinttigrafiikasta verkkoestyksen,
        eli testataan verkkoesityksen olevan olemassa'''
        if 'alku' in self.laby.labyrintti:
            alku_loytyi = True
        else:
            alku_loytyi = False
        self.assertEqual(alku_loytyi, True)
    
    def test_antaa_yhteyden_reunalta_labyrinttiin(self):
        '''Tarkistaa, että labyrintin reunalla olevasta alkusolmusta on
        yhteys labyrintin sisään kutsumalla labyrintin verkkoesitystä 
        alkusolmun koordinaatilla ja katsomalla vastauksen olevan se
        ainoa mahdollinen yhteys labyrintin sisään'''
        self.assertEqual(self.laby.labyrintti[(0,1)], [(1,1)])
    
    def test_annettu_labyrintti_grafiikaksi(self):
        '''Tarkistaa että jos labyrintin alustaa antaen sille grafiikan,
        on kyseinen grafiikka tallennettu luokan grafiikkamuuttujaan'''
        a = ['###','A #','#B#']
        self.laby = Labyrintti(a)
        self.assertEqual(self.laby.grafiikka, a)
    
    def test_annettu_labyrintti_verkoksi(self):
        '''Tarkistaa, että annetusta grafiikasta luodaan verkko,
        muttei verkon oikeellisuutta.'''
        a = ['###','A #','#B#']
        self.laby = Labyrintti(a)
        self.assertEqual(self.laby.labyrintti['alku'], (1,0))
    
    def test_osaa_lukea_vasemman_reunan(self):
        '''Tarkistaa, että myös vasemmassa reunassa olevan alkusolmun
        havaitseminen onnistuu'''
        a = ['###','# A','#B#']
        self.laby = Labyrintti(a)
        self.assertEqual(self.laby.labyrintti['alku'], (1,2))
    
    def test_osaa_lukea_alareunan(self):
        '''Tarkistaa, että labyrintti havaitsee alareunassa olevan
        loppusolmun, eli samalla havaitaanko loppusolmu'''
        a = ['###','A #','#B#']
        self.laby = Labyrintti(a)
        self.assertEqual(self.laby.labyrintti['loppu'], (2,1))
