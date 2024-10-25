
def menu():
    # Ez a függvény megkérdezi a felhasználót, mit szeretne rendelni.
    
    while True:  # Végtelen ciklus, ami addig tart, amíg a felhasználó a "kilépés" szót nem adja meg.
        valasz = input('Mit szeretnél rendelni? (kilépés - kilépés)\n')
        # Kérjük a felhasználót, hogy válasszon a megadott lehetőségek közül.

        if valasz == 'kilépés':  
            # Ha a felhasználó beírja a "kilépés" szót, a program befejeződik.
            print('Kilépés a programból...')
            break  # Kilépünk a while ciklusból, ezzel véget ér a program.

        elif valasz == 'leves':  
            # Ha a felhasználó a "leves" szót írja be, megjelenik egy üzenet a levesről.
            print('A leves a konyhán készül.')

        elif valasz == 'főétel':  
            # Ha a felhasználó a "főétel" szót választja, megjelenik egy üzenet a főételről.
            print('A főétel a séf specialitása.')

        elif valasz == 'desszert':  
            # Ha a felhasználó a "desszert" szót írja be, megjelenik egy üzenet a desszertről.
            print('A desszert a cukrászdában készül.')

        else:  
            # Ha a felhasználó olyan választ ad, ami nem szerepel a lehetőségek között:
            print('Érvénytelen választás, kérlek válassz újra!')
            # Tájékoztató üzenet, hogy a választás érvénytelen volt.
            
# A menü indítása
menu()
