def sportklub():
    # Ez a függvény a sportklub programját szimulálja.

    while True:  # Végtelen ciklus, ami addig fut, amíg a felhasználó be nem írja a "kilépés" szót.
        valasztas = input('Mit szeretnél csinálni? (kilépés - kilépés)\n')
        # Kérjük a felhasználót, hogy válasszon az edzés, verseny vagy konditerem közül.

        if valasztas == 'kilépés':
            # Ha a felhasználó a "kilépés" szót írja be, a program kilép.
            print('Kilépés a programból...')
            break  # Megszakítjuk a ciklust és a program véget ér.

        elif valasztas == 'edzés':
            # Ha a felhasználó "edzés"-t választ, megjelenik az üzenet az edzésről.
            print('Az edzés 16:00-kor kezdődik a sportpályán.')

        elif valasztas == 'verseny
