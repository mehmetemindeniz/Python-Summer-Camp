# choice() --> seçim / seçmek anlamına gelir
# verilen seriden rastgele bir öğe döndürür 
# bu bir string, list, tuple, range vs. olabilir 

import random

renkler = ["beyaz","kırmızı","mavi","sarı","lacivert","pembe","yeşil"]
# hangi renk olsun :)
print("Duvarlar", random.choice(renkler), "olsun :)")

text = "python"
print(random.choice(text)) # string içindeki harflerden birini rastgele seçer 
print(random.choice(text)) # string içindeki harflerden birini rastgele seçer 
print(random.choice(text)) # string içindeki harflerden birini rastgele seçer 

# choices ==> seçilen listeden rastgele bir liste döndürür
# 3 parametre alır birincisi hangi listeden alacağını 
# ikincisi weights yani ağırlık değerlerini alır
# üçüncüsü ise kaç elemanlık bir liste getireceğini söyler.

isimler = ["emin", "mehmet", "deniz", "ali", "veli"]
print(random.choices(isimler, k=5)) 

# --------------------------------------------------------

# shuffle() bir seriyi alır rastgele bir sırayla döndürür

rakamlar = [1,2,3,4,5,6,7,8,9,0]
print(rakamlar) # sıralı olarak yazdırır
random.shuffle(rakamlar) # karma olarak yeniden sıraladı
print(rakamlar) # en son halini yazdırdı 
# orjinal seri değişir

# --------------------------------------------------------

# sample() ==> bir seriden belirli sayıda öğeden oluşan rastgele bir liste döndürür
# sample() orjinal seriyi değiştirmez shuffle() değiştiriyordu

# ör elimizde bir grup öğrenci olsun ve hangi öğrencilerin sıralarda yan yana oturacağını
# sample kullanarak belirleyelim bunu 
ogrenci_listesi = ["emin", "mehmet", "deniz", "putin"]
yan_yana_oturacaklar = random.sample(ogrenci_listesi, k=2)
print(yan_yana_oturacaklar[0], "ve", yan_yana_oturacaklar[1], "yan yana oturacaklar.")

# --------------------------------------------------------

# random.random() modülü 0 ile 1 arasında rastgele bir sayı üretir
print(random.random())
print(random.random())
print(random.random())

# ---------------------------------------------------------

# uniform() ===> verilen 2 parametre arasında rastgele ondalıklı bir sayı döndürür
print(random.uniform(20,30))
print(random.uniform(1,2))
print(random.uniform(10,100))

# ----------------------------------------------------------

# triangular() ===> ingilizcede üçgen anlamına gelir 
# uniform gibi verilen 2 parametre arasında rastgele ondalıklı bir sayı döndürür
# fakat 3 bir parametre vererek üretilen sayının nereye daha yakın olabileceğini de belirtebiliriz.

print(random.triangular,(10,100,99)) # 99'a daha yakın bir sayı üretecektir 
# yığılma yerini değiştirebiliriz bu şekilde 

# -----------------------------------------------------------