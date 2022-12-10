## Viikkoraportti 6

#### Ajankäyttö
12 h

#### Mitä tein
- Lähdin koodaamaan O()-muotoisen aikavaativuuden tarkistusta
- Vaihdoin koordinaattien merkitsemisen tavan

#### Mitä opin
- Että leveyshakuni ei täytä O(n+m) aikavaativuuden vaatimusta, joka on esitelty Tietorakenteet- ja Algoritmit kurssimateriaalissa, vaikka rakensin sen hyödyntäen materiaalissa esiteltyä pseudokoodia. Tämä viittaa siihen, että koska kaarta voi kulkea kahteen suuntaan, täytyy se huomioida myös aikavaativuutta mitatessa kahdesti, eli aikavaativuus on O(2n+m)

#### Miten ohjelma on edistynyt
- Ohjelman tilanne on suhteellisen hyvä, lukuun ottamatta puutteellista testausta ja graafisen käyttöliittymän puutetta
- O()-aikavaativuuden testaus on ollut se kriittisin puute, joten on kiva saada se aluilleen

#### Mikä jäi epäselväksi
- Miten käytetyn tilan testaaminen toimii
- Miten mitattu reaaliaika muunnetaan O()-muotoon. (Tai siis vissiin ei, oletan että tarkoitus on testata eri syötteillä miten monta välivaihetta käydään läpi? En tiedä kun tätä ei ole missään kurssin materiaaleissa käyty läpi.)

#### Mitä teen seuraavaksi
Prioriteettijärjestyksessä
- Yksikkötestaus kuntoon
- Linttausta
- Luodaan kunnon kattavat testaukset aikavaativuudella ja niistä tulostuvat graafit niin algoritmin vaatiman reaaliajan kuin O()-muotoisen aikavaativuuden suhteen
- Graafinen esitys hakujen tuloksille