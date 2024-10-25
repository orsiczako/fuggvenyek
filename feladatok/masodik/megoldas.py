def jegyvasarlas():
    # Kezdeti érték a valasz változónak, hogy elindulhasson a ciklus.
    valasz = ""
    
    while valasz != "kilépés":  
        # A ciklus addig fut, amíg a felhasználó nem írja be, hogy "kilépés".
        valasz = input('Milyen jegyet szeretnél venni? (kilépés - kilépés)\n')
        # Megkérdezzük, milyen jegyet szeretne venni a felhasználó.

        if valasz == 'gyerek':  
            # Ha "gyerek"-jegyet választ, kiírjuk a gyerekjegy árát.
            print('A gyerekjegy ára: 1000 Ft.')

        elif valasz == 'felnőtt':  
            # Ha "felnőtt"-jegyet választ, kiírjuk a felnőttjegy árát.
            print('A felnőttjegy ára: 1500 Ft.')

        elif valasz == 'nyugdíjas':  
            # Ha "nyugdíjas"-jegyet választ, kiírjuk a nyugdíjas jegy árát.
            print('A nyugdíjas jegy ára: 1200 Ft.')

        elif valasz != "kilépés":  
            # Ha nem érvényes jegytípust ír be, hibaüzenet jelenik meg.
            print('Érvénytelen választás, kérlek válassz egy érvényes jegytípust!')
            
    print('Kilépés a programból...')
    # A ciklus véget ér, ezért megjelenik a kilépési üzenet.
    
# Jegyvásárlási folyamat indítása
jegyvasarlas()
