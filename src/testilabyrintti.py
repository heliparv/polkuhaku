'''Luokkaa Testilabyrintti käytetään yksittäisen labyrintin luomiseen
Luokkaa Testipaketti käytetään aikavaativuustestauksissa käytettyjen
testilabyrinttikirjastojen luomiseen'''

class Testilabyrintti:
    ''''Luokka palauttaa toivotunlaisia labyrinttejä, joita voi käyttää
    polun hakemiseen käytettyjen algoritmien testaukseen. Labyrintit ovat
    yksinkertaisia ja toisteisia, mutta toimivat riittävän hyvin aikavaativuuden
    testaamiseen'''

    def __init__(self, leveys = 1, korkeus = 1, tiheys = 'harva'):
        '''Käyttää omaa luo_labyrintti funktiota luodakseen
        labyrintin annettujen leveyden, korkeuden ja
        harva, tiheä vai siksak määrityksen perusteella.
        Luo harvan labyrintin jos käyttäjällä käy typo'''
        self.labyrintti = []
        if leveys > 0 and korkeus > 0:
            if tiheys == 'siksak':
                self.luo_labyrintti(leveys, korkeus, self.siksak())
            elif tiheys == 'tiheä':
                self.luo_labyrintti(leveys, korkeus, self.tihea())
            else:
                self.luo_labyrintti(leveys, korkeus, self.harva())
        else:
            self.luo_labyrintti(1, 1, self.harva())

    def luo_labyrintti(self, leveys: int, korkeus: int, metodi):
        '''Luo labyrintin käyttäen toistokuviota.
        Toistokuvioita voi laittaa vierekkäin ja päällekäin
        halutun verran ja alku- ja loppusolmu tulevat aina
        labyrintin ylä- ja alakulmaan.

        Funktiolle annetut muuttujat leveys ja korkeus
        kertovat toistojen lukumäärän'''

        toistokuvio = metodi
        toiston_leveys = 15
        self.labyrintti = []
        for rivi in toistokuvio:
            self.labyrintti.append('#'+rivi*leveys+'#')
        self.labyrintti = self.labyrintti*korkeus
        self.labyrintti.insert(0, '#A'+'#'*toiston_leveys*leveys)
        self.labyrintti.append('#'*toiston_leveys*leveys+'B#')

    def harva(self):
        ''''Palauttaa labyrintin luontia varten harvan
        toistokuvion. Tätä toistaen saadaan aikaan
        labyrintti, jossa on vähän seiniä ja joka on
        molemmille algoritmeille helppo '''

        return ['      #   #    ',
                '##        #  ##',
                '          #    ',
                '   ########  # ',
                '             # ',
                '   #######   # ',
                '             # ',
                '      #      # ',
                '      #   #  # ',
                ' #    #   #    ']

    def tihea(self):
        ''''Palauttaa labyrintin luontia varten tiheän
        toistokuvion. Tätä toistaen saadaan aikaan
        labyrintti, jossa on paljon seiniä

        Suunniteltu suosimaan leveyshakualgoritmia'''

        return [' #       ######',
                ' # #####      #',
                ' # #   ###### #',
                '   ###        #',
                '#### # ###### #',
                '       #    #  ',
                '###### #### ###',
                '     #      ## ',
                '# #### ####  # ',
                '#        ##### ',
                '########       ']

    def siksak(self):
        '''Palauttaa labyrintin luontia varten toistokuvion,
        jolla voidaan luoda pystysuuntaista siksakkia suosiva
        labyrintti.

        Suunniteltu suosimaan seinänseuraajaa'''

        return ['   #     #     ',
                '   #  #  #  #  ',
                '   #  #  #  #  ',
                '#  #  #  #  #  ',
                '#  #  #  #  #  ',
                '#  #  #     #  ',
                '#     #  #  #  ',
                '#     #  #  #  ',
                '#  #  #  #  #  ',
                '#  #     #     ',]

    def anna_labyrintti(self):
        return self.labyrintti
