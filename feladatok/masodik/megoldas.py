
def jegyvasarlas():
    # Ez a függvény a jegyvásárlási folyamatot szimulálja.

    while True:  # Végtelen ciklus, ami addig tart, amíg a felhasználó a "kilépés" szót nem adja meg.
        jegytipus = input('Milyen jegyet szeretnél venni? (kilépés - kilépés)\n')
        # Kérjük a felhasználót, hogy válasszon a jegytípusok közül.

        if jegytipus == 'kilépés':
            # Ha a felhasználó a "kilépés" szót írja be, a program véget ér.
            print('Kilépés a programból...')
            break  # Kilépünk a ciklusból, és befejezzük a programot.

        elif jegytipus == 'gyerek':
            # Ha a felhasználó "gyerek" jegyet választ, kiírjuk a gyerekjegy árát.
            print('A gyerekjegy ára: 1000 Ft.')

        elif jegytipus == 'felnőtt':
            # Ha a felhasználó "felnőtt" jegyet választ, kiírjuk a felnőttjegy árát.
            print('A felnőttjegy ára: 1500 Ft.')

        elif jegytipus == 'nyugdíjas':
            # Ha a felhasználó "nyugdíjas" jegyet választ, kiírjuk a nyugdíjas jegy árát.
            print('A nyugdíjas jegy ára: 1200 Ft.')

        else:
            # Ha a felhasználó érvénytelen jegytípust választ, tájékoztatjuk, hogy próbálja újra.
            print('Érvénytelen választás, kérlek válassz egy érvényes jegytípust!')
            
# Jegyvásárlási folyamat indítása
jegyvasarlas()
