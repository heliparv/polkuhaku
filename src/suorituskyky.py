from labyrintti import Labyrintti
from leveyshaku import Leveyshaku
from seinanseuraaja import Seinanseuraaja
from testilabyrintti import Testilabyrintti
import pandas as pd
import matplotlib.pyplot as plt

'''Tällä skriptillä voit luoda raportteja algoritmien suoritusajasta joko
reaaliaikaisena tai algoritmin suorittamien looppien määränä verrattuna
algoritmille syötettynä lattiaruutujen ja mahdollisten liikkeiden määrään

Koodi on huonolaatuinen spagetti, pahoittelut :D'''

#Valitse labyrintin tyyppi: 'harva', 'tiheä' tai 'siksak'
tyyppi = 'tiheä'

#Valitse labyrintin pienin koko, suurin koko ja testausintervalli, eli testattavien kokojen
# välimatka, esim intervalli 3 testaa 1x1, 4x4, 7x7...
pienin = 1
suurin = 51
intervalli = 5

#Valitse mitä testataan. 'aika' testaa suoritusaikaa reaaliajassa ja 'kierrokset' suoritettujen
#looppien määrää syötteen kokoon verrattuna
aika = True
kierrokset = True

#Valitse missä muodossa haluat tulokset. 'teksti' antaa tekstitulosteen, 'grafiikka' kuvaajan
teksti = True
grafiikka = True


#Älä muokkaa seuraavaa koodia, täällä suoritetaan testaus

def suorita_reaaliaikatestaus(labyrintin_tyyppi, pienin_leveys, suurin_leveys, intervalli):
    sarakkeet = ['dimensio', 'reaaliaika'] 
    leveyshaku = pd.DataFrame(columns=sarakkeet)
    seinanseuraaja = pd.DataFrame(columns=sarakkeet)
    for i in range(pienin_leveys, suurin_leveys+1, intervalli):
        grafiikka = Testilabyrintti(i, i, labyrintin_tyyppi)
        laby = Labyrintti(grafiikka.labyrintti)

        leveys = Leveyshaku(laby)
        leveys.hae_polku()
        leveyshaku.loc[i-1] = [i, leveys.aika]

        seina = Seinanseuraaja(laby)
        seina.hae_polku()
        seinanseuraaja.loc[i-1] = [i, seina.aika]
    
    return leveyshaku, seinanseuraaja

def suorita_kierrosvertailu(labyrintin_tyyppi, pienin_leveys, suurin_leveys, intervalli):
    sarakkeet = ['dimensio', 'kierrokset'] 
    leveyshaku = pd.DataFrame(columns=sarakkeet)
    seinanseuraaja = pd.DataFrame(columns=sarakkeet)
    for i in range(pienin_leveys, suurin_leveys+1, intervalli):
        grafiikka = Testilabyrintti(i, i, labyrintin_tyyppi)
        laby = Labyrintti(grafiikka.labyrintti)
        o_aikaraja = len(laby.labyrintti)+laby.kaaret

        leveys = Leveyshaku(laby)
        leveys.hae_polku()
        leveyshaku.loc[i-1] = [i, leveys.kierrokset/o_aikaraja]

        seina = Seinanseuraaja(laby)
        seina.hae_polku()
        seinanseuraaja.loc[i-1] = [i, seina.kierrokset/o_aikaraja]
    
    return leveyshaku, seinanseuraaja

def piirra_grafiikka(data, testi, labyrinttityyppi, algoritmi, y_akselin_nimi):
    plt.plot(data['dimensio'],data[testi])
    plt.title(f"{algoritmi} {labyrinttityyppi} labyrintissa, {testi}")
    plt.ylabel(y_akselin_nimi)
    plt.xlabel('Labyrintin koko yksiköissä')
    plt.show()


tyyppi_kuvaajalle = {'harva':'harvassa', 'tiheä':'tiheässä', 'siksak':'siksakkaavassa'}

if aika:
    leveyshaku, seinanseuraaja = suorita_reaaliaikatestaus(tyyppi, pienin, suurin, intervalli)

    if teksti:
        print('Leveyshaun tulokset reaaliaikasessa suorituksessa')
        print(leveyshaku)
        print('')
        print('Seinänseuraajan tulokset reaaliaikaisessa suorituksessa')
        print(seinanseuraaja)
        print('')

    if grafiikka:
        piirra_grafiikka(leveyshaku, 'reaaliaika', tyyppi_kuvaajalle[tyyppi], 'Leveyshaku', 'aika')
        piirra_grafiikka(seinanseuraaja, 'reaaliaika', tyyppi_kuvaajalle[tyyppi], 'Seinänseuraaja', 'aika')

if kierrokset:
    leveyshaku, seinanseuraaja = suorita_kierrosvertailu(tyyppi, pienin, suurin, intervalli)

    if teksti:
        print('Leveyshaun tulokset vertailtaessa kierroksia syötteen kokoon')
        print(leveyshaku)
        print('')
        print('Seinänseuraajan tulokset vertailtaessa kierroksia syötteen kokoon')
        print(seinanseuraaja)

    if grafiikka:
        piirra_grafiikka(leveyshaku, 'kierrokset', tyyppi_kuvaajalle[tyyppi], 'Leveyshaku', 'kierrokset/(solmut+kaaret)')
        piirra_grafiikka(seinanseuraaja, 'kierrokset', tyyppi_kuvaajalle[tyyppi], 'Seinänseuraaja', 'kierrokset/(solmut+kaaret)')