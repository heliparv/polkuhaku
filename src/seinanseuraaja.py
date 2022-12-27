import time
from labyrintti import Labyrintti

class Seinanseuraaja:
    '''Luokka seinänseuraajaalgoritmin toteuttamiseen.
    Seuraa oikeanpuoleista seinää, eli kääntyy aina oikealle kun voi.'''

    def __init__(self, labyrintti: Labyrintti):
        '''alustaa reitin hakuun tarvittavat tietorakenteet ja siirtyy hakuun.
        polku: tallentaa reitin käänteisessä järjestyksessä ja sitä käytetään apurakenteena
        laby: tallentaa labyrinttiolion, jossa labyrintin käsittelevät funktiot
        seinanhakija: sanakirjarakenne, jota käytetään tarkistamaan mihin seuraava askel kohdistuu,
        esitys on suhteellinen koordinaatti verrattuna nykyiseen ruutuun.
        paikka: tallentaa missä ruudussa ollaan nyt'''

        self.polku = {}
        self.laby = labyrintti
        self.seinanhakija = {(-1,-1):(0,-1),(0,-1):(1,-1),(1,-1):(1,0),
        (1,0):(1,1),(1,1):(0,1),(0,1):(-1,1),(-1,1):(-1,0),(-1,0):(-1,-1)}
        self.seinakosketukset = [(-1,-1)]
        self.polkuesitys = []
        self.paikka = ''
        self.aika = 0
        self.o_aika = 0

    def hae_polku(self):
        '''Funktio, joka suorittaa tavallisen seinänseuraaja-algoritmin.
        Mittaa suoritusajan, ei tallenna aputietorakenteita graafista esitystä varten'''
        aloitusaika = time.time()
        self.ensiaskel()
        jatketaan = True
        while jatketaan:
            jatketaan = self.hae_askel()
        lopetusaika = time.time()
        self.aika = lopetusaika-aloitusaika

    def hae_graafinen_polku(self):
        '''Funktio suorittaa seinänseuraaja-algoritmin niin, että tallentaa
        aputietorakenteita graafista esitystä varten'''
        self.polkuesitys.append(self.laby.labyrintti['alku'])
        self.ensiaskel()
        self.seinakosketukset.append((-1,-1))
        self.polkuesitys.append(self.paikka)
        jatketaan = True
        while jatketaan:
            jatketaan = self.hae_askel_grafiikalla()

    def ensiaskel(self):
        '''Tarkistaa millä reunalla labyrintin alku on ja ottaa ensimmäisen askeleen
        Labyrintissa ei olisi reittiä jos alun reunanaapuri ei olisi vapaa, joten
        tarkistetaan vain voidaanko lähteä vinoon oikealle kääntyen vai mennäänkö
        suoraan eteen.
        Vaiheet: 1.Määritä millä seinällä alku on ja sen perusteella vino oikea
        2. Katso voiko vinoon oikealle mennä
        3. Mene vinoon oikealle tai suoraan eteen, tulosta ratkaisu'''

        alku = self.laby.labyrintti['alku']
        if alku[1] == 0:
            vino_oikea = (1,1)
        elif alku[1] == len(self.laby.grafiikka[0])-1:
            vino_oikea = (-1,-1)
        elif alku[0] == 0:
            vino_oikea = (1,-1)
        else:
            vino_oikea = (-1,1)

        koordinaatti = (alku[0]+vino_oikea[0], alku[1]+vino_oikea[1])
        if koordinaatti in self.laby.labyrintti[alku]:
            self.polku[koordinaatti] = alku
            self.paikka = koordinaatti
        else:
            self.seinakosketukset.append(koordinaatti)
            koordinaatti = (alku[0]+self.seinanhakija[vino_oikea][0],alku[1]+self.seinanhakija[vino_oikea][1])
            self.polku[koordinaatti] = alku
            self.paikka = koordinaatti

    def hae_askel(self):
        '''Hakee seuraavan askeleen hyödyntäen seinänhakijaa.

        Seinänhakijalle syötetty hakusuunta-muuttuja on suhteellinen koordinaattisiirtymä
        nykyisestä paikasta edelliseen solmuun ja ns. siirtymäkompassia lähdetään
        tarkistamaan tästä vastapäivään'''

        hakusuunta = (self.polku[self.paikka][0]-self.paikka[0], self.polku[self.paikka][1]-self.paikka[1])
        while True:
            self.o_aika += 1
            hakusuunta = self.seinanhakija[hakusuunta]
            hakukoord = (self.paikka[0]+hakusuunta[0], self.paikka[1]+hakusuunta[1])
            if hakukoord not in self.laby.labyrintti[self.paikka]:
                continue
            break
        self.polku[hakukoord] = self.paikka
        self.paikka = hakukoord
        if self.paikka == self.laby.labyrintti['loppu']:
            return False
        return True

    def hae_askel_grafiikalla(self):
        '''Hakee seuraavan askeleen hyödyntäen seinänhakijaa.

        Toimii kuten hae_askel, mutta tallentaa seinäkosketukset.'''

        hakusuunta = (self.polku[self.paikka][0]-self.paikka[0], self.polku[self.paikka][1]-self.paikka[1])
        while True:
            self.o_aika += 1
            hakusuunta = self.seinanhakija[hakusuunta]
            hakukoord = (self.paikka[0]+hakusuunta[0], self.paikka[1]+hakusuunta[1])
            if hakukoord not in self.laby.labyrintti[self.paikka]:
                self.seinakosketukset.append(hakukoord)
                continue
            break
        self.polku[hakukoord] = self.paikka
        self.polkuesitys.append(hakukoord)
        self.seinakosketukset.append((-1,-1))
        self.paikka = hakukoord
        if self.paikka == self.laby.labyrintti['loppu']:
            return False
        return True

    def piirra_polku(self):
        self.laby.luo_ratkaisugrafiikka()
        for paikka in self.polku:
            self.laby.merkitse_kayty_paikka(self.polku[paikka])
        print('Seinänseuraaja-algoritmin löytämä polku:')
        self.laby.tulosta_ratkaisu()

    def aikavaativuus(self):
        return f"Seinänseuraaja-algoritmin suorittamiseen kului {self.aika}"

    def o_aikavaativuus(self):
        return f"Seinänseuraaja kävi läpi {self.o_aika} silmukkaa"

    def polun_pituus(self):
        return f"Seinänseuraaja-algoritmilla löydetun polun pituus on {len(self.polku)}"
