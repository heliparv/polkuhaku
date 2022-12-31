
class Labyrintti:
    '''Luokka joka käsittelee annetun tekstimuotoisen labyrintin ja muodostaa
    siitä verkkomuotoisen esityksen. Tallentaa myös alkuperäisen ASCII-grafiikan.

    Luokan ymmärtämät labyrintit
    - Reunat ovat seiniä
    - Labyrintin alku- ja loppusolmu ('A' ja 'B') ovat seinillä, eivät kulmissa
    - Labyrintin sisus on seinää '#' tai lattiaa ' '
    - Labyrintissa liikutaan pystyyn, vaakaan ja vinottain, vinottainen liike
      lasketaan saman pituisena kuin muut siirtymät
    - Vinottain voi liikkua jos vinoruutu on lattiaa ja vähintään toinen lähtöruudun
      ja vinoruudun vieressä olevista ruuduista on lattiaa

    Luokan muuttujat:
    grafiikka: tallentaa ASCII-grafiikan

    labyrintti: tallentaa labyrintin verkkoesityksen sanakirjana, jossa avain on
    solmun koordinaatti ja arvona lista koordinaatteja solmuille joihin on yhteys

    kaaret: Tallentaa labyrintista löytyvien kaarien määrän, tätä käytetään jos halutaan
    verrata algoritmin tekemiä käsittelykierroksia annetun syötteen kokoon
    '''

    def __init__(self, grafiikka = ''):
        '''Alustetaan luokan käyttämät muuttujat. Mikäli grafiikkaa ei ole annettu, käyttää
        esimerkkigrafiikkaa. Jos grafiikka on annettu, asettaa sen labyrintin grafiikaksi
        Käyttää lue_labyrintti -funktiota luodakseen grafiikasta sanakirjaesityksen ja
        laske_kaaret funktiota käytetään laskemaan kaaret'''
        if grafiikka == '':
            self.grafiikka = ['#A##########',
                              '# #  #     #',
                              '# #     #  #',
                              '#   ####   #',
                              '###    ##  #',
                              '#    ###  ##',
                              '#      #   #',
                              '##########B#',]
        else:
            self.grafiikka = grafiikka
        self.labyrintti = {}
        self.kaaret = 0
        self.lue_labyrintti()
        self.laske_kaaret()

    def lue_labyrintti(self):
        '''lue_labyrintti: Tekee labyrintin grafiikasta sanakirjaesityksen käyttämällä
        lue_pystyreunat-, lue_vaakareunat-, lue_sisus ja poista_seinasolmut -funktioita.'''
        self.luo_solmut()
        self.lue_pystyreunat()
        self.lue_vaakareunat()
        self.lue_sisus()
        self.poista_seinasolmut()

    def luo_solmut(self):
        '''luo_solmut: alustaa kaikki labyrintin sisällä olevat solmut, jottei luennan
        yhteydessä tarvitse tarkistaa onko solmu olemassa vai ei.'''
        for i in range(1, len(self.grafiikka)-1):
            for j in range(1, len(self.grafiikka[0])-1):
                self.labyrintti[(i,j)] = []

    def lue_pystyreunat(self):
        ''''Syöttää kasittele_pystyreuna funktiolle molemmat pystyreunat'''

        self.kasittele_pystyreuna(0, 1)
        self.kasittele_pystyreuna(len(self.grafiikka[0])-1, -1)

    def kasittele_pystyreuna(self, reuna, suunta):
        '''Funktio käsittelee annetun pystyreunan etsien alku- tai loppusolmua. Jos
        löytää alun tai lopun, se lisätään verkkoon ja sille lisätään siirtymä
        labyrinttiin sekä tarkistetaan voidaanko tehdä vinottainen siirtymä.
        Nurkkapaloja ei käsitellä

        Funktiolle annettu arvo 'reuna' kertoo kummasta reunasta on kyse

        Annettua arvo 'suunta' kertoo mihin suuntaan siirrytään kohti keskustaa'''

        for i in range(1, len(self.grafiikka)-1):
            if self.grafiikka[i][reuna] in ['A', 'B']:
                self.labyrintti[(i, reuna)] = []
                if self.grafiikka[i][reuna+suunta] == ' ':
                    self.labyrintti[(i,reuna)].append((i, reuna+suunta))
                    self.labyrintti[(i,reuna+suunta)].append((i,reuna))
                    if self.grafiikka[i-1][reuna+suunta] == ' ':
                        self.labyrintti[(i, reuna)].append((i-1,reuna+suunta))
                        self.labyrintti[(i-1,reuna+suunta)].append((i,reuna))
                    if self.grafiikka[i+1][reuna+suunta] == ' ':
                        self.labyrintti[(i,reuna)].append((i+1,reuna+suunta))
                        self.labyrintti[(i+1,reuna+suunta)].append((i,reuna))
                    if self.grafiikka[i][reuna] == 'A':
                        self.labyrintti['alku'] = (i,reuna)
                    else:
                        self.labyrintti['loppu'] = (i,reuna)

    def lue_vaakareunat(self):
        '''Syöttää kasittele_vaakareuna funktiolle molemmat vaakareunat'''

        self.kasittele_vaakareuna(0, 1)
        self.kasittele_vaakareuna(len(self.grafiikka)-1, -1)

    def kasittele_vaakareuna(self, reuna, suunta):
        '''Funktio käsittelee annetun vaakareunan etsien alku- tai loppusolmua. Jos
        löytää alun tai lopun, se lisätään verkkoon ja sille lisätään siirtymä
        labyrinttiin sekä tarkistetaan voidaanko tehdä vinottainen siirtymä.
        Nurkkapaloja ei käsitellä

        Funktiolle annettu arvo 'reuna' kertoo kummasta reunasta on kyse

        Annettua arvo 'suunta' kertoo mihin suuntaan siirrytään kohti keskustaa'''

        for j in range(1, len(self.grafiikka[0])-1):
            if self.grafiikka[reuna][j] in ['A', 'B']:
                self.labyrintti[(reuna,j)] = []
                if self.grafiikka[reuna+suunta][j] == ' ':
                    self.labyrintti[(reuna,j)].append((reuna+suunta,j))
                    self.labyrintti[(reuna+suunta,j)].append((reuna,j))
                if self.grafiikka[reuna+suunta][j-1] == ' ':
                    self.labyrintti[(reuna,j)].append((reuna+suunta,j-1))
                    self.labyrintti[(reuna+suunta,j-1)].append((reuna,j))
                if self.grafiikka[reuna+suunta][j-1] == ' ':
                    self.labyrintti[(reuna,j)].append((reuna+suunta,j-1))
                    self.labyrintti[(reuna+suunta,j-1)].append((reuna,j))
                if self.grafiikka[reuna][j] == 'A':
                    self.labyrintti['alku'] = (reuna,j)
                else:
                    self.labyrintti['loppu'] = (reuna,j)

    def lue_sisus(self):
        '''lue_sisus: Funktio käy läpi annetun grafiikan muut kuin reunapalat ja merkitsee
        labyrintin sanakirjaesitykseen mihin ruutuihin mistäkin ruudusta voi liikkua.'''
        for i in range(1,len(self.grafiikka)-1):
            for j in range(1,len(self.grafiikka[0])-1):
                if self.grafiikka[i][j] == '#':
                    continue
                if self.grafiikka[i+1][j+1] == ' ' and (self.grafiikka[i+1][j] == ' ' or self.grafiikka[i][j+1] == ' '):
                    self.labyrintti[(i,j)].append((i+1,j+1))
                    self.labyrintti[(i+1,j+1)].append((i,j))
                if self.grafiikka[i-1][j+1] == ' ' and (self.grafiikka[i-1][j] == ' ' or self.grafiikka[i][j+1] == ' '):
                    self.labyrintti[(i,j)].append((i-1,j+1))
                    self.labyrintti[(i-1,j+1)].append((i,j))
                if self.grafiikka[i+1][j] == ' ':
                    self.labyrintti[(i,j)].append((i+1,j))
                    self.labyrintti[(i+1,j)].append((i,j))
                if self.grafiikka[i][j+1] == ' ':
                    self.labyrintti[(i,j)].append((i,j+1))
                    self.labyrintti[(i,j+1)].append((i,j))

    def poista_seinasolmut(self):
        '''Käy läpi labyrintin verkkoesityksen ja poistaa solmut, joista ei
        ole yhteyksiä muihin solmuihin. Tätä käytetään poistamaan alussa
        turhaan luodut solmut, jotka esittävät seiniä. Näin saadaan tarkka
        mitta algoritmille syötetystä solmujen määrästä tarvittaessa.'''

        for i in range(1, len(self.grafiikka)-1):
            for j in range(1, len(self.grafiikka[0])-1):
                if self.labyrintti[(i,j)] == []:
                    del self.labyrintti[(i,j)]

    def laske_kaaret(self):
        '''Laskee labyrintissa esiintyvät kaaret, eli mahdolliset siirtymät
        lattiaruudusta toiseen. Jos ajateltaisiin kaaria tiukasti yksisuuntaisina
        painottamattomina kaarina niin summa tulisi jakaa kahdella. Algoritmin
        suorituksessa kaari kuitenkin syötetään kumpikin suunta erikseen, joten tätä
        mitataan myös suorituskykytestauksessa'''
        for kaaret in self.labyrintti:
            self.kaaret += len(kaaret)
