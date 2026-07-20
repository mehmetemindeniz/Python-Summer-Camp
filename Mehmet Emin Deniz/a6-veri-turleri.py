# ==== veri türleri ===

# metin türünde : str
name = "mehmet"

# nümerik türünde : int, float, complex(karmaşık sayılar)
x = 10 # integer
y = 12.42 # flolat
comp = 2j # complex datalar

# metinsel ifade ile sayısal ifadeyi normalde print içinde + ile birleştirerek yazamayız.
# bunu yapmak için tür dönüşümü yapabiliriz sayısal ifadeleri print içinde
# str(V) şeklinde yazarak türünü değiştirebiliriz

sayi = 21
isim = "emin"
print("Öğrencinin Adı: " + isim + " " + "öğrencinin yaşı: " + str(sayi)) # sayi değişkenini str ile string olarak yazdırdık 

# type(değişken) fonksiyonu ile değişkenin türünü alabiliriz
print(type(x))
print(type(y))
print(type(comp))
print(type(isim))

# -----------------------------------------------------------

# Sequence Tipi : list, tuple, range

# listeler benzer türde birden çok veriyi çoklu olarka tutmak istersek kullanırız
# listeler köşeli parantezlerle tanımlanır.
# içindeki değerler değişkenler gibi değiştirilebilir
meyveler = ["elma", "armut", "muz", "çilek", "kayısı"]
renkler = ["beyaz", "kırmızı", "yeşil", "mavi", "sarı", "pembe"]
print(type(meyveler))

# tuple'lar list'lerden farklıdır
# normal parantezle tanımlanırlar
# içlerindeki değerler normal olarak değiştirilemezler
# değiştirmek için önce list() fonksiyonu ile listeye çevirmek gerekir.
personelTuple = ("emin", "ali", "ayşe", "murat", "kemal")
print(type(personelTuple))

# range ise bir aralık belirten dizilerdir
sayilarRange = range(7) # range veri türü 0'dan itibaren 0 dahil 7 sayı alır index = 0 y
print(type(sayilarRange))
print(sayilarRange) # bunun çıktısı range(0, 7) şeklinde olur
print(*sayilarRange) # bu yıldızlı ifade ile yazarsak elemanları da getirir = 0,1,2,3,4,5,6
# range'i döngülerde kullanabiliriz 

# mapping tipi : dict 
# anahtar değer çiftleri şeklinde verileri tutar 
# json formatı için kritik bir tür
personelBilgi = {"isim":"Emin", "yas":21}
print(personelBilgi)
print(type(personelBilgi))

# ----------------------------------------------------

# set tipi : set, frozenset
SetRenkler = {"beyaz", "kırmızı", "yeşil", "mavi", "sarı", "pembe"} # set data type
print(SetRenkler)
print(type(SetRenkler))

# set biraz esnektir frozenset ise katıdır değiştirme yapmaya izin vermez 
FrozenSetRenkler = frozenset({"beyaz", "kırmızı", "yeşil", "mavi", "sarı", "pembe"}) # set data type
print(FrozenSetRenkler)
print(type(FrozenSetRenkler))

# ----------------------------------------------------

# boolen veri türü
# true / false olmak üzere sadece iki değer alır 
# True  = 1
# False  = 0
DY = True
print(DY)
print(type(DY))

# -----------------------------------------------------

# none type : null 
# diğer dillerdeki null'a denk gelir \0
# veri yok demektir = null = boş
bos = None
print(bos)
print(type(bos))

# -----------------------------------------------------

# Binary Type : bytes, bytearray, memoryview
# bilgisayar sadece 0 ve 1 lerden anlar.
# bitler ile çalışır bitler bir araya gelerek byte'ları oluşturur.

# değişkenin ram'de ne kadar yer kapladığını anlamak için
# sys.getsizeof() fonksiyonu kullanılır
# sys. ile başlayan komutlar sistem fonksiyonlarıdır
# sys komutlarını kullanabilmek için sys kütüphanesini dahil etmemiz gerekir

import sys # ===> burası önemli !!!
# pythonda bir kütüphaneyi dahil ederken import komutunu kullanırız

print(sys.getsizeof(x))
print(sys.getsizeof(personelBilgi))

# bitsel işlemler yapacaksal üzerinde çalışacağımız değişkenler bytes tipinde olacaktır
ismim = b"emin" # başındaki b bunun binary şeklilde tutulacağını ifade eder 
print(type(ismim))
# python'da ikili verileri işlemek istediğimiz zaman kullanırız 
# metni kodlayıp kodunu çözmek
# dosya giriş çıkışını işlemek
# ağlar üzerinden iletişim kurmak 
# gibi yerlerde kullanılır

# bytes değişmez dizilerden oluşuyorken 
# bytes arrays nesnelerin değiştirilebilir olmasını sağlar 
# bytes = değiştirilemez katıo
# bytes = değiştirilebilir, daha esnek
# bytes ASCII karakterleri kabul eder
# yani şğü gibi Türkçe utf-8 formatındakileri yazdığımızda hata verecektir 
# bun çözmek için kullanım
ismim2 = bytes("şakir", "utf-8") # ş'yi hexadecimal değerde yazar
print(ismim2)

ismim3 = bytearray([65]) # ASCII değeri alıp çıktı olarak karşılık gelen karakteri verir
print(ismim3)

# memeoryview = bellek bloklarına doğrudan erişim imkanı sunan uygulama arayüzü sunar.
# programların bellek tüketimini izlemek ve optimize etmek için kullanılır
# memoryview programcılara bellek üzerinden veri manipülasyonu yapmak imkanı sunar.
# bu sayede python programları daha verimli çalıştırabilir 
# veri yapılarını işlerken kullanılır 
# verilere hızlıca erişmek ve bu veriler üzerinden işlemk yapmak gerektiği durumlarda kullanılır.
# bilimsel hesaplamalar, veri analizleri, medya işleme gibi alanlarda kullanılır 

foobar = memoryview(bytes(5))
print(type(foobar))
print(foobar)
# ram ile daha hızlı etkileşime girmeyi ve rami daha etkili kullanabilmeyi sağlar 
# C'deki pointer gibi düşünülebilir 
# veri manipülasyonları için kullanılır.