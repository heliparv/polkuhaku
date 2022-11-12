import unittest
from labyrintti import Labyrintti

class testLabyrintti(unittest.TestCase):
    def setUp(self):
        self.laby = Labyrintti()
    
    def test_tyhja_alustus_luo_labyrintin_grafiikan(self):
        laby = self.laby.anna_grafiikka()
        self.assertEqual(laby[0][0], '#')
    
    def test_tyhja_alustus_luo_labyrintin_sanakirjan(self):
        laby = self.laby.anna_labyrintti()
        if 'alku' in laby:
            alku_loytyi = True
        else:
            alku_loytyi = False
        self.assertEqual(alku_loytyi, True)
    