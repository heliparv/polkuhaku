from labyrintti import Labyrintti
from leveyshaku import Leveyshaku
from seinanseuraaja import Seinanseuraaja
from testilabyrintti import Testilabyrintti

'''Täältä koko ohjelmaa ajetaan, homma on tällä hetkellä
siinä vaiheessa että vai testailen tapahtuuko jotain'''

testi = Testilabyrintti()
laby = Labyrintti(testi.labyrintti)
leveys = Leveyshaku(laby)
seina = Seinanseuraaja(laby)
print(leveys.polun_pituus())
print(seina.polun_pituus())
print(leveys.aikavaativuus())
print(seina.aikavaativuus())