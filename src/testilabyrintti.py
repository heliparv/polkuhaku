
class Testilabyrintti:
    '''Luokkaa käytetään luomaan ASCII-muotoinen labyrinttigrafiikka, jolla voi
    testata polkuhakuun käytettyjä algoritmeja.

    Luokassa on kolme erilaista vaihtoehtoa labyrinttityypille, kustakin vaihtoehdosta
    on grafiikka, jota toistamalla saadaan aikaan labyrintti. Labyrintit ovat
    yksinkertaisia ja toisteisia, mutta toimivat riittävän hyvin
    
    Luokan muuttujat:
    labyrintti = sisältää ASCII-muotoisen labyrinttigrafiikan'''

    def __init__(self, leveys = 1, korkeus = 1, tiheys = 'harva'):
        '''Käyttää luo_labyrintti funktiota luodakseen
        labyrintin annettujen leveyden, korkeuden ja
        harva, tiheä vai siksak määrityksen perusteella.
        Luo harvan labyrintin jos käyttäjän syöte ei vastaa mitään
        labyrinttityyppiä tai syötettä ei ole.'''
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
        samoihin kulmiin labyrintissa.

        Funktiolle annetut muuttujat leveys ja korkeus
        kertovat toistojen lukumäärän'''

        toistokuvio = metodi
        toiston_leveys = len(toistokuvio[0])
        self.labyrintti = []
        for rivi in toistokuvio:
            self.labyrintti.append('#'+rivi*leveys+'#')
        self.labyrintti = self.labyrintti*korkeus
        self.labyrintti.insert(0, '#A'+'#'*toiston_leveys*leveys)
        self.labyrintti.append('#'*toiston_leveys*leveys+'B#')

    def harva(self):
        ''''Palauttaa labyrintin luontia varten harvan
        toistokuvion.'''

        return ['               ',
                '##            #',
                '     #####     ',
                '               ',
                '#      #    ###',
                '       #       ',
                '  #    #       ',
                '  #            ',
                '  #            ',
                '        ###    ']

    def tihea(self):
        ''''Palauttaa labyrintin luontia varten tiheän
        toistokuvion.'''

        return [' #       ######',
                ' # #####      #',
                '   #    ##### #',
                '#### ##   #   #',
                '       #  # #  ',
                '###### #### ###',
                '            ## ',
                '# #########  # ',
                '#        ##### ',
                '########       ']

    def siksak(self):
        '''Palauttaa labyrintin luontia varten toistokuvion,
        jolla voidaan luoda pystysuuntaista siksakkia sisältävä
        labyrintti.'''

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
