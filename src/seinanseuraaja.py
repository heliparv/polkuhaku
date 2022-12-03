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
        paikka: tallentaa missä ruudussa ollaan nyt
        pituus: tallentaa löydetyn reitin pituuden'''

        self.polku = {}
        self.laby = labyrintti
        self.seinanhakija = {'-1,-1':'0,-1','0,-1':'1,-1','1,-1':'1,0',
        '1,0':'1,1','1,1':'0,1','0,1':'-1,1','-1,1':'-1,0','-1,0':'-1,-1'}
        self.paikka = ''
        self.pituus = 0
        self.laby.luo_ratkaisugrafiikka()
        self.aika = 0
        self.hae_polku()

    def hae_polku(self):
        alku = time.time()
        self.ensiaskel()
        jatketaan = True
        while jatketaan:
            jatketaan = self.hae_askel()
        loppu = time.time()
        self.aika = loppu-alku
        print('Seinänseuraaja-algoritmin löytämä polku:')
        self.laby.tulosta_ratkaisu()

    def ensiaskel(self):
        '''Tarkistaa millä reunalla labyrintin alku on ja ottaa ensimmäisen askeleen
        Labyrintissa ei olisi reittiä jos alun reunanaapuri ei olisi vapaa, joten
        tarkistetaan vain voidaanko lähteä vinoon oikealle kääntyen vai mennäänkö
        suoraan eteen.
        Vaiheet: 1.Määritä millä seinällä alku on ja sen perusteella vino oikea
        2. Katso voiko vinoon oikealle mennä
        3. Mene vinoon oikealle tai suoraan eteen, tulosta ratkaisu'''

        alku_str = self.laby.labyrintti['alku']
        alku = alku_str.split(',')
        if int(alku[1]) == 0:
            vino_oikea = '1,1'
        elif int(alku[1]) == len(self.laby.ratkaisu[0])-1:
            vino_oikea = '-1,-1'
        elif int(alku[0]) == 0:
            vino_oikea = '1,-1'
        else:
            vino_oikea = '-1,1'

        vino_koordinaatti = self.suhteellinen_koordinaatiksi(vino_oikea, alku_str)
        if vino_koordinaatti in self.laby.labyrintti[alku_str]:
            self.polku[vino_koordinaatti] = alku_str
            self.laby.merkitse_kayty_paikka(vino_koordinaatti)
            self.paikka = vino_koordinaatti
        else:
            koordinaatti = self.suhteellinen_koordinaatiksi(self.seinanhakija[vino_oikea], alku_str)
            self.polku[koordinaatti] = alku_str
            self.laby.merkitse_kayty_paikka(koordinaatti)
            self.paikka = koordinaatti
        self.pituus += 1

    def hae_askel(self):
        '''Hakee seuraavan askeleen hyödyntäen seinänhakijaa.'''
        #edellinen = self.polku[self.paikka]
        hakukoord = self.koordinaatti_suhteelliseksi(self.paikka, self.polku[self.paikka])
        while True:
            hakukoord = self.seinanhakija[hakukoord]
            oikea_koord = self.suhteellinen_koordinaatiksi(hakukoord, self.paikka)
            if oikea_koord not in self.laby.labyrintti[self.paikka]:
                continue
            break
        self.polku[oikea_koord] = self.paikka
        self.paikka = oikea_koord
        self.pituus += 1
        if self.paikka == self.laby.labyrintti['loppu']:
            return False
        self.laby.merkitse_kayty_paikka(oikea_koord)
        return True

    def suhteellinen_koordinaatiksi(self, suhteellinen: str, nykyinen: str):
        '''Ottaa nykyiseen koordinaattiin verratun suhteellisen merkkijonoesityksen
        ja muuntaa sen koordinaatiksi labyrintissa nykyisen koordinaatin suhteen'''
        muutos = suhteellinen.split(',')
        nykykoordinaatti = nykyinen.split(',')
        return f'{int(nykykoordinaatti[0])+int(muutos[0])},{int(nykykoordinaatti[1])+int(muutos[1])}'

    def koordinaatti_suhteelliseksi(self, nykyinen: str, verrokki: str):
        '''Ottaa kaksi merkkijonomuotoista koordinaattia ja tekee niistä suhteellisen
        koordinaattiestityksen sille, miten nykyisestä pääsee verrokkiin'''
        nyky = nykyinen.split(',')
        vert = verrokki.split(',')
        return f'{int(vert[0])-int(nyky[0])},{int(vert[1])-int(nyky[1])}'

    def aikavaativuus(self):
        return f"Seinänseuraaja-algoritmin suorittamiseen kului {self.aika}"

    def polun_pituus(self):
        return f"Seinänseuraaja-algoritmilla löydetun polun pituus on {self.pituus}"
