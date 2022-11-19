from collections import deque
from labyrintti import Labyrintti

class Leveyshaku:
    '''Luokka leveyshaun toteuttamiseen'''

    def __init__(self, labyrintti: Labyrintti):
        '''alustaa sanakirjan, johon tallennetaan solmut linkitettynä
        ns käänteisessä kävelyjärjestyksessä, siirtyy hakuun'''
        self.polut = {}
        self.laby = labyrintti
        self.laby.luo_ratkaisugrafiikka()
        self.hae_polku()
    
    def hae_polku(self):
        '''Hakee leveyshaulla reitin, tulostaa mennessään esityksen
        käydyistä lattiaruuduista. Kun loppu on löydetty, siirtyy
        tulostamaan reitin'''
        kayty = set()
        kayty.add(self.laby.labyrintti['alku'])
        jono = deque()
        jono.append(self.laby.labyrintti['alku'])
        print('Leveyshaku alkaa')
        while jono:
            paikka = jono.popleft()
            for naapuri in self.laby.labyrintti[paikka]:
                if naapuri == self.laby.labyrintti['loppu']:
                    self.polut[naapuri] = paikka
                    self.laby.merkitse_kayty_paikka(naapuri)
                    self.laby.tulosta_ratkaisu()
                    #self.esita_polku(naapuri)
                if naapuri in kayty:
                    continue
                jono.append(naapuri)
                kayty.add(naapuri)
                self.polut[naapuri] = paikka
                self.laby.merkitse_kayty_paikka(naapuri)
                self.laby.tulosta_ratkaisu()

    def esita_polku(self, loppu):
        '''Luo esityksen löydetystä lyhyimmästä polusta ja
        kertoo sen pituuden'''
        self.laby.luo_ratkaisugrafiikka()
        pituus = 0
        paikka = loppu
        #while True:
        #    paikka = self.laby.labyrintti[paikka]
        #    pituus += 1
        #    if paikka == self.laby.labyrintti['alku']:
        #        break
        #    self.laby.merkitse_kayty_paikka(paikka)
        print(f'Löydetyn polun pituus on {pituus}')
        self.laby.tulosta_ratkaisu()