'''Väliaikainen testilabyrintti jota käyttää siihen asti
että saa labyrintin generoivan kirjaston käyttöön'''

class Testilabyrintti:
    def __init__(self):
        self.labyrintti =['#A##########################',
            '#                                        #',
            '#####################      #             #',
            '#                          #             #',
            '#        ###################             #',
            '#           #              #   ###########',
            '#           #        #     #             #',
            '#           #        #     #             #',
            '#           #        #     #####         #',
            '#                    #                   #',
            '#               #                        #',
            '########################################B#']
    
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
        ''''Palauttaa labyrintin luontia varten harvan
        toistokuvion. Tätä toistaen saadaan aikaan
        labyrintti, jossa on paljon seiniä'''

        return ['    ##### ## # ',
                '### #  ##  # # ',
                '    ##  # #    ',
                '###       #####',
                '    # ##       ',
                '#####   ### ###',
                '#       #      ',
                '# ####  #  ####',
                '   # # ###     ',
                '#### #     ### ']
