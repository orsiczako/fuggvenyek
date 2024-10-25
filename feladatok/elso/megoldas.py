def menu():
    # Kezdetben valasz üres értéket kap, hogy a while ciklus tudjon elindulni.
    valasz = ""
    
    while valasz != "kilépés":  
        # A ciklus addig fut, amíg a felhasználó nem írja be, hogy "kilépés".
        valasz = input('Mit szeretnél rendelni? (kilépés - kilépés)\n')
        # Megkérdezzük a felhasználót, hogy mit szeretne rendelni.

        if valasz == 'leves':  
            # Ha a felhasználó "leves"-t ír be, kiírjuk ezt az üzenetet.
            print('A leves a konyhán készül.')

        elif valasz == 'főétel':  
            # Ha "főétel"-t választ, kiírjuk az üzenetet a főételről.
            print('A főétel a séf specialitása.')

        elif valasz == 'desszert':  
            # Ha "desszert"-et választ, kiírjuk az üzenetet a desszertről.
            print('A desszert a cukrászdában készül.')

        elif valasz != "kilépés":
            # Ha valami más szöveget ír be, mint a lehetséges választások, hibaüzenet jelenik meg.
            print('Érvénytelen választás, kérlek válassz újra!')
            
    print('Kilépés a programból...')
    # A ciklus véget ért, ezért megjelenik a kilépési üzenet.
    
# A menü indítása
menu()

