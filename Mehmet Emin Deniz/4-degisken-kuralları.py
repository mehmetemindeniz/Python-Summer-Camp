# uzun degisken isimleri tanımlarken alt çizgiler kullanabiliriz. 
# bunlar tanımlama/isimlendirme standartlarıdır.

isim_soyIsim = "Mehmet Emin DENİZ"
print(isim_soyIsim)

# değişken isimleri asla sayı ile başlayamaz.
# ya bir harf ile ya da alt çizgi ile başlayabilir
# 3isim diye bir şey tanımlamamıza izin vermez 
_yas = 21

# değişken isimleri harfler rakamlar ve altçizgi içerebilir diğer karakterleri içeremez.
# isim-soyisim = gibi bir kullanım olamaz

# değişken isimleri büyük küçük harfe duyarlıdır

# bir değişken ismi pythondaki komutlarla aynı olamaz
# aynı C deki gibi. çünkü bu kelimeler reserve kelimelerdir
# for, while, de, if, else gibi komutlar değişken ismi olarak kullanılamaz.

# --------------------------------------------------------

# Çoklu kelime içeren değişken isimleri için isimlendirme standartları: 

# Camel Case: ilk kelime haric her kelime büyük başlar => isimSoyisimYas
# Pascal Case: her kelim büyük harfle başlar => IsimSoyisimYas
# Snake Case: hepsi küçük yazılır alt çizgi ile ayrılır => isim_soyisim_yas 

# --------------------------------------------------------

# farklı değişkenlere tek satırda değer atamam

x,y,z = "Muz", "Elma", "Armut"
print(x)
print(y)
print(z)

# değişken sayısıyla değer sayısı aynı olmalı 

a=b=c="kırmızı"
print(a)
print(b)
print(c)
# böyle bir kullanım da mevcuttur 

# bir değişkenin değerini başka bir değişkene direk atayabiliriz
isim = "Mehmet Emin Deniz"
name = isim
print(name)

# -----------------------------------------------------------

# değişkenlere direk dizideki/listedeki değerleri boca edebiliriz

renkler = ["beyaz", "kırmızı", "mavi"]
b, k, m = renkler
print(b)
print(k)
print(m)
