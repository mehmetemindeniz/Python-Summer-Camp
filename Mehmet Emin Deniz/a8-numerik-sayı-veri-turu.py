# int : tamsayı
# float : ondalıklı sayı
# complex : karmaşık sayı

x = 7 # int
y = 19.57 # float
z = 2j # complex
# print("int:", x, "float:", y, "complex:", z)
# \n ile alt alta yazdırabiliriz
print("int:", x, "\nfloat:", y, "\ncomplex:", z)

# float ile E ile üstel gösterim
# 19E4 bu 19 x 10*4 demektir
f = 19E4
print(f) # float türünde çıktı verir

a = 5 + 5j
b = 7j
c = 3 + 7j
print("a:", a, "b:", b, "c:", c)
# not: karmaşık sayılar farklı sayı türlerine dönüştürülemezler
# normal sayılar complekse dönüşebilir
Q = complex(7)
print(Q) # hata vermeyecekti

# ------------------------------------------------------

# yarı çapı verilen dairenin alan ve çevresini bulan program:

# dışardan veri almak için => input() fonksiyonunu kullanırız
yari_cap = float(input("Dairenin Yarıçapını Giriniz:"))
# ÇOK ÖNEMLİ BİLGİ !!!
# input fonksiyonu dışardan string türünde veri okur
# yani klayeden girdiğimiz bir şeyi integer olarak değil string olarak alır
# biz bu dışardan alınan değeri bir işlemde kullanacaksak eğer
# öncesinde bu değeri sayısal bir değer dönüştürme convert / type casting işlemi yapmamız gerekir.

pi_sayisi = 3.14

# alan formulü : pi x r*2
# daire çevre formulü : pi x r x 2

alan = pi_sayisi * yari_cap * yari_cap
cevre = pi_sayisi * yari_cap * 2

print("Dairenin Çevres:", cevre, "\nDairenin Alanı:", alan)

# --------------------------------------------------------

# dışardan girilen iki sayının toplamını veren program:

sayi1 = int(input("1. sayıyı giriniz:"))
sayi2 = int(input("2. sayıyı giriniz:"))
toplam = sayi1 + sayi2
print("\n\nSayıların Toplamı:", toplam)

# ---------------------------------------------------------

# metinsel bir ifadeyi integer türüne çevirebiliriz

ilk_asal_sayi = int("2")
print(ilk_asal_sayi)
print(type(ilk_asal_sayi))

# sayı olması koşuluyla!!!
# ilk_asal_sayi = int("python") gibi bir şey yapamayız