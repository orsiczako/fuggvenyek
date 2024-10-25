def erdeklodes():
    # Ez a függvény a főmenü, ami megkérdezi a felhasználót, mi érdekli.
    # A függvény addig fut, amíg a felhasználó be nem írja a "stop" szót.
    
    valasz = input('Mi érdekel téged? (stop - kilépés)')  
    # Itt a felhasználótól kérünk egy bemenetet, amit a "valasz" változó tárol.
    # A felhasználó írhat be bármit, de a lehetséges válaszok: "stop", "gyakorlat" vagy "előadás".
    
    if valasz == 'stop':  
        # Ha a felhasználó a "stop" szót írja be, a program megáll.
        # A "return" utasítással kilép a függvényből, így véget ér a program futása.
        return  # Kilépés a függvényből, itt a program befejeződik.
    
    elif valasz == 'gyakorlat':  
        # Ha a felhasználó a "gyakorlat" szót írja be, akkor a gyakorlat függvény fog meghívódni.
        gyakorlat()  # Meghívjuk a "gyakorlat" nevű függvényt, ami információt ad a gyakorlatról.
    
    elif valasz == 'előadás':  
        # Ha a felhasználó az "előadás" szót adja meg, akkor az előadás függvény fog meghívódni.
        eloadas()  # Meghívjuk az "eloadas" nevű függvényt, ami információt ad az előadásról.

def eloadas():
    # Ez a függvény felelős az előadás helyének megjelenítéséért.
    # Ha a felhasználó "előadás"-t választott, akkor itt kap információt.
    
    print('Az előadás a 29-es előadóteremben van.')
    # A "print" függvény kiírja az üzenetet a képernyőre, ami megmondja, hol van az előadás.
    
    erdeklodes()  
    # Miután az üzenet kiírásra került, újra visszatérünk a főmenübe, 
    # hogy a felhasználó újra választhasson, mi érdekli.
    
def gyakorlat():
    # Ez a függvény ad információt a gyakorlat helyszínéről.
    # Ha a felhasználó a "gyakorlat" szót választotta, akkor itt kap erről információt.
    
    print('A gyakorlat a 403-mas teremben van.')
    # A "print" függvény kiírja az üzenetet, ami megmondja, hol van a gyakorlat.
    
    erdeklodes()  
    # Miután az üzenet megjelent, visszatérünk a főmenübe, hogy a felhasználó újra választhasson.

erdeklodes()  
# Ez a program indításakor meghívja az "erdeklodes" függvényt, ami a főmenü.
# Ez biztosítja, hogy a felhasználó azonnal választhat, mi érdekli.
