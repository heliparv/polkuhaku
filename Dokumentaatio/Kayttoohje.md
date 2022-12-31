## Käyttöohje

#### Ohjelman käsittelemät labyrintit
- Ohjelma on tehty käsittelemään labyrintteja, joissa reunimmaiset ruudut ovat seinää ja seinät ovat saman kokoisia kuin lattiaruudut
- Labyrintin alku ja loppu sijaitsevat aina seinillä eivätkä koskaan nurkissa
- Labyrintissa voi kulkea sivuille, ylös ja alas mikäli sivuiltaan koskettavat lattian osat ovat molemmat lattiaa.
- Labyrintissa voi kulkea vinottain mikäli lattiaa ovat sekä määränpää että jompi kumpi ruuduista jotka ovat määränpään ja lähtöruudun kanssa naapureita
- Vinottaisliike lasketaan saman pituiseksi kuin muut liikkeet, koska näin saadaan algoritmeille enemmän käsiteltävää, mutta käsittely pysyy riittävän yksinkertaisena

### Ohjelman käyttäminen
Ohjelma käynnistetään suorittamalla src-kansiossa oleva index.py tiedosto. Tämän voi tehdä esimerkiksi terminaalissa navigoimalla polkuhaun sisältämään kansioon ja käyttämällä komentoa
```bash
python3 src/index.py
```
tai vaikkapa vscodessa avaamalla index.py tiedoston ja painamalla play.

Ohjelma toimii näppäinkomennoilla. Kaikilla ruuduilla P tarkoittaa paluuta ja vie sinut edelliselle ruudulle. Muuten käytössä olevat komennot näkyvät ruudulla.

Ohjelmassa valitaan ensin labyrintin tyyppi tarjolla olevista vaihtoehdoista, jotka kuvaavat toistuvia lattialaattoja. Sitten valitaan labyrintin koko ilmoittamalla luku n, jolloin muodostetaan n*n kokoinen labyrintti jossa n on lattialaatan toistojen määrä.

Tämän jälkeen voit valita minkä algoritmin suorituksesta haluat katsoa graafisen esityksen. Esityksessä merkitään missä lattiaruudussa algoritmi on vieraillut ja lopuksi näytetään vihrein palloin mistä löydetty reitti kulkee.

Seinänseuraaja-algoritmin tapauksessa merkitään punaisin palloin suunnat, joista algoritmi on etsinyt kulkureittiä ja pallo muuttuu tummemmaksi jos sitä tarkastellaan uudestaan. Myös polku muuttuu tummemmaksi jos samasta kohdasta kuljetaan kahdesti.

### Algoritmien suorituskyvyn testaus
Mikäli haluaa tarkastella eri algoritmien suoritusta joko reaaliajassa tai suoritettujen ohjelman looppien määränä, on sitä varten olemassa tekstimuotoinen skripti suorituskyky.py

Vaihtamalla ohjelman alussa olevien muuttujien arvoja voit kertoa skriptille mitä asioita haluat tarkastella ja haluatko tulosteen tekstimuotoisena, kuvaajana vai molempina.
