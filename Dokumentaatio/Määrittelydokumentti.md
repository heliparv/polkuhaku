# Määrittelydokumentti

### Kielet
Python on projektissa käytetty ohjelmointikielikieli ja ainoa ohjelmointikieli, jolla osaan antaa järkevää palautetta ohjelmistoprojektin tasoisesta työstä.

Projekti dokumentoidaan, kommentoidaan ja koodataan suomeksi, mutta englanninkielisten töiden kommentointi ja katselmointi onnistuu.

### Projektin kuvaus
Projektissa verrataan reitinhakualgoritmeja lyhyimmän reitin löytämiseen alusta loppuun labyrintissä, jossa on monta mahdollista ratkaisua ja suhteellisen vähän seiniä.

Verrattavat algoritmit ja perustelut niiden valintaan:
- Leveyshaku (Breadth First Search): Yksinkertainen, löytää taatusti lyhyimmän reitin.
    - Aikavaativuustavoite: O(n+m) jossa m solmut ja n kaaret
- Wall follower: Yksinkertainen, käytetty jo antiikissa, saattaa olla leveyshakua nopeampi
    - Aikavaativuustavoite: pienempi kuin O(n+m)
- Hierarchical Pathfinding A*
    - Aikavaativuustavoite: Lähteet sanovat että pitäisi olla kymmenkertaisesti lyhyempi kuin A*, jolla O(b^d) jossa b on keskimääräinen yhteyksien määrä ja d on lyhyimmän polun pituus

Kolmen algoritmin toimintaa verrataan eri kokoisissa labyrinteissa, joissa on joko paljon tai vähän seiniä.

### Koodarin koulutusohjelma
Tietojenkäsittelytieteen kandiohjelma

### Lähteet
[Harabor, D. 5.5.2009, Clearance-based Pathfinding and Hierarchical Annotated A* Search](https://web.archive.org/web/20190411040123/http://aigamedev.com/open/article/clearance-based-pathfinding/), archive.org tiedosto, viitattu 10.11.2022

Laaksonen, A. 2021. Tietorakenteet ja algoritmit. Kurssimoniste

[Wikipedia: Maze-solving algorithm](https://en.wikipedia.org/wiki/Maze-solving_algorithm), viitattu 10.11.2022, viimeksi editoitu 8.10.2022