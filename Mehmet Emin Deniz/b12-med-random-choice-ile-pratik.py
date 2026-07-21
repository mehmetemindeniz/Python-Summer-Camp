# kendi örneğimdir
# random choice kullanarak basit bir oyun yapalım.
# bir renkler listemiz olsun içerisinde kırmızı, beyaz ve sarı olsun 
# random.choice ile bu listeden rastgele 2 renk seçilecek
# eğer seçilen renkler kırmızı beyaz ise Türk Bayrağı
# eğer seçilen renkler kırmızı sarı ise İspanya Bayrağı 
# çıktısını verecek program

import random

bayrak_renkleri = ["kırmızı", "beyaz", "sarı"]

renk1 = random.choice(bayrak_renkleri)
renk2 = random.choice(bayrak_renkleri)

if renk1 == "kırmızı":
    if renk2 == "beyaz":
        print("Türk Bayrağı")
    elif renk2 == "sarı":
        print("İspanya Bayrağı")
else:
    print("**Bilinmeyen Bayrak Renkleri**")