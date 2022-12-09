from copy import deepcopy

class Labyrintti:
    '''Luokka labyrintille. Tällä hetkellä palauttaa vain pyydettäessä yhden
    labyrintin, jotta saadaan ensin varsinaiset algoritmit tehtyä.
    Myöhemmin koodataan vaihtoehtoja.

    Labyrintin muodon sääntöjä: Reunat ovat aina seinää, lukuun ottamatta alku-
    ja loppupisteitä, jotka ovat aina labyrintin reunoilla. Alku- tai loppupisteet
    eivät voi olla kulmissa. Labyrintissa on vain seinää tai lattiaa sisällä.
    Labyrintissa voi liikkua pystyyn ja vaakaan jos vierekkäiset palat ovat lattiaa.
    Vinottain voi liikkua jos vinoruutu on lattiaa ja vähintään toinen lähtöruudun
    ja vinoruudun vieressä olevista ruuduista on lattiaa.
    '''
    def __init__(self, grafiikka = 0):
        '''alustusfunktio. Mikäli grafiikkaa ei ole annettu, käyttää
        esimerkkigrafiikkaa. Jos grafiikka on annettu, asettaa sen labyrintin grafiikaksi
        Käyttää lue_labyrintti -funktiota luodakseen grafiikasta sanakirjaesityksen, joka
        kuvaa joka ruudulle minne siitä on pääsy. Muuttujaan ratkaisu sijoitetaan myöhemmin
        ratkaisun graafinen esitys.'''
        if grafiikka == 0:
            self.grafiikka = ['#A##########',
                              '# #  #     #',
                              '# #     #  #',
                              '#     ##   #',
                              '###    ##  #',
                              '#    ###  ##',
                              '#      #   #',
                              '##########B#',]
        else:
            self.grafiikka = grafiikka
        self.labyrintti = {}
        self.lue_labyrintti()
        self.ratkaisu = []

    def lue_labyrintti(self):
        '''lue_labyrintti: Tekee labyrintin grafiikasta sanakirjaesityksen käyttämällä
        lue_pystyreunat-, lue_vaakareunat- ja lue_sisus -funktioita.'''
        self.luo_solmut()
        self.lue_pystyreunat()
        self.lue_vaakareunat()
        self.lue_sisus()
        self.poista_seinasolmut()

    def luo_solmut(self):
        '''luo_solmut: alustaa kaikki labyrintin sisällä olevat solmut, jottei niitä tarvitse
        luoda myöhemmin ja tarkistaa luennan yhteydessä ovatko jo olemassa.'''
        for i in range(1, len(self.grafiikka)-1):
            for j in range(1, len(self.grafiikka[0])-1):
                self.labyrintti[(i,j)] = []

    def lue_pystyreunat(self):
        ''''lue_pystyreunat: funktio lukee annetun grafiikan pystyreunat etsien alku- tai
        loppupistettä, jotka merkitsee labyrintin solmuesitykseen. Ei tarkastele
        nurkkapaloja.
        
        Funktio on täysin turha jos alku ja loppu ovat aina samoissa nurkissa,
        kuten testilabyrintissa'''

        for reuna in [0, len(self.grafiikka[0])-1]:
            for i in range(1, len(self.grafiikka)-1):
                if self.grafiikka[i][reuna] in ['A', 'B']:
                    self.labyrintti[(i, reuna)] = []
                    if reuna == 0:
                        ero = 1
                    else:
                        ero = -1
                    if self.grafiikka[i][reuna+ero] == ' ':
                        self.labyrintti[(i,reuna)].append((i, reuna+ero))
                        self.labyrintti[(i,reuna+ero)].append((i,reuna))
                        if self.grafiikka[i-1][reuna+ero] == ' ':
                            self.labyrintti[(i, reuna)].append((i-1,reuna+ero))
                            self.labyrintti[(i-1,reuna+ero)].append((i,reuna))
                        if self.grafiikka[i+1][reuna+ero] == ' ':
                            self.labyrintti[(i,reuna)].append((i+1,reuna+ero))
                            self.labyrintti[(i+1,reuna+ero)].append((i,reuna))
                        if self.grafiikka[i][reuna] == 'A':
                            self.labyrintti['alku'] = (i,reuna)
                        else:
                            self.labyrintti['loppu'] = (i,reuna)

    def lue_vaakareunat(self):
        '''lue_vaakareunat: funktio lukee annetun grafiikan vaakareunat etsien alku- tai
        loppupistettä, jonka merkitsee labyrintin solmuesitykseen. Ei tarkastele
        nurkkapaloja.
        
        Funktio on täysin turha jos alku ja loppu ovat aina samoissa nurkissa,
        kuten testilabyrintissa'''

        for reuna in [0, len(self.grafiikka)-1]:
            for j in range(1, len(self.grafiikka[0])-1):
                if self.grafiikka[reuna][j] in ['A', 'B']:
                    self.labyrintti[(reuna,j)] = []
                    if reuna == 0:
                        ero = 1
                    else:
                        ero = -1
                    if self.grafiikka[reuna+ero][j] == ' ':
                        self.labyrintti[(reuna,j)].append((reuna+ero,j))
                        self.labyrintti[(reuna+ero,j)].append((reuna,j))
                    if self.grafiikka[reuna+ero][j-1] == ' ':
                        self.labyrintti[(reuna,j)].append((reuna+ero,j-1))
                        self.labyrintti[(reuna+ero,j-1)].append((reuna,j))
                    if self.grafiikka[reuna+ero][j-1] == ' ':
                        self.labyrintti[(reuna,j)].append((reuna+ero,j-1))
                        self.labyrintti[(reuna+ero,j-1)].append((reuna,j))
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
                if self.grafiikka[i+1][j] == ' ':
                    self.labyrintti[(i,j)].append((i+1,j))
                    self.labyrintti[(i+1,j)].append((i,j))
                if self.grafiikka[i][j+1] == ' ':
                    self.labyrintti[(i,j)].append((i,j+1))
                    self.labyrintti[(i,j+1)].append((i,j))
    
    def poista_seinasolmut(self):
        for i in range(1, len(self.grafiikka)-1):
            for j in range(1, len(self.grafiikka[0])-1):
                if self.labyrintti[(i,j)] == []:
                    del self.labyrintti[(i,j)]

    def luo_ratkaisugrafiikka(self):
        '''Alustaa grafiikan ratkaisuesitystä varten'''
        self.ratkaisu = deepcopy(self.grafiikka)

    def merkitse_kayty_paikka(self, paikka):
        '''Merkitsee annetun lattiapaikan käydyksi ratkaisuesityksessä'''
        mjono = self.ratkaisu[paikka[0]]
        self.ratkaisu[paikka[0]] = mjono[:paikka[1]]+'.'+mjono[paikka[1]+1:]

    def tulosta_grafiikka(self):
        '''Tulostaa grafiikan riveittäin, jotta se näyttää labyrintilta'''
        for i in range(len(self.grafiikka)):
            print(self.grafiikka[i])

    def tulosta_ratkaisu(self):
        '''Tulostaa ratkaisugrafiikan riveittäin, jotta se näyttää labyrintilta'''
        for i in range(len(self.ratkaisu)):
            print(self.ratkaisu[i])
        print('')

    def leveys(self):
        return len(self.grafiikka[0])

    def korkeus(self):
        return len(self.grafiikka)
