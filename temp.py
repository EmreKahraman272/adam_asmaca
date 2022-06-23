import random
kelime = ("elma")
kelime1 = list(kelime)
harf = "e"
cizgi = len(kelime1) * "_"
l_cizgi = list(cizgi)

print(*l_cizgi)
yer = kelime1.index(harf)
l_cizgi[yer] = harf
print(*l_cizgi)
