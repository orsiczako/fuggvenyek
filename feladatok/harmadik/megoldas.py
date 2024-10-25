def sportklub():
    # A valasz változó kezdetben üres, hogy elindulhasson a ciklus.
    valasz = ""
    
    while valasz != "kilépés":  
        # A ciklus addig fut, amíg a felhasználó nem írja be, hogy "kilépés".
        valasz = input('Mit szeretnél csinálni? (kilépés - kilépés)\n')
        # Megkérdezzük, hogy mit szeretne csinálni a sportklubban.

        if valasz == 'edzés':  
            # Ha "edzés"-t választ, kiírjuk az edzéssel kapcsolatos információkat.
            print('Az edzés 16:00-kor kezdődik a sportpályán.')

        elif valasz == 'verseny':  
            # Ha "verseny"-t választ, kiírjuk a verseny időpontját és helyszínét.
            print('A verseny 14:00-kor kezdődik a stadionban.')

        elif valasz == 'konditerem':  
            # Ha "konditerem"-et választ, kiírjuk az erre vonatkozó információkat.
            print('A konditerem egész nap nyitva van.')

        elif valasz != "kilépés":  
            # Ha nem érvényes választ ad, hibaüzenet jelenik meg.
            print('Érvénytelen választás, kérlek válassz egy érvényes lehetőséget!')
            
    print('Kilépés a programból...')
    # A ciklus véget ért, ezért megjelenik a kilépési üzenet.
    
# Sportklub program indítása
sportklub()
