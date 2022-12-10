## Testausdokumentti
Tetstit eivät tällä hetkellä ole kattavia eivätkä testaa polkuhakualgoritmeja, koska en ole vielä koodannut kyseisiä testejä.

### Yksikkötestaus
[![codecov](https://codecov.io/gh/heliparv/polkuhaku/branch/main/graph/badge.svg?token=W1CWXGM2BY)](https://codecov.io/gh/heliparv/polkuhaku)

Yllä kuvattu badge on codecov:n avulla luotu token tämänhetkisestä testien haarakattavuudesta yksikkötestauksessa.

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

### Algoritmien aikavaativuuden testaus
Ohjelman algoritmien aikavaativuusrajaksi on asetettu O(2n+m) jossa n on kaarien lukumäärä ja m solmujen lukumäärä.

Testaus suoritetaan ajamalla tiedosto aikavaativuustestaus.py, jonka voi suorittaa esimerkiksi avaamalla terminaalissa Polkuhaku-ohjelman sisältävän kansion ja suorittamalla käskyn
```bash
python3 src/aikavaativuustestaus.py
```

Testi tarkistaa aikavaativuuden kolmella eri labyrinttityypillä muutamassa eri koossa. Testauksen tuloksena saadut reaaliaikaiset aikavaatuvuudet sekä O()-muotoiset aikavaativuudet tulostuvat näytölle käyrinä. Näistä jälkimmäiset ovat suhdelukuja, jotka kuvaavat läpikäytyjen silmukoiden määrää jaettuna syötteestä lasketulla 2n+m lukumäärällä.

#### Teoriaa aikavaativuustestauksesta

Sekä leveyshaku- että seinänseuraaja-algoritmille annetaan syötteenä labyrintin verkkoesitys, jossa solmujen määrä vastaa lattiapaikkoja, jotka algoritmi voi käydä läpi. Tämä on siis algoritmille syötetty m eli solmujen lukumäärä. Sen saa suoraan tarkistamalla algoritmille syötetyn verkkoesityksen alkioiden lukumäärän

Tarvitaan myös kaarien määrä n, jota varten on olemassa labyrintti-luokassa oma muuttuja, jota kasvatetaan aina löydettäessä yhteys solmujen välille.

Leveyshaun aikavaativuustavoite on O(2n+m), joten tarkastetaan että leveyshaussa tapahtuu suorituksen aikana enintään näin monta vierailua metodin sisimmässä silmukassa. Tätä varten leveyshaku-luokan o_aika laskuri lisää lukemaan +1 joka kierroksella hae_polku funktiossa. Tietorakenteet- ja Algoritmit kurssilla esitetty aikavaativuus on O(n+m), mutta koska labyrintissa jokainen kaari on mahdollista kulkea kahteen suuntaan, leveyshaku käsittelee sen kahdesti.

Seinänseuraajalle asetettu aikavaativuustavoite on myös O(2n+m). Tätä varten seinänseuraaja-luokan o_aika laskuri lisää lukemaan +1 joka kierroksella hae_askel funktiossa. 

Suorituskykytestaus on suoritettu algoritmien yksikkötestauksen yhteydessä testaamalla, että o_aika on kolmella erilaisella testilabyrintti-luokalla luodulla labyrinttityypillä alle n+m