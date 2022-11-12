from collections import deque

class Leveyshaku:
    '''Luokka leveyshaun toteuttamiseen, tässä kohtaa erittäin tynkä
    koska lähden 10 min tämän aloittamisen jälkeen kohti vujuja :D '''

    def __init__(self):
        #jaahas, mitäs tänne laittais. Noh, kattellaan
        self.aa = "Minä olen vielä turha muuttuja"
    
    def hae_polku(self, labyrintti: dict):
        kayty = set()
        #seuraa copypaste koodia omista TiRan harkoista = yritän keksiä miten toimia
        kayty.add(labyrintti['alku'])
        loppu = labyrintti['loppu']
        jono = deque()
        jono.append(labyrintti['alku'])
        while jono:
            paikka = jono.popleft()
            for naapuri in [paikka]:
                if naapuri == loppu:
                    return #TODO reitti
                if naapuri in kayty:
                    continue
                jono.append(naapuri)
                kayty.add(naapuri)
                #TODO reitti 
