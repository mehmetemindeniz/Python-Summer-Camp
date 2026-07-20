# veri türünü mecburen belirtmemiz gereken yerler vardır.
# bu yüzden de tür dönüşümlerini yapmamız gereken yerler olabilir.
# veri türünü zorlayarak dönüştürürüz

x = str("Merhaba Dünya")
print(x)
print(type)

y = str(True) # true ifadesi artık boolen değil bir string olacak 
print(y)
print(type(y))

z = int(7.19) # zorla int yaptık
print(z)
print(type(z))

t = float(5)
print(t)
print(type(t))

DY1 = int(True)
print(DY1) # 1 yazdırır

DY2 = int(False)
print(DY2) # 0 yazdırır

# -------------------------------

# Karmaşık Sayılar = a + b.i / a + bj vs. real + imajiner

Q = complex(3,5)
print(Q)
print(type(Q))

# --------------------------------

marka = list(("skoda", "nissan", "volvo")) # listeye çevirir
print(marka)
print(type(marka))

# ---------------------------------

aralık = range(8)
print(aralık)
print(type(aralık))

# ---------------------------------

anahtarkilit = dict(isim = "Emin", yas = 21)
print(anahtarkilit)
print(type(anahtarkilit))

# ---------------------------------

test = bool(324829034)
print(test)
print(type(test))
# bool yapılarda 0 dışındaki her değer true'dur - 1'dir eksili olsa bile 