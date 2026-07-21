# stringler metinsel değerleri temsil ederler.
# python'da stringler tek tırnak veya çift tırnak içerisinde gösterilirler.
print("merhaba", 'python')

# çift tırnak içerisinde tek tırnak kullanabiliriz.
print("Bunu Emin'e ver")

# fakat çift tırnağın içinde çift tırnak veya
# tek tırnağın içinde tek tırnak kullanamayız.
# bunu yapabilmek için \ - backspace - esspace - kaçış karakteri kullanmamız gerekir.

print("Bunu kesinlikle \"yarın\" getirmelisin") # vurgu için olan tırnak içindekileri
# backspace ile yazdık. 

# bunun sebebi programın derlenirken bir tırnak gördüğünde bu tırnağın bitimi olarak 
# gördüğü ikinci ilk tırnağı alıyor olmasında aynı C'deki gibi mantığı.

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

# stringler birer array / dizidir.
# aslında stringler birer karakter dizisidir.
# python ===> {'p','y','t','h',o','n'} şeklindedir.