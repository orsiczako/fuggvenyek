# fuggvenyek

#### Miért használjunk függvényeket?

1. **Újrahasznosítható kód**: Ha egy feladatot többször kell végrehajtani a kódban, nem kell minden alkalommal újraírni a kódot. Elég létrehozni egy függvényt, majd meghívni azt.
2. **Olvashatóság és átláthatóság**: A függvények segítenek a programod tisztábbá tételében, mivel a kód részekre bontható, ami megkönnyíti az olvasást és a karbantartást.
3. **Modularitás**: Könnyebb módosítani vagy hibát keresni egy kisebb függvényben, mint az egész programban egyszerre.

#### Hogyan működik egy függvény?

Egy függvény Pythonban a következőképpen épül fel:

1. **Definiálás**: Meghatározzuk a függvényt.
2. **Meghívás**: A függvényt "meghívjuk" (azaz futtatjuk), amikor szükség van rá.

##### 1. Függvény definiálása

A függvények definiálása a `def` kulcsszóval történik, majd a függvény neve következik, és zárójelek közé írhatjuk a bemeneti paramétereket. Például:

```python
def koszones():
    print("Helló, üdvözöllek!")
```

- **`def`**: Ezzel kezdünk minden függvényt.
- **`koszones`**: Ez a függvény neve. Ezt fogjuk meghívni később.
- **`print("Helló, üdvözöllek!")`**: Ez az a kódrészlet, amit a függvény végrehajt.

##### 2. Függvény meghívása

Most, hogy létrehoztuk a `koszones()` függvényt, meg is tudjuk hívni:

```python
koszones()
```

Amikor meghívjuk a függvényt, a kimenet a következő lesz:

```
Helló, üdvözöllek!
```

Ez ennyire egyszerű: létrehoztunk egy függvényt, ami egy adott feladatot hajt végre, majd meghívtuk.

#### Függvények paraméterekkel

A függvények feladata gyakran változhat attól függően, hogy milyen adatokat adunk nekik. Ezért létrehozhatunk olyan függvényeket, amelyek **paramétereket** fogadnak. Nézzünk egy példát, ahol a `koszones()` függvény most már egy nevet is fogad:

```python
def koszones(nev):
    print(f"Hello, {nev}!")
```

Most már egy nevet is átadhatunk a függvénynek:

```python
koszones("Anna")
koszones("Péter")
```

A kimenet:

```
Hello, Anna!
Hello, Péter!
```

##### Hogyan működik?

- A **`nev`** paraméter egy változó, ami a függvény belsejében kap értéket. A függvény most nem csak egy általános üdvözlést ír ki, hanem személyre szabottan üdvözöl mindenkit a megadott név alapján.

#### Visszatérési érték (return)

A függvények nemcsak végrehajtanak valamit, hanem vissza is adhatnak egy értéket, amelyet máshol a kódban használhatunk. Ehhez a **`return`** kulcsszót használjuk. Például egy függvény, amely két szám összegét adja vissza:

```python
def osszead(a, b):
    return a + b
```

A függvény meghívása:

```python
eredmeny = osszead(5, 3)
print(eredmeny)
```

Kimenet:

```
8
```

##### Hogyan működik?

- **`return a + b`**: Ez a sor visszaadja az `a` és `b` összeadásának eredményét. A függvény visszatérési értékét elmenthetjük egy változóba (például `eredmeny`), majd felhasználhatjuk a programban.

#### Alapértelmezett értékek

Néha olyan függvényeket szeretnénk, amelyeknek van alapértelmezett értéke, ha a felhasználó nem ad meg egy paramétert. Például:

```python
def koszones(nev="Vendég"):
    print(f"Hello, {nev}!")
```

Most ha nem adunk meg nevet, a függvény automatikusan a "Vendég" szót fogja használni:

```python
koszones()       # Alapértelmezett értékkel hívjuk meg
koszones("Ákos") # Átadjuk a nevet
```

Kimenet:

```
Hello, Vendég!
Hello, Ákos!
```

#### Függvények több visszatérési értékkel

Egy függvény egyszerre több értéket is vissza tud adni, például egy négyzet és egy köb kiszámításánál:

```python
def hatvanyok(szam):
    negyzet = szam ** 2
    kob = szam ** 3
    return negyzet, kob
```

A függvény meghívása:

```python
n, k = hatvanyok(3)
print(f"Négyzet: {n}, Köb: {k}")
```

Kimenet:

```
Négyzet: 9, Köb: 27
```

##### Hogyan működik?

- A függvény két értéket ad vissza: a négyzetet és a köböt. A visszatérési értékeket külön változókba menthetjük.

#### Összefoglalás

A függvények az alábbiak szerint működnek Pythonban:
1. **Definiáljuk a függvényt** a `def` kulcsszóval.
2. **Meghívjuk a függvényt** a nevével és zárójelben a paramétereivel.
3. A függvények fogadhatnak **paramétereket**, amiket a zárójelekben adunk meg.
4. A függvények **visszaadhatnak** értéket a `return` kulcsszó segítségével.
5. Paraméterekhez adhatunk **alapértelmezett értékeket**, ha a függvényt paraméterek nélkül hívjuk meg.

#### Példa feladat

Íme egy egyszerű feladat, hogy gyakorold a függvények használatát. Írj egy függvényt, ami visszaadja egy szám négyzetét!

```python
def negyzet(szam):
    return szam ** 2

# Teszteljük a függvényt
eredmeny = negyzet(4)
print(f"A szám négyzete: {eredmeny}")
```

Kimenet:

```
A szám négyzete: 16
```

Most már tisztán látod, hogyan működnek a függvények Pythonban! További gyakorlatként próbáld ki, hogy írsz olyan függvényeket, amelyek több műveletet végeznek, és különböző paraméterekkel dolgoznak!
