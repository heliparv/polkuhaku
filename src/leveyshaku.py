from collections import deque
from labyrintti import Labyrintti
import time

class Leveyshaku:
    '''Luokka leveyshaun toteuttamiseen'''

    def __init__(self, labyrintti: Labyrintti):
        '''alustaa sanakirjan, johon tallennetaan solmut linkitettynä
        ns käänteisessä kävelyjärjestyksessä, siirtyy ascii-hakuun,
        koska tällä hetkellä toimitaan edelleen terminaalissa
        
        polut: sanakirjarakenne, jossa solmut linkitetään edelliseen
        läpikäytyyn solmuun.
        esitys: tallentaa läpikäydyt solmut graafista esitystä varten
        aika: Tallentaa hakuun kuluneen ajan'''
        self.polut = {}
        self.esitys = []
        self.laby = labyrintti
        self.aika = 0
        self.pituus = 0
        self.hae_polku_ascii()    

    def hae_polku_ascii(self):
        '''Hakee leveyshaulla reitin, tulostaa mennessään esityksen
        käydyistä lattiaruuduista. Kun loppu on löydetty, siirtyy
        tulostamaan reitin'''
        self.laby.luo_ratkaisugrafiikka()
        alku = time.time()
        kayty = set()
        kayty.add(self.laby.labyrintti['alku'])
        jono = deque()
        jono.append(self.laby.labyrintti['alku'])
        valmis = False
        while not valmis:
            paikka = jono.popleft()
            for naapuri in self.laby.labyrintti[paikka]:
                if naapuri == self.laby.labyrintti['loppu']:
                    valmis = True
                    self.polut[naapuri] = paikka
                    loppu = time.time()
                    self.aika = loppu-alku
                    self.laby.tulosta_ratkaisu()
                    self.esita_kaydyt_paikat()
                    self.esita_polku_ascii(naapuri)
                    break
                if naapuri in kayty:
                    continue
                jono.append(naapuri)
                kayty.add(naapuri)
                self.polut[naapuri] = paikka

    def hae_polku(self):
        '''Hakee leveyshaulla reitin, talentaa mennessään listan
        käydyistä lattiaruuduista'''
        kayty = set()
        kayty.add(self.laby.labyrintti['alku'])
        jono = deque()
        jono.append(self.laby.labyrintti['alku'])
        self.esitys.append(self.laby.labyrintti['alku'])
        valmis = False
        while not valmis:
            paikka = jono.popleft()
            self.esitys.append(paikka)
            for naapuri in self.laby.labyrintti[paikka]:
                if naapuri == self.laby.labyrintti['loppu']:
                    valmis = True
                    self.polut[naapuri] = paikka
                    break
                if naapuri in kayty:
                    continue
                jono.append(naapuri)
                kayty.add(naapuri)
                self.polut[naapuri] = paikka

    def esita_kaydyt_paikat(self):
        self.laby.luo_ratkaisugrafiikka()
        for solmu in self.esitys:
            self.laby.merkitse_kayty_paikka()
        print('Leveyshaussa vieraillut solmut:')
        self.laby.tulosta_ratkaisu()


    def esita_polku_ascii(self, loppu):
        '''Luo esityksen löydetystä lyhyimmästä polusta ja
        kertoo sen pituuden'''
        self.laby.luo_ratkaisugrafiikka()
        paikka = loppu
        while True:
            paikka = self.polut[paikka]
            self.pituus += 1
            if paikka == self.laby.labyrintti['alku']:
                break
            self.laby.merkitse_kayty_paikka(paikka)
        print("Leveyshaun löytämä ratkaisu:")
        self.laby.tulosta_ratkaisu()

    def aikavaativuus(self):
        return f"Leveyshaun suorittamiseen kului {self.aika}"

    def O_aikavaativuus(self):
        return f"Annetuista {len(self.laby.labyrintti)} solmusta leveyshaku kävi läpi {len(self.esitys)}"

    def polun_pituus(self):
        return f"Leveyshaulla löydetun polun pituus on {self.pituus}"
