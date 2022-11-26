## Testausdokumentti

### Yksikkötestaus
[![codecov](https://codecov.io/gh/heliparv/polkuhaku/branch/main/graph/badge.svg?token=W1CWXGM2BY)](https://codecov.io/gh/heliparv/polkuhaku)

Yllä kuvattu badge on codecov:n avulla luotu token tämänhetkisestä testien haarakattavuudesta.

#### Yksikköestauksen toistaminen

Ensin täytyy asentaa ohjelman riippuvuudet komennolla
```bash
poetry install
```
Ennen suorittamista avataan suoritusympäristö komennolla
```bash
poetry shell
```

Testiraportin voi luoda suorittamalla komennon
```bash
coverage run --branch -m pytest; coverage html
```
jolloin raportti luodaan htmlcov-kansion index.html -tiedostoon

### Kurssin vaatima testaus
En ole aloittanut, huppista :')