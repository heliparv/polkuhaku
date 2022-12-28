import time
from labyrintti import Labyrintti

class Seinanseuraaja:
    '''Luokka seinänseuraajaalgoritmin toteuttamiseen. Algoritmi on
    luotu perustuen ajatukseen siitä, että kun labyrintin alku- ja
    loppukohta ovat labyrintin reunoilla, voi alusta kulkea loppuun
    seuraamalla joko vasemmanpuoleista tai oikeanpuoleista seinää.
    Tämä algoritmi seuraa oikeanpuoleista seinää.'''

    def __init__(self, labyrintti: Labyrintti):
        '''Alustaa algoritmin ja graafisen käyttöliittymän käyttämät tietorakenteet

        polku: lista, jossa kuljetut solmut esitetään järjestyksessä

        laby: tallentaa labyrinttiolion, jossa ovat labyrintin käsittelevät funktiot

        seinanhakija: sanakirjarakenne, jota käytetään tarkistamaan mihin seuraava askel kohdistuu,
        esitys on suhteellinen koordinaatti verrattuna nykyiseen ruutuun.

        seinakosketukset: Tallentaa järjestyksessä kunkin seinänhakijalla tarkastetun suunnan,
        johon ei siirrytty, jotta ne osataan esittää graafisesti. Tallentaa koordinaatin (-1,-1)
        merkkinä siitä, että seuraava askel on löytynyt, tätä käytetään graafisessa esityksessä siirtymissä.

        aika: Tallentaa reaaliaikaisen suoritusajan

        kierrokset: Tallentaa algoritmissa käydyt kierrokset sisimmässä silmukassa

        '''

        self.polku = []
        self.laby = labyrintti
        self.seinanhakija = {(-1,-1):(0,-1),(0,-1):(1,-1),(1,-1):(1,0),
        (1,0):(1,1),(1,1):(0,1),(0,1):(-1,1),(-1,1):(-1,0),(-1,0):(-1,-1)}
        self.seinakosketukset = [(-1,-1)]
        self.aika = 0
        self.kierrokset = 0

    def hae_polku(self):
        '''Funktio, joka suorittaa tavallisen seinänseuraaja-algoritmin.
        Mittaa suoritusajan, ei tallenna aputietorakenteita graafista esitystä varten'''
        aloitusaika = time.time()
        self.polku.append(self.laby.labyrintti['alku'])
        self.ensiaskel()
        jatketaan = True
        while jatketaan:
            jatketaan = self.hae_askel()
        lopetusaika = time.time()
        self.aika = lopetusaika-aloitusaika

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
            self.polku.append(koordinaatti)
        else:
            self.seinakosketukset.append(koordinaatti)
            koordinaatti = (alku[0]+self.seinanhakija[vino_oikea][0],alku[1]+self.seinanhakija[vino_oikea][1])
            self.polku.append(koordinaatti)

    def hae_askel(self):
        '''Hakee seuraavan askeleen hyödyntäen seinänhakijaa.

        Seinänhakijalle syötetty hakusuunta-muuttuja on suhteellinen koordinaattisiirtymä
        nykyisestä paikasta edelliseen solmuun ja ns. siirtymäkompassia lähdetään
        tarkistamaan tästä vastapäivään'''

        hakusuunta = (self.polku[-2][0]-self.polku[-1][0], self.polku[-2][1]-self.polku[-1][1])
        while True:
            self.kierrokset += 1
            hakusuunta = self.seinanhakija[hakusuunta]
            hakukoord = (self.polku[-1][0]+hakusuunta[0], self.polku[-1][1]+hakusuunta[1])
            if hakukoord not in self.laby.labyrintti[self.polku[-1]]:
                self.seinakosketukset.append(hakukoord)
                continue
            break
        self.polku.append(hakukoord)
        self.seinakosketukset.append((-1,-1))
        if self.polku[-1] == self.laby.labyrintti['loppu']:
            self.seinakosketukset.append((-1,-1))
            return False
        return True
