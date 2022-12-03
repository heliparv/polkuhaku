import pygame
from testilabyrintti import Testilabyrintti
from labyrintti import Labyrintti
from leveyshaku import Leveyshaku

testilaby = Testilabyrintti()
laby = Labyrintti(testilaby.labyrintti)
#leveyshaku = Leveyshaku(laby)
#leveyshaku.hae_polku()

kello = pygame.time.Clock()
print(laby.korkeus())
print(laby.leveys())

if laby.leveys()*10 <= 1500 and laby.korkeus()*10 <= 1000:
    naytto = pygame.display.set_mode((laby.leveys()*10,laby.korkeus()*10))
    dimensio = 10
else:
    xmaksimi = int(1500/laby.leveys())
    ymaksimi = int(1000/laby.korkeus())
    dimensio = min(xmaksimi, ymaksimi)
    naytto = pygame.display.set_mode((laby.leveys()*dimensio, laby.korkeus()*dimensio))

#seina = []
lattia = []
kayty = []

x = 0
y = 0
for rivi in laby.grafiikka:
    for ruutu in rivi:
        if ruutu == '#':
            #seina.append(pygame.Rect(x,y,dimensio,dimensio))
            continue
        else:
            print(x,y)
            lattia.append(pygame.Rect(x,y,dimensio,dimensio))
        x += dimensio
    y += dimensio
    x = 0

running = True
i = 0
while running:
    kello.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    
    naytto.fill((0,0,0))
    for ruutu in lattia:
        pygame.draw.rect(naytto, (255, 255, 255), ruutu)
    #if i < len(leveyshaku.esitys[i]):
     #   x,y = leveyshaku.esitys[i]
      #  kayty.append(pygame.Rect(x,y,dimensio,dimensio))
       # for ruutu in kayty:
        #    pygame.draw.rect(naytto, (150,150,150), ruutu)

    pygame.display.flip()
    kello.tick(60)
    

pygame.quit()
