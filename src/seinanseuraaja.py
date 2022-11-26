from labyrintti import Labyrintti

class Seinanseuraaja:
    '''Luokka seinänseuraajaalgoritmin toteuttamiseen.
    Seuraa oikeanpuoleista seinää, eli kääntyy aina
    oikealle kun voi.'''

    def __init__(self, labyrintti: Labyrintti):
        '''alustaa reitin hakuun tarvittavat tietorakenteet ja siirtyy hakuun'''
        self.polku = {}
        self.laby = labyrintti
        self.seinanhakija = {'-1,-1':'0,-1','0,-1':'1,-1','1,-1':'1,0',
        '1,0':'1,1','1,1':'0,1','0,1':'-1,1','-1,1':'-1,0','-1,0':'-1,-1'}
        self.laby.luo_ratkaisugrafiikka()
        self.hae_polku()
    
    def hae_polku(self):
        self.etsi_alku()
        '''Algoritmi pyrkii aina seuraamaan vasenta seinää'''
    
    def etsi_alku(self):
        '''Tarkistaa millä reunalla labyrintin alku on ja ottaa ensimmäisen askeleen'''
        #Tarkista indeksit
        alku = self.laby.labyrintti['alku'].split(',')
        if int(alku[1]) == 0:
            tarkista = '1,-1'
        if int(alku[1]) == len(self.laby.ratkaisu[0])-1:
            tarkista = '1,-1'
        elif int(alku[1]) == 0:
            tarkista = '1,1'
        elif int(alku[1]) == len(self.laby.ratkaisu[0])-1:
            tarkista = '-1,-1'

