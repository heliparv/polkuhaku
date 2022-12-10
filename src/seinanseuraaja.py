from labyrintti import Labyrintti
import time

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
        self.paikka = ''
        self.aika = 0
        self.o_aika = 0

    def hae_polku(self):
        alku = time.time()
        self.ensiaskel()
        jatketaan = True
        while jatketaan:
            jatketaan = self.hae_askel()
        loppu = time.time()
        self.aika = loppu-alku

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
        elif alku[1] == len(self.laby.ratkaisu[0])-1:
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

    def piirra_polku(self):
        self.laby.luo_ratkaisugrafiikka()
        for paikka in self.polku:
            self.laby.merkitse_kayty_paikka(self.polku[paikka])
        print('Seinänseuraaja-algoritmin löytämä polku:')
        self.laby.tulosta_ratkaisu()

    def aikavaativuus(self):
        return f"Seinänseuraaja-algoritmin suorittamiseen kului {self.aika}"

    def O_aikavaativuus(self):
        return f"Seinänseuraaja kävi läpi {self.o_aika} silmukkaa"

    def polun_pituus(self):
        return f"Seinänseuraaja-algoritmilla löydetun polun pituus on {len(self.polku)}"
