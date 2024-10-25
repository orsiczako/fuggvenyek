### Mit fog kiírni egyes paraméterek átadásánál? A következő feladatoknál erre a kérdésre kellene válaszolni:

### 1. Feladat: „Kávézó rendelés”

Készítsünk egy `rendeles` nevű függvényt, amely fogadja a kávé típusát és a méretét paraméterként, majd a választott kávé és méret alapján kiírja a megfelelő árat.

```python
def rendeles(kave_tipus, meret):
    # Az árakat a kávé típus és a méret alapján állítjuk be.
    if kave_tipus == 'espresso':
        if meret == 'kicsi':
            ar = 500
        elif meret == 'nagy':
            ar = 700
    elif kave_tipus == 'latte':
        if meret == 'kicsi':
            ar = 600
        elif meret == 'nagy':
            ar = 800
    elif kave_tipus == 'capuccino':
        if meret == 'kicsi':
            ar = 550
        elif meret == 'nagy':
            ar = 750
    
    print(f"A választott {meret} {kave_tipus} ára: {ar} Ft")

# Különböző kávétípusokkal és méretekkel történő rendelés
rendeles("espresso", "kicsi")
rendeles("latte", "nagy")
rendeles("capuccino", "kicsi")
```

#### Magyarázat:
- **`kave_tipus` és `meret`**: ezek a paraméterek adják meg a kávé típusát és méretét.
- Minden kávétípushoz két különböző ár van beállítva a mérettől függően, és a függvény ezek alapján választja ki az árat.

---

### 2. Feladat: „Könyvtár”

Készítsünk egy `kolcsonzes` nevű függvényt, amely két paramétert fogad: a könyv típusát és a kölcsönzés időtartamát. A függvény ennek alapján kiszámolja és kiírja a kölcsönzés árát.

```python
def kolcsonzes(konyv_tipus, idotartam):
    # Az árak a könyv típusától és a kölcsönzés időtartamától függően változnak.
    if konyv_tipus == 'regeny':
        ar = 200 * idotartam
    elif konyv_tipus == 'ismeretterjeszto':
        ar = 300 * idotartam
    elif konyv_tipus == 'gyermek':
        ar = 150 * idotartam
    
    print(f"A(z) {konyv_tipus} típusú könyv kölcsönzési díja {idotartam} napra: {ar} Ft")
    
# A függvény meghívása különböző típusokkal és kölcsönzési időtartammal
kolcsonzes("regeny", 3)
kolcsonzes("ismeretterjeszto", 5)
kolcsonzes("gyermek", 7)
```

#### Magyarázat:
- **`konyv_tipus` és `idotartam`**: ezek a paraméterek adják meg a kölcsönözni kívánt könyv típusát és a kölcsönzési idő hosszát.
- Az ár a könyv típusától és az időtartamtól függ, amit a függvény az adott paraméterekkel kiszámol.

---

### 3. Feladat: „Mozi jegyrendelés”

Készítsünk egy `mozi_jegy` nevű függvényt, amely fogadja a jegy típusát (gyerek, felnőtt vagy nyugdíjas) és a vetítés időpontját (délután vagy este), majd ezek alapján kiírja a jegy árát.

```python
def mozi_jegy(jegy_tipus, idopont):
    # Az árak a jegy típusától és az időponttól függően változnak.
    if jegy_tipus == 'gyerek':
        if idopont == 'délután':
            ar = 800
        elif idopont == 'este':
            ar = 1000
    elif jegy_tipus == 'felnőtt':
        if idopont == 'délután':
            ar = 1200
        elif idopont == 'este':
            ar = 1500
    elif jegy_tipus == 'nyugdíjas':
        if idopont == 'délután':
            ar = 900
        elif idopont == 'este':
            ar = 1100
    
    print(f"A(z) {jegy_tipus} jegy ára {idopont} időpontban: {ar} Ft")

# A függvény meghívása különböző jegytípusokkal és időpontokkal
mozi_jegy("gyerek", "délután")
mozi_jegy("felnőtt", "este")
mozi_jegy("nyugdíjas", "délután")
```

#### Magyarázat:
- **`jegy_tipus` és `idopont`**: ezek a paraméterek adják meg a jegy típusát és a vetítés időpontját.
- Minden jegytípushoz más ár tartozik attól függően, hogy délutáni vagy esti vetítésre szól, és a függvény ez alapján állapítja meg a megfelelő árat.

---

### 4. Feladat: „Pizzarendelés”

Készítsünk egy `pizza_rendeles` nevű függvényt, amely három paramétert fogad: a pizza típusát (Margherita, Hawaii vagy Pepperoni), a méretet (kicsi, közepes vagy nagy) és a feltét számát. Ezek alapján kiszámítja és kiírja a rendelés végösszegét.

```python
def pizza_rendeles(pizza_tipus, meret, feltet_szam):
    # Alapárak a pizza típus és méret alapján.
    if pizza_tipus == 'Margherita':
        if meret == 'kicsi':
            alap_ar = 1000
        elif meret == 'kozepes':
            alap_ar = 1500
        elif meret == 'nagy':
            alap_ar = 2000
    elif pizza_tipus == 'Hawaii':
        if meret == 'kicsi':
            alap_ar = 1200
        elif meret == 'kozepes':
            alap_ar = 1700
        elif meret == 'nagy':
            alap_ar = 2200
    elif pizza_tipus == 'Pepperoni':
        if meret == 'kicsi':
            alap_ar = 1300
        elif meret == 'kozepes':
            alap_ar = 1800
        elif meret == 'nagy':
            alap_ar = 2300
    
    # A végösszeg kiszámítása a feltétek alapján (minden feltét +200 Ft).
    vegosszeg = alap_ar + (feltet_szam * 200)
    print(f"A {meret} {pizza_tipus} pizza {feltet_szam} extra feltéttel: {vegosszeg} Ft")

# A függvény meghívása különböző típusú pizzákkal, méretekkel és feltétszámokkal
pizza_rendeles("Margherita", "kicsi", 2)
pizza_rendeles("Hawaii", "nagy", 3)
pizza_rendeles("Pepperoni", "kozepes", 1)
```

#### Magyarázat:
- **`pizza_tipus`, `meret`, és `feltet_szam`**: ezek a paraméterek adják meg a rendelni kívánt pizza típusát, méretét és a hozzáadott feltétek számát.
- A pizza alapárát a típus és méret alapján választjuk ki. Ezután minden feltét 200 Ft-tal növeli a végösszeget, amit a `vegosszeg` változó tárol.

---

### 5. Feladat: „Edzésnapló”

Készítsünk egy `edzes` nevű függvényt, amely fogadja az edzés típusát (kardió, erősítés vagy jóga), a tartamát (percben), és a napi célokat. A függvény kiírja, hogy hány percet sikerült a célból teljesíteni.

```python
def edzes(edzes_tipus, tartam, cel):
    # Kiírjuk az edzés típusát és tartamát.
    print(f"{tartam} perc {edzes_tipus} edzést végeztél.")
    
    # Számítjuk a hátralévő időt a célig.
    teljesites = min(tartam, cel)
    print(f"Ebből {teljesites} perc teljesítette a napi {cel} perces célt.")

# A függvény meghívása különböző típusú edzésekkel, időtartamokkal és célokkal
edzes("kardió", 30, 60)
edzes("erősítés", 45, 40)
edzes("jóga", 50, 50)
