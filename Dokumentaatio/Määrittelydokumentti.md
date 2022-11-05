# Määrittelydokumentti

### Kielet
Python on projektissa käytetty ohjelmointikielikieli ja ainoa ohjelmointikieli, jolla osaan antaa järkevää palautetta ohjelmistoprojektin tasoisesta työstä.

Projekti dokumentoidaan, kommentoidaan ja koodataan suomeksi, mutta englanninkielisten töiden kommentointi ja katselmointi onnistuu.

### Projektin kuvaus
Projektissa verrataan reitinhakualgoritmeja satunnaisesti luodussa verkossa lyhyimmän reitin löytämiseen aloitussolmusta loppusolmuun.

Verrattavat algoritmit ja perustelut niiden valintaan:
- Leveyshaku (Breadth First Search): Yksinkertainen, löytää taatusti lyhyimmän reitin.
    - Aikavaativuustavoite: O(n+m) jossa m solmut ja n kaaret
- Fringe Search: Annetuissa aiheissa ehdotettu algoritmi, vaikuttaa kiinnostavalta.
    - Aikavaativuustavoite: Enpä ossoo sanoa kun ei lähteessä lue, varmaan parempi kuin O(n + m log n) eli Dijkstran aikavaativuus

Mikäli aikaa jää ja algoritmi on soveltuva, tarkastellaan myös Yang & Mackworth artikkelissa Hierarchical shortest pathfinding applied to route-planning for wheelchair users (2007) esittämää Hierarchical Shortest Path (HSP) algoritmia koska törmäsin siihen omassa haussani, sillä on kovat lupaukset ja kuitenkin vain kolme viittauskertaa Scopuksessa. Kiinnostelee. Aikatavoitteena artikkelin antama O(b^c l) jossa l on hierarkisten tasojen määrä, b on ala-solmujen määrä abstraktissa solmussa (m = b^l) ja c on vakio.

Verkko luodaan satunnaistetusti niin, että siinä on taatusti aina vähintään yksi reitti aloitussolmusta loppusolmuun.

Ohjelma saa syötteenä luotavan verkon solmujen lukumäärän, kaarien painojen maksimi- ja minimiarvon, jokaisesta solmusta lähtevien kaarien lukumäärän maksimi- ja minimiarvon, sekä verkkoon generoidun taatusti olemassaolevan polun pituuden kaarien lukumääränä. Huom! Kaarien satunnaistuksessa saattaa syntyä lyhyempi polku, etenkin jos solmuista lähtee paljon kaaria suhteessa verkon kokoon.

### Koodarin koulutusohjelma
Tietojenkäsittelytieteen kandiohjelma

### Lähteet
Björnsson, Y., Enzenberger, M., Holte, R.C., Schaeffer, J. 2005. Fringe search: Beating A* at pathfinding on game maps. IEEE 2005 Symposium on Computational Intelligence and Games, pp 125-132

Laaksonen, A. 2021. Tietorakenteet ja algoritmit. Kurssimoniste

Yang, S., Mackworth, A.K. 2007. Hierarchical shortest pathfinding applied to route-planning for wheelchair users. Lecture notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics). LNAI, pp. 539-550 