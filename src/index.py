from labyrintti import Labyrintti
from leveyshaku import Leveyshaku
from testilabyrintti import Testilabyrintti

'''Täältä koko ohjelmaa ajetaan, homma on tällä hetkellä
siinä vaiheessa että vai testailen tapahtuuko jotain'''

testi = Testilabyrintti()
laby = Labyrintti(testi.labyrintti)
leveys = Leveyshaku(laby)