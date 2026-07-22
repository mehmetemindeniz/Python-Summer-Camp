# stringler metinsel değerleri temsil ederler.
# python'da stringler tek tırnak veya çift tırnak içerisinde gösterilirler.
print("merhaba", 'python')

# ------------------------------------------------------

# çift tırnak içerisinde tek tırnak kullanabiliriz.
print("Bunu Emin'e ver")

# fakat çift tırnağın içinde çift tırnak veya
# tek tırnağın içinde tek tırnak kullanamayız.
# bunu yapabilmek için \ - backspace - esspace - kaçış karakteri kullanmamız gerekir.

print("Bunu kesinlikle \"yarın\" getirmelisin") # vurgu için olan tırnak içindekileri
# backspace ile yazdık. 

# bunun sebebi programın derlenirken bir tırnak gördüğünde bu tırnağın bitimi olarak 
# gördüğü ikinci ilk tırnağı alıyor olmasında aynı C'deki gibi mantığı.

# ------------------------------------------------------

text = "python" # değişkene string değer ataması

# çok satırlı bir stringi bir değişkene atama.
# daha önce üç tırnak arasına yazılanların değişkene atanmamış stringler olduğunu söylemiştik.
# bunları değişkenlere atayabiliriz.

metin = """
bu bir deneme
amaçlı metindir 
birden çok
satırı içerir
"""
print(metin)
# 3 çift tırnak içerisine yazabildiğimiz gibi 3 tek tırnak arasında da yazabiliriz.

# ------------------------------------------------------

# stringler birer array / dizidir.
# aslında stringler birer karakter dizisidir.
# python ===> {'p','y','t','h',o','n'} şeklindedir.
# diziler 0. indexten başlar. yani ilk karakterin indexi 0'dır.

arabalar = "mercedes, bmw, audi, toyota, honda"
print(arabalar[2]) 

# stringler de dizidir 
 
print(text[0]) # 0. indexteki karakteri verir.
print(text[1]) # 1. indexteki karakteri verir.

# ------------------------------------------------------

# stringler de döngü kullanımı

text2 = "Python Tuhaftır"
for x in text2:
    print(x)

# ------------------------------------------------------

# stringin uzunluğunu getirme len komutu.
# len komutu bir stringin uzunluğunu getirir

print(len(text2)) # 15 karakter uzunluğunda olduğunu gösterir. space'i de sayar

# ------------------------------------------------------

# string içersinde arama:
# belirli bir karakterin ya da ifadenin bir string içerisinde geçip geçmediği aramak için in kullanabiliriz.

text3 = "Hayattaki en iyi diller bedavadır."
print("bedava" in text3) # True döner çünkü bedava ifadesi text3 içerisinde geçiyor.
print("pahalı" in text3) # False döner çünkü pahalı ifadesi text3 içerisinde geçmiyor.
# in komutu ile arama yaparken büyük küçük harf duyarlılığı vardır. yani "bedava" ile "Bedava" farklıdır.
# in eğer aranan ifade varsa true yoksa false döndürür.
# bunu bir değişken ile de yapabilirdik
aranan_kelime = "bedava"
print(aranan_kelime in text3)

# in'li ifadeleri programlamada koşullar ile kullanarız.
# içinde şu varsa şu olsun şu yoksa bu olsun gibisinden.
if aranan_kelime in text3:
    print("aranan kelime bulundu")

# ------------------------------------------------------

# in gibi not in de kullanılabilir bu da içinde geçmeme durumunu kontrol eder.