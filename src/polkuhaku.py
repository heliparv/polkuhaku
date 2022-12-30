import pygame
from labyrintti import Labyrintti
from leveyshaku import Leveyshaku
from seinanseuraaja import Seinanseuraaja
from testilabyrintti import Testilabyrintti

class Polkuhaku:
    '''Tämä luokka koodaa polkuhakuohjelman käyttöliittymän'''

    def __init__(self):
        '''Luokan luonnissa käynnistetään pygame ja määritellään sille näytön koko,
        kello, sekä kaksi fonttia. Alustetaan myös muut muuttujat ja alustuksen jälkeen
        siirrytään luokan metodiin, joka näyttää aloitusvalikon

        Luokan muut muuttuja:
        labyrinttityyppi: Testilabyrintti-luokassa käytetty tyyppi, harva, tiheä tai siksak

        sivun_pituus: Testilabyrintti koostuu toistuvista palasista, sivun_pituus kertoo
        kuinka monta kertaa palanen toistuu sekä vaaka- että pystysuunnassa

        labyrintti: Käytetään säilyttämään labyrintti-olio, jolle polkuhaku suoritetaan

        lattia: Graafista esitystä varten luotu lista, joka sisältää labyrintin esitystä
        varten tarvitut lattian kappaleet

        dimensio: Labyrinttien koko vaihtelee, jolloin on hyvä että lattiaruudut esitetään eri
        kokoisina. Dimensio tllentaa lattiaruutujen leveyden pikseleinä

        leveyshaku: Tämä säilyttää leveyshakualgoritmille luotua oliota, joka tallentaa
        leveyshakualgoritmista saadut tulokset

        seinanseuraaja: Tallentaa Seinanseuraaja-olion, jossa on tallennettuna algoritmin
        saamat tulokset
        '''
        pygame.init()
        pygame.display.set_caption('Polkuhaku')
        self.naytto = pygame.display.set_mode((1400,1000))
        self.kello = pygame.time.Clock()
        self.isofontti = pygame.font.SysFont('Arial', 60)
        self.pienifontti = pygame.font.SysFont('Arial', 40)
        self.virheviesti = ''
        self.labyrinttityyppi = ''
        self.sivun_pituus = ''
        self.labyrintti = None
        self.lattia = []
        self.dimensio = 0
        self.leveyshaku = None
        self.seinanseuraaja = None
        self.aloitusvalikko()

    def aloitusvalikko(self):
        '''Funktio näyttää käyttäjälle labyrintin luonnissa käytettävät tyypit ja
        pyytää käyttäjää valitsemaan näistä yhden'''

        harva = pygame.image.load('src/harva.png')
        tihea = pygame.image.load('src/tihea.png')
        siksak = pygame.image.load('src/siksak.png')
        while True:
            self.hae_aloitusvalikon_tapahtumat()

            self.naytto.fill((40,40,70))
            rivi1 = self.isofontti.render('Anna labyrintin tyyppi', True, (240, 240, 250))
            self.naytto.blit(rivi1, (750-rivi1.get_width()/2, 160))
            rivi2 = self.pienifontti.render(
                'Labyrintti koostuu toistuvista samanlaisista palasista',
                True, (240, 240, 250))
            self.naytto.blit(rivi2, (750-rivi2.get_width()/2, 250))
            harvateksti = self.isofontti.render('H = harva', True, (240, 240, 250))
            self.naytto.blit(harvateksti, (100+(400-harvateksti.get_width())/2, 400))
            tiheateksti = self.isofontti.render('T = tiheä', True, (240, 240, 250))
            self.naytto.blit(tiheateksti, (500+(400-tiheateksti.get_width())/2, 400))
            siksakteksti = self.isofontti.render('S = siksak', True, (240, 240, 250))
            self.naytto.blit(siksakteksti, (1000+(400-siksakteksti.get_width())/2, 400))
            self.naytto.blit(harva, (100, 500))
            self.naytto.blit(tihea, (550, 500))
            self.naytto.blit(siksak, (1000, 500))
            pygame.display.flip()
            self.kello.tick(60)

    def hae_aloitusvalikon_tapahtumat(self):
        '''Funktio huolehtii aloitusvalikon toiminnallisuudesta,
        tarkistaa painaako käyttäjä jotakin valikon toimintonäppäintä'''

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_h:
                    self.labyrinttityyppi = 'harva'
                    self.labyrintin_koko()
                if tapahtuma.key == pygame.K_t:
                    self.labyrinttityyppi = 'tiheä'
                    self.labyrintin_koko()
                if tapahtuma.key == pygame.K_s:
                    self.labyrinttityyppi = 'siksak'
                    self.labyrintin_koko()

    def labyrintin_koko(self):
        '''Funktio näyttää käyttäjälle ruudun jolla on ohjeita labyrintin koon valintaan,
        esittää virheviestin jos käyttäjä on valitsemassa labyrintille sopimattoman koon'''

        while True:
            virhe = self.hae_labyrintin_koon_tapahtumat()

            self.naytto.fill((40,40,70))
            rivi1 = self.isofontti.render('Anna labyrintin reunan pituus', True, (240, 240, 250))
            self.naytto.blit(rivi1, (750-rivi1.get_width()/2, 160))
            rivi2 = self.pienifontti.render(
                'Pituus tarkoittaa valitun labyrinttipalasen toistokertoja',
                True, (240, 240, 250))
            self.naytto.blit(rivi2, (750-rivi2.get_width()/2, 250))
            rivi3 = self.pienifontti.render('Suurin sallittu koko on 100x100', True, (240, 240, 250))
            self.naytto.blit(rivi3, (750-rivi3.get_width()/2, 300))
            rivi4 = self.isofontti.render(f'Valittu koko: {self.sivun_pituus}', True, (240, 240, 250))
            self.naytto.blit(rivi4, (400, 500))
            if virhe:
                self.naytto.blit(self.virheviesti, (750-self.virheviesti.get_width()/2, 600))
            pygame.display.flip()
            self.kello.tick(60)

    def hae_labyrintin_koon_tapahtumat(self):
        '''Funktio huolehtii labyrintin koon määrittämiseen varatun näkymän toiminnallisuudesta.
        Tarkistaa painaako käyttäjä näppäintä ja korjaa labyrintin sivun pituuden oikeaksi.
        Palauttaa tiedon siitä, tarvitseeko esittää virheviesti'''

        virhe = False
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()

            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key in pygame.K_1:
                    self.sivun_pituus = self.sivun_pituus+'1'
                if tapahtuma.key == pygame.K_2:
                    self.sivun_pituus = self.sivun_pituus+'2'
                if tapahtuma.key == pygame.K_3:
                    self.sivun_pituus = self.sivun_pituus+'3'
                if tapahtuma.key == pygame.K_4:
                    self.sivun_pituus = self.sivun_pituus+'4'
                if tapahtuma.key == pygame.K_5:
                    self.sivun_pituus = self.sivun_pituus+'5'
                if tapahtuma.key == pygame.K_6:
                    self.sivun_pituus = self.sivun_pituus+'6'
                if tapahtuma.key == pygame.K_7:
                    self.sivun_pituus = self.sivun_pituus+'7'
                if tapahtuma.key == pygame.K_8:
                    self.sivun_pituus = self.sivun_pituus+'8'
                if tapahtuma.key == pygame.K_9:
                    self.sivun_pituus = self.sivun_pituus+'9'
                if tapahtuma.key == pygame.K_0:
                    self.sivun_pituus = self.sivun_pituus+'0'
                if tapahtuma.key == pygame.K_BACKSPACE:
                    self.sivun_pituus = self.sivun_pituus[:-1]

                if tapahtuma.key == pygame.K_RETURN or tapahtuma.key == pygame.K_KP_ENTER:
                    if self.sivun_pituus == '' or int(self.sivun_pituus) == 0:
                        virhe = True
                        self.virheviesti = self.pienifontti.render(
                            'Anna nollaa suurempi sivun pituus',
                            True, (240, 240, 250))
                    elif int(self.sivun_pituus) > 100:
                        virhe = True
                        self.virheviesti = self.pienifontti.render(
                            'Sivun pituus voi olla korkeintaan 100',
                            True, (240, 240, 250))
                    else:
                        self.sivun_pituus = int(self.sivun_pituus)
                        self.suorita_haut()
        return virhe

    def suorita_haut(self):
        '''Kun käyttäjä on valinnut labyrintin tyypin ja koon, suoritetaan
        polkuhakualgoritmit valmiiksi, minkä järkeen siirrytään alustamaan
        labyrintin grafiikka.'''

        laby = Testilabyrintti(self.sivun_pituus, self.sivun_pituus,self.labyrinttityyppi)
        self.labyrintti = Labyrintti(laby.labyrintti)
        self.leveyshaku = Leveyshaku(self.labyrintti)
        self.leveyshaku.hae_polku()
        self.seinanseuraaja = Seinanseuraaja(self.labyrintti)
        self.seinanseuraaja.hae_polku()
        self.alusta_labyrinttigrafiikka()

    def alusta_labyrinttigrafiikka(self):
        '''Funktio valitsee minkä kokoisia labyrintin ruudut ovat, muokkaa ohjelman ikkunan
        koon labyrintille sopivaksi, merkitsee missä labyrintin lattiaruudut ovat käymällä
        läpi labyrintin ACII-grafiikan.

        Siirtyy lopuksi funktioon, jossa käyttäjä saa valita näytettävän algoritmin'''

        self.dimensio = int(900/((self.sivun_pituus*10)))
        self.naytto = pygame.display.set_mode(
            ((2+(self.sivun_pituus*15))*self.dimensio,
            (2+(self.sivun_pituus*10))*self.dimensio))
        vaaka = 0
        pysty = 0
        for rivi in self.labyrintti.grafiikka:
            for ruutu in rivi:
                if ruutu != '#':
                    self.lattia.append(pygame.Rect(vaaka,pysty,self.dimensio,self.dimensio))
                vaaka += self.dimensio
            pysty += self.dimensio
            vaaka = 0
        self.algoritmin_valinta()

    def algoritmin_valinta(self):
        '''Näyttää valikon, jossa käyttäjä voi valita minkä algoritmin suoritusta
        haluaa tarkastella'''
        while True:
            self.hae_algoritmin_valinnan_tapahtumat()
            self.naytto.fill((40,40,70))
            rivi1 = self.isofontti.render('Valitse algoritmi', True, (240, 240, 250))
            self.naytto.blit(rivi1, (750-rivi1.get_width()/2, 160))
            rivi2 = self.isofontti.render('L = Leveyshaku    S = Seinänseuraaja', True, (240, 240, 250))
            self.naytto.blit(rivi2, (750-rivi2.get_width()/2, 300))
            rivi3 = self.isofontti.render('P = Palaa takaisin', True, (240, 240, 250))
            self.naytto.blit(rivi3, (750-rivi3.get_width()/2, 390))
            pygame.display.flip()
            self.kello.tick(60)

    def hae_algoritmin_valinnan_tapahtumat(self):
        '''Hakee tapahtumat algoritmin valinnassa'''
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_l:
                    self.nayta_leveyshaku()
                if tapahtuma.key == pygame.K_s:
                    self.nayta_seinanseuraaja()
                if tapahtuma.key == pygame.K_p:
                    self.lattia = []
                    self.sivun_pituus = ''
                    self.aloitusvalikko()

    def nayta_leveyshaku(self):
        '''Näyttää ruutu kerrallaan missä lattiaruudussa leveyshaku vierailee
        ja kun tämä on valmis, siirtyy näyttämään polun labyrintin läpi

        Muuttujat i ja j kuvaavat indeksiä, josta seuraava tarkastettu lattiaruutu tai
        seuraava polun ruutu haetaan piirrettävään grafiikkaan algoritmin tietorakenteesta

        kayty: sisältää listana tiedon ruuduista, joissa leveyshaku on käynyt
        polku: sisältää listana tiedon ruuduista, jotka kuuluvat löydettyyn polkuun'''

        i = 0
        j = -1
        kayty = []
        polku = []
        while True:
            self.hae_algoritmin_nayton_tapahtumat()

            self.naytto.fill((40,40,70))
            for ruutu in self.lattia:
                pygame.draw.rect(self.naytto, (240, 240, 250), ruutu)

            if i < len(self.leveyshaku.esitys):
                pysty, vaaka = self.leveyshaku.esitys[i]
                kayty.append(pygame.Rect(vaaka*self.dimensio, pysty*self.dimensio,self.dimensio,self.dimensio))
            if i == len(self.leveyshaku.esitys):
                j = len(self.leveyshaku.oikea_polku)-1
            for ruutu in kayty:
                pygame.draw.rect(self.naytto, (130,160,250), ruutu)

            if j >= 0:
                pysty, vaaka = self.leveyshaku.oikea_polku[j]
                polku.append((vaaka*self.dimensio+int(self.dimensio/2), pysty*self.dimensio+int(self.dimensio/2)))
            for ruutu in polku:
                pygame.draw.circle(self.naytto, (70, 250, 230), ruutu, self.dimensio/2)

            pygame.display.flip()
            i += 1
            j -= 1
            self.kello.tick(60*self.sivun_pituus)

    def nayta_seinanseuraaja(self):
        '''Näyttää ruutu ruudulta missä seinänseuraaja-algoritmi etenee,
        samalla näyttää punaisin palloin minkä ruudun osalta algoritmi tarkistaa
        pääseekö sinne liikkumaan. Kun tämä on tehty, näytetään algoritmin löytämä
        polku vihrein palloin. Koska algoritmi tarkistaa samoja ruutuja uudestaan kulkureitiksi
        ja saattaa kulkea saman lattiaruudun halki uudestaan, kuvatan tätä sillä, että
        mitä tummempi pallo on, sitä useammin se on tarkastettu tai sen läpi on kuljettu'''

        kayty = []
        tarkastettu = {}
        polku = {}
        while True:
            self.hae_algoritmin_nayton_tapahtumat()

            self.naytto.fill((40,40,70))
            for ruutu in self.lattia:
                pygame.draw.rect(self.naytto, (240, 240, 250), ruutu)

            if len(self.seinanseuraaja.seinakosketukset) > 0:
                pysty, vaaka = self.seinanseuraaja.seinakosketukset.pop(0)
                if pysty == -1:
                    pysty, vaaka = self.seinanseuraaja.polku.pop(0)
                    kayty.append(pygame.Rect(vaaka*self.dimensio,pysty*self.dimensio,self.dimensio,self.dimensio))
                    koordinaatti = (vaaka*self.dimensio+int(self.dimensio/2), pysty*self.dimensio+int(self.dimensio/2))
                    if koordinaatti in polku:
                        polku[koordinaatti] += 1
                    else:
                        polku[koordinaatti] = 0
                else:
                    koordinaatti = (vaaka*self.dimensio+int(self.dimensio/2), pysty*self.dimensio+int(self.dimensio/2))
                    if koordinaatti in tarkastettu:
                        tarkastettu[koordinaatti] += 1
                    else:
                        tarkastettu[koordinaatti] = 0

            for ruutu in kayty:
                pygame.draw.rect(self.naytto, (130,160,250), ruutu)
            for ruutu in tarkastettu:
                punainen = max(255-30*tarkastettu[ruutu],0)
                vihrea = max(150-30*tarkastettu[ruutu],0)
                sininen = max(130-30*tarkastettu[ruutu],0)
                pygame.draw.circle(self.naytto, (punainen, vihrea, sininen), ruutu, self.dimensio/2)
            if len(self.seinanseuraaja.seinakosketukset) == 0:
                for ruutu in polku:
                    punainen = max(70-50*polku[ruutu],0)
                    vihrea = max(250-30*polku[ruutu],0)
                    sininen = max(230-40*polku[ruutu],0)
                    pygame.draw.circle(self.naytto, (punainen, vihrea, sininen), ruutu, self.dimensio/2)

            pygame.display.flip()
            self.kello.tick(60*self.sivun_pituus)

    def hae_algoritmin_nayton_tapahtumat(self):
        '''Funktio hakee käyttäjän syötteet kun ohjelma esittää jonkin algoritmin toimintaa'''
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_p:
                    self.algoritmin_valinta()
