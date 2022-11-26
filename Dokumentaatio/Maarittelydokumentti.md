# Määrittelydokumentti
HUOM! Esitetyt algoritmit todennäköisesti vaihtuvat, kunhan koodari keksii mikä kiinnostaa ja mitä haluaa elämältä.

### Kielet
Python on projektissa käytetty ohjelmointikielikieli ja ainoa ohjelmointikieli, jolla osaan antaa järkevää palautetta ohjelmistoprojektin tasoisesta työstä.

Projekti dokumentoidaan, kommentoidaan ja koodataan suomeksi, mutta englanninkielisten töiden kommentointi ja katselmointi onnistuu.

### Projektin kuvaus
Projektissa verrataan reitinhakualgoritmeja lyhyimmän reitin löytämiseen alusta loppuun labyrintissä, jossa on monta mahdollista ratkaisua ja suhteellisen vähän seiniä.

Verrattavat algoritmit ja perustelut niiden valintaan:
- Leveyshaku (Breadth First Search): Yksinkertainen, löytää taatusti lyhyimmän reitin.
    - Aikavaativuustavoite: O(n+m) jossa m solmut ja n kaaret
- Wall follower: Yksinkertainen, käytetty jo antiikissa, saattaa olla leveyshakua nopeampi riippuen labyrintista
    - Aikavaativuustavoite: pienempi kuin O(n+m)
    - Saattaa kuulemma jäädä jumiin jos labyrintissa on syklejä. Oletan, ettei tämä tule ongelmaksi nykyisenmuotoisten labyrinttien ja käytössä olevan algoritmin kanssa, mutta katsotaan!
    - Olisiko ollut fiksumpaa etsiä valmis pseudokoodi kuin toteuttaa itse konseptin pohjalta? Todennäköisesti. Tämä kuitenkin antaa ihmiselle murusen verran serotoniinia joten tehdään nyt näin. :D
- Mikäli jää aikaa ja energiaa: Hierarchical Pathfinding A*, HPA*
    - Aikavaativuustavoite: Lähteet sanovat että pitäisi olla kymmenkertaisesti lyhyempi kuin A*, jolla O(b^d) jossa b on keskimääräinen yhteyksien määrä ja d on lyhyimmän polun pituus
    - HPA*:n ei pitäisi toimia labyrintissa jos eteneminen kohti maalia ei ole aina optimaalinen idea ja jos maalin sijainti ei ole tiedossa. Käytetyssä algoritmissa oletetaan maalin sijainti tunnetuksi ja Botea et al ovat esittävät tuloksia algoritmilla Baldur's gaten labyrinteissa, joten kiinnostaa.

Kolmen algoritmin toimintaa verrataan eri kokoisissa labyrinteissa, joissa on joko paljon tai vähän seiniä.

### Koodarin koulutusohjelma
Tietojenkäsittelytieteen kandiohjelma

### Lähteet
[Harabor, D. 5.5.2009, Clearance-based Pathfinding and Hierarchical Annotated A* Search](https://web.archive.org/web/20190411040123/http://aigamedev.com/open/article/clearance-based-pathfinding/), archive.org tiedosto, viitattu 10.11.2022

[Botea A., Müller M., Schaeffer J., 2004, Near optimal hierarchical path-finding (HPA*)](https://www.researchgate.net/publication/228785110_Near_optimal_hierarchical_path-finding_HPA)

Laaksonen, A. 2021. Tietorakenteet ja algoritmit. Kurssimoniste

[Wikipedia: Maze-solving algorithm](https://en.wikipedia.org/wiki/Maze-solving_algorithm), viitattu 10.11.2022, viimeksi editoitu 8.10.2022