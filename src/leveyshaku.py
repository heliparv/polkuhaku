import time
from collections import deque
from labyrintti import Labyrintti

class Leveyshaku:
    '''Luokka leveyshaun toteuttamiseen. Metodi on esitetty muun muassa
    kurssilla Tietorakenteet ja Algoritmit'''

    def __init__(self, labyrintti: Labyrintti):
        '''Alustetaan algoritmin ja graafisen esityksen tarvitsemat rakenteet.

        polut: sanakirjarakenne, jossa läpi käydyt solmut linkitetään edelliseen
        läpikäytyyn solmuun.

        esitys: Lista, johon läpi käydyt solmut tallennetaan järjestyksessä
        algoritmin graafista esitystä varten

        oikea_polku: Lista, johon löydetty reitti tallennetaan järjestyksessä graafista
        esitystä varten.

        aika: Tallentaa hakuun kuluneen ajan reaaliaikaisena

        kierrokset: Tallentaa haussa vierailut polkuhaun sisimmässä for-loopissa'''

        self.polut = {}
        self.esitys = []
        self.laby = labyrintti
        self.oikea_polku = []
        self.aika = 0
        self.kierrokset = 0

    def hae_polku(self):
        '''Hakee reitin labyrintin läpi leveyshaku-algoritmilla.
        Tallentaa tietoa graafista esitystä ja suorituskykymittausta varten

        muuttujat:
        aloitusaika: tallentaa algoritmin suorituksen aloitusajan

        kayty: tietorakenne, jota algoritmi käyttää tarkistaessaan ettei jo
        käsiteltyjä solmuja käsitellä uudestaan

        jono: Käsiteltävät solmut asetetaan jonoon ja käsitellään algoritmissa
        samassa järjestyksessä kuin ne on lisätty jonoon

        paikka: Kulloinkin käsiteltävänä oleva solmu, sen koordinaattiesitys

        naapuri: Käsiteltävänä olevan solmun naapurit, eli solmut, joihin
        kulloisestakin paikasta pääsee liikkumaan
        '''
        aloitusaika = time.time()
        kayty = set()
        kayty.add(self.laby.labyrintti['alku'])
        jono = deque()
        jono.append(self.laby.labyrintti['alku'])
        self.esitys.append(self.laby.labyrintti['alku'])
        while jono:
            paikka = jono.popleft()
            self.esitys.append(paikka)
            for naapuri in self.laby.labyrintti[paikka]:
                self.kierrokset += 1
                if naapuri == self.laby.labyrintti['loppu']:
                    self.esitys.append(naapuri)
                    self.polut[naapuri] = paikka
                    self.aika = time.time()-aloitusaika
                    self.polun_esitys()
                    break
                if naapuri in kayty:
                    continue
                jono.append(naapuri)
                kayty.add(naapuri)
                self.polut[naapuri] = paikka

    def polun_esitys(self):
        '''Käy läpi leveyshaussa muodostetun polut-tietorakenteen, jossa
        jokainen solmu on linkitetty sitä edeltäneeseen solmuun. Tallentaa
        oikea_polku listaan leveyshaun löytämän polun käänteisessä
        järjestyksessä

        paikka: Apumuuttuja, johon tallennetaan kulloinkin käsittelyssä
        oleva solmu'''
        paikka = self.laby.labyrintti['loppu']
        self.oikea_polku.append(paikka)
        while True:
            paikka = self.polut[paikka]
            self.oikea_polku.append(paikka)
            if paikka == self.laby.labyrintti['alku']:
                break
