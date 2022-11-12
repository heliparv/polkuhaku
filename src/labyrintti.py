class Labyrintti:
     '''Luokka labyrintille. Tällä hetkellä palauttaa vain pyydettäessä yhden
     labyrintin, jotta saadaan ensin varsinaiset algoritmit tehtyä.
     Myöhemmin koodataan vaihtoehtoja.

     Labyrintin muodon sääntöjä: Reunat ovat aina seinää, lukuun ottamatta alku-
     ja loppupisteitä, jotka ovat aina labyrintin reunoilla. Alku- tai loppupisteet
     eivät voi olla kulmissa. Labyrintissa on vain seinää tai lattiaa sisällä.
     Labyrintissa voi liikkua pystyyn ja vaakaan jos vierekkäiset palat ovat lattiaa.
     Vinottain voi liikkua jos vinoruutu on lattiaa ja vähintään toinen lähtöruudun
     ja vinoruudun vieressä olevista ruuduista on lattiaa.

     Funktioita:
     __init__: alustusfunktio. Mikäli grafiikkaa ei ole annettu, käyttää
     esimerkkigrafiikkaa. Jos grafiikka on annettu, asettaa sen labyrintin grafiikaksi
     Käyttää lue_labyrintti -funktiota luodakseen grafiikasta sanakirjaesityksen, joka
     kuvaa joka ruudulle minne siitä on pääsy.

     lue_labyrintti: Tekee labyrintin grafiikasta sanakirjaesityksen käyttämällä
     lue_pystyreunat-, lue_vaakareunat- ja lue_sisus -funktioita.

     luo_solmut: alustaa kaikki labyrintin sisällä olevat solmut, jottei niitä tarvitse
     luoda myöhemmin ja tarkistaa luennan yhteydessä ovatko jo olemassa.

     lue_pystyreunat: funktio lukee annetun grafiikan pystyreunat etsien alku- tai
     loppupistettä, jotka merkitsee labyrintin solmuesitykseen. Ei tarkastele
     nurkkapaloja.

     lue_vaakareunat: funktio lukee annetun grafiikan vaakareunat etsien alku- tai
     loppupistettä, jonka merkitsee labyrintin solmuesitykseen. Ei tarkastele
     nurkkapaloja.

     lue_sisus: Funktio käy läpi annetun grafiikan muut kuin reunapalat ja merkitsee
     labyrintin sanakirjaesitykseen mihin ruutuihin mistäkin ruudusta voi liikkua.
     '''
     def __init__(self, grafiikka = 0):
          if grafiikka == 0:
               self.__grafiikka = ['#A##########',
                                   '# #  #     #',
                                   '# #     #  #',
                                   '#     ##   #',
                                   '###    ##  #',
                                   '#    ###  ##',
                                   '#      #   #',
                                   '##########B#',
                                   ]
          else:
               self.__grafiikka = grafiikka
          self.__labyrintti = self.lue_labyrintti()

     def lue_labyrintti(self):
          labyrintti = {}
          self.luo_solmut(labyrintti)
          #self.lue_pystyreunat(labyrintti)
          self.lue_vaakareunat(labyrintti)
          #self.lue_sisus(labyrintti)
          return labyrintti

     def luo_solmut(self, labyrintti):
          for i in range(1, len(self.__grafiikka)-1):
               for j in range(1, len(self.__grafiikka[0])-1):
                    labyrintti[f'{i},{j}'] = []
     
     def lue_pystyreunat(self, labyrintti):
          for reuna in [0, len(self.__grafiikka[0])-1]:
               for i in range(1, len(self.__grafiikka)-1):
                    if self.__grafiikka[i][reuna] in ['A', 'B']:
                         labyrintti[f'{i},{reuna}'] = []
                         if reuna == 0:
                              ero = 1
                         else:
                              ero = -1
                         if self.__grafiikka[i][reuna+ero] == ' ':
                              labyrintti[f'{i},{reuna}'].append(f'{i},{reuna+ero}')
                              labyrintti[f'{i},{reuna+ero}'].append(f'{i},{reuna}')
                              if self.__grafiikka[i-1][reuna+ero] == ' ':
                                   labyrintti[f'{i},{reuna}'].append(f'{i-1},{reuna+ero}')
                                   labyrintti[f'{i-1},{reuna+ero}'].append(f'{i},{reuna}')
                              if self.__grafiikka[i+1][reuna+ero] == ' ':
                                   labyrintti[f'{i},{reuna}'].append(f'{i+1},{reuna+ero}')
                                   labyrintti[f'{i+1},{reuna+ero}'].append(f'{i},{reuna}')
                         if self.__grafiikka[i][reuna] == 'A':
                              labyrintti['alku'] = f'{i},{reuna}'
                         else:
                              labyrintti['loppu'] = f'{i},{reuna}'
          
     def lue_vaakareunat(self, labyrintti):
          for reuna in [0, len(self.__grafiikka)-1]:
               for j in range(1, len(self.__grafiikka[0])-1):
                    if self.__grafiikka[reuna][j] in ['A', 'B']:
                         labyrintti[f'{reuna},{j}'] = []
                         if reuna == 0:
                              ero = 1
                         else:
                              ero = -1
                         if self.__grafiikka[reuna+ero][j] == ' ':
                              labyrintti[f'{reuna},{j}'].append(f'{reuna+ero},{j}')
                              labyrintti[f'{reuna+ero},{j}'].append(f'{reuna},{j}')
                              if self.__grafiikka[reuna+ero][j-1] == ' ':
                                   labyrintti[f'{reuna},{j}'].append(f'{reuna+ero},{j-1}')
                                   labyrintti[f'{reuna+ero},{j-1}'].append(f'{reuna},{j}')
                              if self.__grafiikka[reuna+ero][j-1] == ' ':
                                   labyrintti[f'{reuna},{j}'].append(f'{reuna+ero},{j-1}')
                                   labyrintti[f'{reuna+ero},{j-1}'].append(f'{reuna},{j}')
                         if self.__grafiikka[reuna][j] == 'A':
                              labyrintti['alku'] = f'{reuna},{j}'
                         else:
                              labyrintti['loppu'] = f'{reuna},{j}'
     
     def lue_sisus(self, labyrintti):
          for i in range(1,len(self.__grafiikka)-1):
               for j in range(1,len(self.__grafiikka[0])-1):
                    if self.__grafiikka[i][j] == '#':
                         continue
                    else:
                         if self.__grafiikka[i+1][j+1] == ' ' and (self.__grafiikka[i+1][j] == ' ' or self.__grafiikka[i][j+1] == ' '):
                              labyrintti[f'{i},{j}'].append(f'{i+1},{j+1}')
                              labyrintti[f'{i+1},{j+1}'].append(f'{i},{j}')
                         if self.__grafiikka[i+1][j] == ' ':
                              labyrintti[f'{i},{j}'].append(f'{i+1},{j}')
                              labyrintti[f'{i+1},{j}'].append(f'{i},{j}')
                         if self.__grafiikka[i][j+1] == ' ':
                              labyrintti[f'{i},{j}'].append(f'{i},{j+1}')
                              labyrintti[f'{i},{j+1}'].append(f'{i},{j}')

     def anna_labyrintti(self):
          return self.__labyrintti
     
     def anna_grafiikka(self):
          return self.__grafiikka