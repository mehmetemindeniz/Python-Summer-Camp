# kendi örneğimdir.
# soru: random modulü kullanarak bir zar atma oyunu yapın.
# iki kullanıcı için program her çalıştığında zarlar atılsın
# hangi kullanıcının zarındaki değer büyükse o kazanacak oyunu

import random

print("Zarlar atılıyor...\n")

oyuncu1 = random.randrange(1,7)
oyuncu2 = random.randrange(1,7)
print("Oyuncu1'in zarı:", oyuncu1)
print("Oyuncu2'in zarı:", oyuncu2)

if oyuncu1 > oyuncu2:
    print("\nKazanan **Oyuncu1**")
elif oyuncu2 > oyuncu1:
    print("\nKazanan **Oyuncu2**")
elif oyuncu1 == oyuncu2:
    print("\nDurum **Berabere**")
else:
    print("\n**Geçersiz Tur**")