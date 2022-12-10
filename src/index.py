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
print(f'Labyrintissa solmujen ja kaarien yhteismäärä oli n+m = {len(laby.labyrintti)+laby.kaaret}')
print(leveys.O_aikavaativuus())
print(seina.O_aikavaativuus())