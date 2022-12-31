## Testausdokumentti
Kävi silleen kivasti, että poetry lakkasi toimimasta viime metreillä ja taidot loppuivat korjata asia, joten testauksen toimivuutta on katsottu pushaamalla githubiin. :D Paitsi sitten myös actions deprekoitui, joten koko homma kaatui.

### Yksikkötestaus
[![codecov](https://codecov.io/gh/heliparv/polkuhaku/branch/main/graph/badge.svg?token=W1CWXGM2BY)](https://codecov.io/gh/heliparv/polkuhaku)

Yllä kuvattu badge on codecov:n avulla luotu token tämänhetkisestä testien haarakattavuudesta yksikkötestauksessa.

#### Yksikkötestauksen toistaminen

Ensin täytyy asentaa ohjelman riippuvuudet komennolla
```bash
poetry install
```
Ennen suorittamista avataan suoritusympäristö komennolla
```bash
poetry shell
```
Yksikkötestauksen voi suorittaa komennolla 
```bash
pytest src
```

Testiraportin voi luoda suorittamalla komennon
```bash
coverage run --branch -m pytest; coverage html
```
jolloin raportti luodaan htmlcov-kansion index.html -tiedostoon

### Algoritmien suorituskyvyn testaus
Algoritmien suorituskykyä voi testata katsomalla kuinka kauan reaaliajassa algoritmin suorittaminen eri kokoisissa ja tyyppisissä labyrinteissa kestää, tai tarkastamalla kuinka monta kertaa algoritmi käy sisimmässä for-loopissa verrattuna algoritmille annettun solmujen ja kaarten määrään. Tätä varten oleva skripti löytyy src-kansion tiedostosta suorituskyky.py ja siellä voi valita minkälaisessa labyrintissa ja miten monessa eri koossa suoritusta tarkastelee.

Kierroksia verrataan solmujen, eli lattiaruutujen sekä kaarien, eli mahdollisten siirtymien summaan. Verkkoesityksessä siirtymä esiintyy erikseen kumpaankin suuntaan, eli esim. jos ruudusta (1,1) voi siirtyä ruutuun (1,2), voi siirtyä ruudusta (1,2) ruutuun (1,1) ja nämä molemmat siirtymät lasketaan kaarina. Näin saadaan myös graafiseen esitykseen helppo nyrkkisääntö siitä, että suhdeluvun kierrokset/(solmut+kaaret) ylittäessä luvun 1, ei tavoiteltu aikavaativuus enää täyty.
