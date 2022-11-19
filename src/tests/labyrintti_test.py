import unittest
from labyrintti import Labyrintti

class testLabyrintti(unittest.TestCase):
    def setUp(self):
        self.laby = Labyrintti()
    
    def test_tyhja_alustus_luo_labyrintin_grafiikan(self):
        self.assertEqual(self.laby.grafiikka[0][0], '#')
    
    def test_tyhja_alustus_luo_labyrintin_sanakirjan(self):
        if 'alku' in self.laby.labyrintti:
            alku_loytyi = True
        else:
            alku_loytyi = False
        self.assertEqual(alku_loytyi, True)
    
    def test_antaa_yhteyden_reunalta_labyrinttiin(self):
        self.assertEqual(self.laby.labyrintti['0,1'], ['1,1'])
    
    def test_annettu_labyrintti_grafiikaksi(self):
        a = ['###','A #','#B#']
        self.laby = Labyrintti(a)
        self.assertEqual(self.laby.grafiikka, a)
    
    def test_annettu_labyrintti_verkoksi(self):
        a = ['###','A #','#B#']
        self.laby = Labyrintti(a)
        self.assertEqual(self.laby.labyrintti['alku'], '1,0')
    
    def test_osaa_lukea_vasemman_reunan(self):
        a = ['###','# A','#B#']
        self.laby = Labyrintti(a)
        self.assertEqual(self.laby.labyrintti['alku'], '1,2')
    
    def test_osaa_lukea_alareunan(self):
        a = ['###','A #','#B#']
        self.laby = Labyrintti(a)
        self.assertEqual(self.laby.labyrintti['loppu'], '2,1')
