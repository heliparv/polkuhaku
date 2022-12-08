'''Väliaikainen testilabyrintti jota käyttää siihen asti
että saa labyrintin generoivan kirjaston käyttöön'''

class Testilabyrintti:
    def __init__(self, leveys = 1, korkeus = 1, tiheys = 'harva'):
        '''Käyttää omaa luo_labyrintti funktiota luodakseen
        labyrintin annettujen leveyden, korkeuden ja 
        harva vai ei määrityksen perusteella'''
        self.labyrintti = []
        if leveys > 0 and korkeus > 0:
            if tiheys == 'harva':
                self.luo_labyrintti(leveys, korkeus, self.harva())
            else:
                self.luo_labyrintti(leveys, korkeus, self.tihea())
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
        labyrintti, jossa on vähän seiniä '''

        return ['      #   #    ',
                '##        #  ##',
                '          #    ',
                '######    #  # ',
                '   #         # ',
                '   #    ###### ',
                '             # ',
                '  #####      # ',
                '      #   #  # ',
                ' #    #   #    ']

    def tihea(self):
        ''''Palauttaa labyrintin luontia varten tiheän
        toistokuvion. Tätä toistaen saadaan aikaan
        labyrintti, jossa on paljon seiniä'''

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

    def anna_labyrintti(self):
        return self.labyrintti


laby = Testilabyrintti(4,4, 'kappyra')
