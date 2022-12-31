## Ohjelman yleisrakenne
- Index: Käynnistää graafisen käyttöliittymän
- Polkuhaku: Toteuttaa ohjelman graafisen käyttöliittymän ja koordinoi ohjelman suoritusta
- Testilabyrintti: Luokka antaa valinnan perusteella toistorakenteisia labyrintteja, joita voi valita kolmesta eri tyypistä. Luo ASCII-muotoisen grafiikan, jota Labyrintti-luokka osaa tulkita
- Labyrintti: Tämä luokka lukee ASCII-muotoisen labyrinttigrafiikan ja muodostaa siitä sanakirjamuotoisen verkkorakenteen algoritmeille käsiteltäväksi.
- Leveyshaku: Luokka käsittelee Labyrintti-oliota ja osaa suorittaa leveyshaun. Algoritmin lähteenä on Laaksonen (2021) Tietorakenteet ja Algoritmit kurssimoniste. Tallentaa sekä tuloksen että erinäisiä apurakenteita suorituskykymittausta ja graafista esitystä varten.
- Seinänseuraaja: Luokka käsittelee Labyrintti-oliota ja osaa suorittaa seinänseuraaja-algoritmin. Algoritmi on Wikipediassa esitetyn seinänseuraamisalgoritmin idean pohjalta muodostettu, mutta ilman pseudokoodilähdettä kehitetty. Tallentaa sekä tuloksen että erinäisiä apurakenteita suorituskykymittausta ja graafista esitystä varten. 

## Saavutetut aikavaativuudet
Leveyshaulla saavutetaan aikavaativuus O(n+m) jossa n on kaarien (mahdollisten liikkumasuuntien) lukumäärä ja m solmujen (lattiaruutujen) lukumäärä. Koska n on labyrintissa korkeintaan 8, on aikavaativuus käytännössä O(m)

Seinänseuraaja-algoritmi on vahvasti graafiseen labyrinttimuotoon sidottu, joten sen aikavaativuus on O(m) jossa m on solmujen (lattiaruutujen) lukumäärä.

## Työn mahdolliset puutteet ja parannusehdotukset
- Testaus. Pelkästään ohjelman toiminnallisuuden pystyyn saaminen on ollut iso haaste käytettävissä olleen ajan ja energian puitteissa, joten tein valinnan saada aikaan testaamaton ohjelma sen sijaan että olisi ollut keskeneräisempi ohjelma jossa testausta on. Mikä ei ole silleen hirvittävän ammattimainen valinta käpistelijälle :D
- HPA* algoritmi jäi toteuttamatta ja olisi ollut kiva kokeilla
- Algoritmit eivät osaa käsitellä umpikujaa, mikä toki ei ole ongelma kun ohjelmalle voi nyt syöttää vain labyrintteja ilman umpikujia
- Olisi kiva jos algoritmille voisi syöttää oman labyrintin tai generoida sattumanvaraisen labyrintin, mutta tämä ei ollut ykkösprioriteetti ohjelmalla jonka tarkoitus oli käsitellä algoritmeja polun etsimiseen

## Lähteet
Laaksonen, A. 2021. Tietorakenteet ja algoritmit. Kurssimoniste

[Wikipedia: Maze-solving algorithm](https://en.wikipedia.org/wiki/Maze-solving_algorithm), viitattu 10.11.2022, viimeksi editoitu 8.10.2022

#### Käyttämättömät lähteet joita katselin toiveikkaana
[Harabor, D. 5.5.2009, Clearance-based Pathfinding and Hierarchical Annotated A* Search](https://web.archive.org/web/20190411040123/http://aigamedev.com/open/article/clearance-based-pathfinding/), archive.org tiedosto, viitattu 10.11.2022

[Botea A., Müller M., Schaeffer J., 2004, Near optimal hierarchical path-finding (HPA*)](https://www.researchgate.net/publication/228785110_Near_optimal_hierarchical_path-finding_HPA)