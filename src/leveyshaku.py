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
        oikea_polku: koska polut-rakenne tallentaa kaikki mahdolliset polut, on
        löydetty polku käytännöllistä hakea erilleen muita funktioita varten
        aika: Tallentaa hakuun kuluneen ajan reaaliaikaisena
        o_aika: Tallentaa hakuun käytetyt vierailut polkuhaun sisimmässä
        for-loopissa, joten saadaan O()-muotoinen aikavaativuus'''

        self.polut = {}
        self.esitys = []
        self.laby = labyrintti
        self.oikea_polku = {}
        self.aika = 0
        self.o_aika = 0

    def hae_polku_ascii(self):
        '''Käyttää funktiota hae_polku reitin löytämiseen, tulostaa
        lopuksi esityksen käydyistä lattiaruuduista. Kun loppu on löydetty,
        tulostaa reitin'''

        self.laby.luo_ratkaisugrafiikka()
        self.hae_polku()
        self.laby.tulosta_ratkaisu()
        self.esita_kaydyt_paikat_ascii()
        self.esita_polku_ascii()

    def hae_polku(self):
        '''Hakee leveyshaulla reitin, talentaa mennessään listan
        käydyistä lattiaruuduista'''
        alku = time.time()
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
                self.o_aika += 1
                if naapuri == self.laby.labyrintti['loppu']:
                    valmis = True
                    self.polut[naapuri] = paikka
                    loppu = time.time()
                    self.aika = loppu-alku
                    self.polun_esitys()
                    break
                if naapuri in kayty:
                    continue
                jono.append(naapuri)
                kayty.add(naapuri)
                self.polut[naapuri] = paikka

    def polun_esitys(self):
        paikka = self.laby.labyrintti['loppu']
        while True:
            seuraava = self.polut[paikka]
            self.oikea_polku[paikka] = seuraava
            paikka = seuraava
            if paikka == self.laby.labyrintti['alku']:
                break

    def esita_kaydyt_paikat_ascii(self):
        self.laby.luo_ratkaisugrafiikka()
        for solmu in self.esitys:
            self.laby.merkitse_kayty_paikka(solmu)
        print('Leveyshaussa vieraillut solmut:')
        self.laby.tulosta_ratkaisu()


    def esita_polku_ascii(self):
        '''Luo esityksen löydetystä lyhyimmästä polusta ja
        kertoo sen pituuden'''
        self.laby.luo_ratkaisugrafiikka()
        paikka = self.laby.labyrintti['loppu']
        for solmu in self.oikea_polku:
            self.laby.merkitse_kayty_paikka(solmu)
        print("Leveyshaun löytämä ratkaisu:")
        self.laby.tulosta_ratkaisu()

    def aikavaativuus(self):
        return f"Leveyshaun suorittamiseen kului {self.aika}"

    def O_aikavaativuus(self):
        return f"Leveyshaku kävi läpi {self.o_aika} silmukkaa"

    def polun_pituus(self):
        return f"Leveyshaulla löydetun polun pituus on {len(self.oikea_polku)}"
