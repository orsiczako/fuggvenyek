## Sziasztok! 
### Jeleztétek, hogy még kicsit foglalkozzunk a függvényekkel, így még írtam pár feladatot, továbbá magyarázatot, amit ebben a README file-ban meg is találhattok. A feladatoknál értelemszerűen találhattok feladatokat, azoknak a leírását és megoldását, ha a platformra beléptek, ott Trinketben ezeket meg is tudjátok oldani önállóan. Mindemellett észleltem, hogy a paraméterátadás sem túl tiszta, így a feladatok között olyat is megtalálhattok, ami célzottan ezt gyakoroltatja, nézzétek át alaposan a kódokat és próbáljátok megtippelni, hogy egy egy paraméterátadásnál mit ad majd vissza a függvény. Ha esetleg lenne igény arra, hogy írjak még össze feladatokat, vagy esetleg kérdésetek van, akkor keressetek bármikor, igyekszem minél hamarabb és legjobb tudásom szerint válaszolni, az e-mail címem: czakorsi@gmail.com
### Jó programozást, istenkirályok vagytok!


## Függvények – Mi ez az egész?

A függvények egyfajta „eszközök” a programozásban, amikkel különféle feladatokat könnyen el lehet végezni. Gondolj rájuk úgy, mint kis „programdarabokra”, amiket bármikor használhatunk, ha ugyanazt a feladatot többször kell megoldanunk.

### Miért hasznosak a függvények?
A függvények segítségével:
1. Rövidebbé tehetjük a kódunkat, mert nem kell ugyanazt újra és újra leírni.
2. Logikusabbá, átláthatóbbá válik a program.
3. Könnyebben tudjuk tesztelni és hibát keresni a kódban, mert kisebb, jól körülhatárolható részekkel dolgozunk.

### Függvény létrehozása és használata
Egy függvény létrehozásához a `def` kulcsszót használjuk. Ezzel jelöljük, hogy most egy függvényt szeretnénk létrehozni. Utána megadunk neki egy nevet, hogy később is felismerjük. A függvény neve után zárójelben helyezkednek el az úgynevezett „paraméterek” (erről később lesz szó), majd egy kettőspontot teszünk a sor végére.

#### Alap Példa
Nézzük meg a legeslegegyszerűbb függvényt, ami semmit nem csinál, csak kiírja, hogy „Helló!”:

```python
def koszones():
    print("Helló!")
```

#### Bontjuk szét, mi történik itt:
1. `def`: Ezzel kezdjük a függvény létrehozását.
2. `koszones`: Ez a függvény neve. Bármi lehet a neve, amit a későbbiekben meg szeretnénk hívni.
3. `print("Helló!")`: Ez az a sor, ami lefut, amikor meghívjuk a függvényt. A `print` csak egy utasítás, ami megjeleníti a szöveget.

Most, hogy megvan a függvényünk, bármikor hívhatjuk így:

```python
koszones()
```

Ha ezt lefuttatjuk, akkor megjelenik a szöveg: `Helló!`.

---

### Függvény paraméterekkel

A paraméterek azok a dolgok, amiket a függvény "felhasználhat" a működéséhez. Gondolj rá úgy, mint egy csavarkulcsra: a kulcs működik minden csavarra, de a különböző méretekhez paraméterek kellenek. Például, ha azt szeretnénk, hogy a `koszones` függvény valakinek név szerint köszönjön, akkor ezt így oldhatjuk meg:

```python
def koszones(nev):
    print("Helló, " + nev + "!")
```

Most létrehoztunk egy `nev` nevű paramétert. Amikor meghívjuk a függvényt, ezt a paramétert ki kell töltenünk:

```python
koszones("Anna")
```

A végeredmény ez lesz: `Helló, Anna!`

#### Mi történt itt?
Amikor meghívtuk a `koszones("Anna")` függvényt, a Python tudta, hogy a `nev` értéke most „Anna”, így azt helyettesítette be a `print` utasításban. Ezt hívják "argumentumnak" is – így nevezzük azokat az értékeket, amiket a függvény hívásakor adunk meg.

---

### Több paraméter használata

Ha több információt szeretnénk átadni a függvénynek, azt is megtehetjük. Például egy `bemutatkozas` függvényt, amely név mellett kort is megjelenít:

```python
def bemutatkozas(nev, kor):
    print("Helló, " + nev + "! Te " + str(kor) + " éves vagy.")
```

Most két paramétert adtunk meg: `nev` és `kor`. Amikor meghívjuk a függvényt, mindkét értéket meg kell adnunk:

```python
bemutatkozas("Anna", 25)
```

A végeredmény: `Helló, Anna! Te 25 éves vagy.`

---

### Függvény, ami visszatér egy értékkel

Néha szükség lehet arra, hogy a függvény ne csak valamit megjelenítsen, hanem egy konkrét értéket adjon vissza. Ehhez a `return` kulcsszót használjuk.

Tegyük fel, hogy szeretnénk egy függvényt, ami két számot összead, és az eredményt visszaadja:

```python
def osszeadas(a, b):
    return a + b
```

A `return` utasítás itt az `a + b` értékét adja vissza. Ez azt jelenti, hogy amikor meghívjuk ezt a függvényt, kapunk egy konkrét eredményt:

```python
eredmeny = osszeadas(5, 3)
print(eredmeny)
```

Ez megjeleníti a `8`-at, mert az `osszeadas(5, 3)` értéke `8`.

#### Mi történik itt?
Amikor meghívjuk az `osszeadas(5, 3)` függvényt, az `a` értéke `5`, a `b` értéke `3`, és a függvény ezt a két számot összeadja. A `return` miatt a függvény visszaadja ezt az eredményt, amit a `eredmeny` nevű változóba mentettünk, és így ki tudjuk írni az eredményt a `print` segítségével.

---

### Függvények összefoglalása

1. **Létrehozás**: A függvényeket a `def` kulcsszóval hozzuk létre, és egy nevet adunk nekik.
2. **Meghívás**: A függvény nevét beírva hívjuk meg őket, zárójelek között megadva a szükséges paramétereket.
3. **Paraméterek**: Lehetőségünk van értékeket átadni a függvénynek, hogy azokkal dolgozzon.
4. **Return**: Ha azt szeretnénk, hogy a függvény eredményt adjon vissza, a `return` utasítással adjuk meg az eredményt.

---

### Gyakorlat: Függvény létrehozása és hívása

1. Készíts egy `ketszeres` nevű függvényt, amely egy számot fogad, és visszaadja annak kétszeresét.
2. Hívd meg a függvényt egy számmal, és írd ki az eredményt.

#### Megoldás

```python
def ketszeres(szam):
    return szam * 2

eredmeny = ketszeres(4)
print(eredmeny)
```

Eredmény: `8`

---


