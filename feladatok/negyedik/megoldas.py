
def etel_ara(etel):
    # Az étel típusától függően adja vissza annak az árát
    if etel == "leves":
        return 1200
    elif etel == "foetel":
        return 2500
    elif etel == "desszert":
        return 800

def felszolg_dij(alap_ar):
    # A felszolgálási díj az alap ár 10%-a
    return alap_ar * 0.1

def szamla(etel):
    # Elsőként kiszámítjuk az étel alap árát a `etel_ara` függvény segítségével
    alap_ar = etel_ara(etel)
    # Ezután kiszámítjuk a felszolgálási díjat a `felszolg_dij` függvény meghívásával
    dij = felszolg_dij(alap_ar)
    # Végül visszaadjuk az étel árát és a felszolgálási díjat összegyűjtve
    return alap_ar + dij

# Példa függvényhívás
vegosszeg = szamla("foetel")
print(f"A végső számla összesen: {vegosszeg} Ft")
