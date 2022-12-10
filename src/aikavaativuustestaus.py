from labyrintti import Labyrintti
from leveyshaku import Leveyshaku
from seinanseuraaja import Seinanseuraaja
from testilabyrintti import Testilabyrintti
import pandas as pd
import matplotlib.pyplot as plt

'''Testaa molemmat algoritmit kolmella labyrinttityypillä ja luo
sekä sanallisen että graafisen raportin

Koodi on melkoinen spagetti tällähetkellä, refaktoroidaan joskus myöhemmin

HUOM! Koodilla saattaa kestää hieman aikaa pyöriä

Ohjelman algoritmien aikavaativuusrajaksi on asetettu O(2n+m)
jossa n on kaarien lukumäärä ja m solmujen lukumäärä.'''

def suorita_haut(labyrintin_tyyppi):
    sarakkeet = ['dimensio', 'reaaliaika', 'O-aika'] 
    leveyshaku = pd.DataFrame(columns=sarakkeet)
    seinanseuraaja = pd.DataFrame(columns=sarakkeet)
    for i in range(1,52, 5):
        grafiikka = Testilabyrintti(i, i, labyrintin_tyyppi)
        laby = Labyrintti(grafiikka.anna_labyrintti())
        o_aikaraja = len(laby.labyrintti)+2*laby.kaaret

        leveys = Leveyshaku(laby)
        leveys.hae_polku()
        leveyshaku.loc[i-1] = [i, leveys.aika, leveys.o_aika/o_aikaraja]

        seina = Seinanseuraaja(laby)
        seina.hae_polku()
        seinanseuraaja.loc[i-1] = [i, seina.aika, seina.o_aika/o_aikaraja]
    
    return leveyshaku, seinanseuraaja

leveys_harva, seina_harva = suorita_haut('harva')
leveys_tihea, seina_tihea = suorita_haut('tihea')
leveys_siksak, seina_siksak = suorita_haut('siksak')

if leveys_harva.max()[2] <= 1 and leveys_tihea.max()[2] <= 1 and leveys_siksak.max()[2] <= 1:
    print('Leveyshaun aikavaativuus on korkeintaan O(2n+m)')
else:
    print('Leveyshaun aikavaativuus ylittää joskus O(2n+m)')

if seina_harva.max()[2] <= 1 and seina_tihea.max()[2] <= 1 and seina_siksak.max()[2] <= 1:
    print('Seinänseuraajan aikavaativuus on korkeintaan O(2n+m)')
else:
    print('Seinänseuraajan aikavaativuus ylittää joskus O(2n+m)')

plt.plot(leveys_harva['dimensio'],leveys_harva['O-aika'])
plt.title("Leveyshaku harvassa labyrintissa, silmukat/(2n+m)")
plt.ylabel('Labyrintin koko yksiköissä')
plt.show()

plt.plot(leveys_tihea['dimensio'],leveys_tihea['O-aika'])
plt.title("Leveyshaku tiheässä labyrintissa, silmukat/(2n+m)")
plt.ylabel('Labyrintin koko yksiköissä')
plt.show()

plt.plot(leveys_siksak['dimensio'],leveys_siksak['O-aika'])
plt.title("Leveyshaku siksakkaavassa labyrintissa, silmukat/(2n+m)")
plt.ylabel('Labyrintin koko yksiköissä')
plt.show()

plt.plot(leveys_harva['dimensio'],leveys_harva['reaaliaika'])
plt.title("Leveyshaku harvassa labyrintissa, reaaliaika")
plt.ylabel('Labyrintin koko yksiköissä')
plt.show()

plt.plot(leveys_tihea['dimensio'],leveys_tihea['reaaliaika'])
plt.title("Leveyshaku tiheässä labyrintissa, reaaliaika")
plt.ylabel('Labyrintin koko yksiköissä')
plt.show()

plt.plot(leveys_siksak['dimensio'],leveys_siksak['reaaliaika'])
plt.title("Leveyshaku siksakkaavassa labyrintissa, reaaliaika")
plt.ylabel('Labyrintin koko yksiköissä')
plt.show()

plt.plot(seina_harva['dimensio'],seina_harva['O-aika'])
plt.title("Seinänseuraaja harvassa labyrintissa, silmukat/(2n+m)")
plt.ylabel('Labyrintin koko yksiköissä')
plt.show()

plt.plot(seina_tihea['dimensio'],seina_tihea['O-aika'])
plt.title("Seinänseuraaja tiheässä labyrintissa, silmukat/(2n+m)")
plt.ylabel('Labyrintin koko yksiköissä')
plt.show()

plt.plot(seina_siksak['dimensio'],seina_siksak['O-aika'])
plt.title("Seinänseuraaja siksakkaavassa labyrintissa, silmukat/(2n+m)")
plt.ylabel('Labyrintin koko yksiköissä')
plt.show()

plt.plot(seina_harva['dimensio'],seina_harva['reaaliaika'])
plt.title("Seinänseuraaja harvassa labyrintissa, reaaliaika")
plt.ylabel('Labyrintin koko yksiköissä')
plt.show()

plt.plot(seina_tihea['dimensio'],seina_tihea['reaaliaika'])
plt.title("Seinänseuraaja tiheässä labyrintissa, reaaliaika")
plt.ylabel('Labyrintin koko yksiköissä')
plt.show()

plt.plot(seina_siksak['dimensio'],seina_siksak['reaaliaika'])
plt.title("Seinänseuraaja siksakkaavassa labyrintissa, reaaliaika")
plt.ylabel('Labyrintin koko yksiköissä')
plt.show()
