from labyrintti import Labyrintti
from leveyshaku import Leveyshaku
from seinanseuraaja import Seinanseuraaja
from testilabyrintti import Testilabyrintti
import pygame

class Polkuhaku:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Polkuhaku')
        self.naytto = pygame.display.set_mode((1500,1000))
        self.kello = pygame.time.Clock()
        self.isofontti = pygame.font.SysFont('Arial', 60)
        self.pienifontti = pygame.font.SysFont('Arial', 40)
        self.labyrinttityyppi = ''
        self.laby_sivunpituus = 0
        self.testilabyrintti = ''
        self.labyrintti = ''
        self.leveyshaku = ''
        self.seinanseuraaja = ''
        self.lattia = []
        self.dimensio = 0
        self.labyrintin_tyyppi()

    def labyrintin_tyyppi(self):
        harva = pygame.image.load('src/harva.png')
        tihea = pygame.image.load('src/tihea.png')
        siksak = pygame.image.load('src/siksak.png')
        while True:
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

            self.naytto.fill((40,40,70))
            rivi1 = self.isofontti.render('Anna labyrintin tyyppi', True, (240, 240, 250))
            self.naytto.blit(rivi1, (750-rivi1.get_width()/2, 160))
            rivi2 = self.pienifontti.render('Labyrintti koostuu toistuvista samanlaisista palasista', True, (240, 240, 250))
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

    def labyrintin_koko(self):
        koko = ''
        virhe = False
        while True:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    exit()
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_1:
                        koko = koko+'1'
                    if tapahtuma.key == pygame.K_2:
                        koko = koko+'2'
                    if tapahtuma.key == pygame.K_3:
                        koko = koko+'3'
                    if tapahtuma.key == pygame.K_4:
                        koko = koko+'4'
                    if tapahtuma.key == pygame.K_5:
                        koko = koko+'5'
                    if tapahtuma.key == pygame.K_6:
                        koko = koko+'6'
                    if tapahtuma.key == pygame.K_7:
                        koko = koko+'7'
                    if tapahtuma.key == pygame.K_8:
                        koko = koko+'8'
                    if tapahtuma.key == pygame.K_9:
                        koko = koko+'9'
                    if tapahtuma.key == pygame.K_0:
                        koko = koko+'0'
                    if tapahtuma.key == pygame.K_BACKSPACE:
                        koko = koko[:-1]
                    if tapahtuma.key == pygame.K_RETURN or tapahtuma.key == pygame.K_KP_ENTER:
                        if koko == '' or int(koko) == 0:
                            virhe = True
                            virheviesti = self.pienifontti.render('Anna nollaa suurempi sivun pituus', True, (240, 240, 250))
                        elif int(koko) > 100:
                            virhe = True
                            virheviesti = self.pienifontti.render('Sivun pituus voi olla korkeintaan 100', True, (240, 240, 250))
                        else:
                            self.laby_sivunpituus = int(koko)
                            self.suorita_haut()

            self.naytto.fill((40,40,70))
            rivi1 = self.isofontti.render('Anna labyrintin reunan pituus', True, (240, 240, 250))
            self.naytto.blit(rivi1, (750-rivi1.get_width()/2, 160))
            rivi2 = self.pienifontti.render('Pituus tarkoittaa valitun labyrinttipalasen toistokertoja', True, (240, 240, 250))
            self.naytto.blit(rivi2, (750-rivi2.get_width()/2, 250))
            rivi3 = self.pienifontti.render('Suurin sallittu koko on 100x100', True, (240, 240, 250))
            self.naytto.blit(rivi3, (750-rivi3.get_width()/2, 300))
            rivi4 = self.isofontti.render(f'Valittu koko: {koko}', True, (240, 240, 250))
            self.naytto.blit(rivi4, (400, 500))
            if virhe:
                self.naytto.blit(virheviesti, (750-virheviesti.get_width()/2, 600))
            pygame.display.flip()
            self.kello.tick(60)

    def suorita_haut(self):
        self.testilabyrintti = Testilabyrintti(self.laby_sivunpituus, self.laby_sivunpituus,self.labyrinttityyppi)
        self.labyrintti = Labyrintti(self.testilabyrintti.labyrintti)
        self.leveyshaku = Leveyshaku(self.labyrintti)
        self.leveyshaku.hae_polku()
        self.seinanseuraaja = Seinanseuraaja(self.labyrintti)
        self.seinanseuraaja.hae_polku()
        self.alusta_labyrintti()

    def alusta_labyrintti(self):
        self.dimensio = int(1000/((self.laby_sivunpituus*10)+2))
        x = 0
        y = 0
        for rivi in self.testilabyrintti.labyrintti:
            for ruutu in rivi:
                if ruutu != '#':
                    self.lattia.append(pygame.Rect(x,y,self.dimensio,self.dimensio))
                x += self.dimensio
            y += self.dimensio
            x = 0
        self.valikko()

    def valikko(self):
        while True:
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
                        self.labyrintin_tyyppi()
            self.naytto.fill((40,40,70))
            rivi1 = self.isofontti.render('Valitse algoritmi', True, (240, 240, 250))
            self.naytto.blit(rivi1, (750-rivi1.get_width()/2, 160))
            rivi2 = self.isofontti.render('L = Leveyshaku    S = Seinänseuraaja', True, (240, 240, 250))
            self.naytto.blit(rivi2, (750-rivi2.get_width()/2, 300))
            rivi3 = self.isofontti.render('P = Palaa takaisin', True, (240, 240, 250))
            self.naytto.blit(rivi3, (750-rivi3.get_width()/2, 390))
            pygame.display.flip()
            self.kello.tick(60)

    def nayta_leveyshaku(self):
        i = 0
        j = -1
        kayty = []
        polku = []
        while True:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    exit()
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_p:
                        self.valikko()

            self.naytto.fill((40,40,70))
            for ruutu in self.lattia:
                pygame.draw.rect(self.naytto, (240, 240, 250), ruutu)

            if i < len(self.leveyshaku.esitys):
                y,x = self.leveyshaku.esitys[i]
                kayty.append(pygame.Rect(x*self.dimensio,y*self.dimensio,self.dimensio,self.dimensio))
            if i == len(self.leveyshaku.esitys):
                j = len(self.leveyshaku.oikea_polku)-1
            for ruutu in kayty:
                pygame.draw.rect(self.naytto, (130,160,250), ruutu)

            if j >= 0:
                y,x = self.leveyshaku.oikea_polku[j]
                polku.append((x*self.dimensio+int(self.dimensio/2), y*self.dimensio+int(self.dimensio/2)))
            for ruutu in polku:
                pygame.draw.circle(self.naytto, (70, 250, 230), ruutu, self.dimensio/2)

            pygame.display.flip()
            i += 1
            j -= 1
            self.kello.tick(60*self.laby_sivunpituus)


    def nayta_seinanseuraaja(self):
        kayty = []
        tarkastettu = {}
        polku = {}
        while True:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    exit()
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_p:
                        self.valikko()
        
            self.naytto.fill((40,40,70))
            for ruutu in self.lattia:
                pygame.draw.rect(self.naytto, (240, 240, 250), ruutu)

            if len(self.seinanseuraaja.seinakosketukset) > 0:
                y, x = self.seinanseuraaja.seinakosketukset.pop(0)
                if y == -1:
                    y, x = self.seinanseuraaja.polkuesitys.pop(0)
                    kayty.append(pygame.Rect(x*self.dimensio,y*self.dimensio,self.dimensio,self.dimensio))
                    koordinaatti = (x*self.dimensio+int(self.dimensio/2), y*self.dimensio+int(self.dimensio/2))
                    if koordinaatti in polku:
                        polku[koordinaatti] += 1
                    else:
                        polku[koordinaatti] = 0
                else:
                    koordinaatti = (x*self.dimensio+int(self.dimensio/2), y*self.dimensio+int(self.dimensio/2))
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
            self.kello.tick(60*self.laby_sivunpituus)
