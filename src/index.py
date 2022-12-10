from labyrintti import Labyrintti
from leveyshaku import Leveyshaku
from seinanseuraaja import Seinanseuraaja
from testilabyrintti import Testilabyrintti

'''Täältä ajetaan kumpikin polkuhakualgoritmi kertaalleen läpi
esimerkkilabyrintilla, tulostetaan löydetty reitti ja läpikäydyt solut
kummastakin algoritmista, sekä muutama toteutuneita hakuja kuvaava tunnusluku'''

testi = Testilabyrintti(3,3,'tiheä')
laby = Labyrintti(testi.anna_labyrintti())
leveys = Leveyshaku(laby)
leveys.hae_polku_ascii()
seina = Seinanseuraaja(laby)
seina.hae_polku()
seina.piirra_polku()
print(leveys.polun_pituus())
print(seina.polun_pituus())
print(leveys.aikavaativuus())
print(seina.aikavaativuus())
print('Vaadittu aikavaativuus oli pienempi kuin O(2n+m), jossa n on kaaret ja m solmut')
print(f'2n+m = {len(laby.labyrintti)+2*laby.kaaret}')
print(leveys.o_aikavaativuus())
print(seina.o_aikavaativuus())
