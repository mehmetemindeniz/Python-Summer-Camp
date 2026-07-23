#RANDOM
#random sayı üretmek için doğrudan kullanabileceğimiz fonksiyon yoktur .
#yerleşik bir modül üretmişlerdir kütüphaneyi import etmemiz gerekir .
#import random

#random.seed() fonksiyonu, rastgele sayı üreticisinin başlangıç noktasını (tohumunu) belirler. Bu sayede aynı rastgele sayı dizisini tekrar tekrar üretebilirim.
#Seed kullanılmazsa her program çalıştığında farklı sayılar üretilir.


#neden kullanılır ?
#Test yaparken aynı sonuçları tekrar elde etmek.
#Yapay zeka veya makine öğrenmesi deneylerini tekrar edebilmek.
#Oyun geliştirirken aynı haritayı veya olayları yeniden oluşturabilmek.
#Derslerde herkesin aynı rastgele sayıları üretmesini sağlamak.

#seed i başlangıç anahtarı gibi düşünebiliriz . seed(5)-->A yolu , seed(10)-->B yolu , seed(100)-->C yolu gibi


import random

random.seed(10)

durum = random.getstate()   # O anki durumu kaydet

print(random.randint(1, 100))
print(random.randint(1, 100))

random.setstate(durum)      # Kaydedilen duruma geri dön

print(random.randint(1, 100))
print(random.randint(1, 100))

#çıktı-->  74  5  74  5


#random.getstate(), rastgele sayı üretecinin mevcut durumunu kaydeder.
# Daha sonra random.setstate() ile bu durum geri yüklenebilir ve rastgele sayı üretimi kaldığı yerden aynı şekilde devam eder.
#getstate() kendinden sonraki durumu kaydediyor.
#---------------------------------------------

#random.randint() fonksiyonu, belirtilen iki sayı arasında (uçlar dahil) rastgele bir tam sayı üretir.
#Kullanımı
#import random
#random.randint(alt_sınır, üst_sınır)
#alt_sınır → En küçük sayı
#üst_sınır → En büyük sayı

#Her iki sayı da dahil edilir.örneğin radom.randint(1,3) --> 1,2,3 sayılarından birisini getirir.

#choice metodu ile liste(ya da herhangi bir veri türü(string,tuple...)) içinden rstgele bir elemanı getirebiliriz.
#örnek:

#import random

#renkListe=["kırmızı","pembe","beyaz","mavi"]
#print(random.choice(renkListe))

#ya da başka bir veri türlerinin içindekileri de rastegele alabilirim.örnek:
#import random
#text="python"
#print(random.choice(text)) ----python kelimesinin harflerinden rastgele seçecektir.


#random.shuffle() fonksiyonu, bir listenin elemanlarını rastgele karıştırır.
#Önemli: shuffle() sadece liste (list) üzerinde çalışır ve yeni bir liste oluşturmaz, mevcut listeyi değiştirir.
#programı her çalıltırdıpımızda farklı bir sıra görebiliriz.

#random.sample(myList,k=2)--2. parametre kadar içerisinden veri getirir,listenin içindeki veri sayısından fazla bir sayı girersek hata veriri


#örnekler:
#----------

#rastgele öğrenci seçme
import random

ogrenciler = ["Ali", "Ayşe", "Mehmet", "Zeynep"]

kazanan = random.choice(ogrenciler)

print("Seçilen öğrenci:", kazanan)

#---------

#şifre oluşturma
import random

karakterler = "ABCDEF123456"

sifre = ""

for i in range(6):
    sifre += random.choice(karakterler)

print(sifre)

#----------

#listeden rastgele eleman seçme 
import random

renkler = ["Kırmızı", "Mavi", "Yeşil", "Sarı"]

print(random.choice(renkler))