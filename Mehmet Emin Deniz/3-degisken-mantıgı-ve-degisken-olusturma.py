# variable = değişken

# verileri tutmak için kullanılır.
# python da değişkenleri tanımlamak için tip belirtmemize gerek yoktur.
# yani int str vs. gibi
# bir değişkene değer atandığı anda pytyhon kendisi onun tipini algılar ve tanımlar.
# değişkenler verilerin ram'de adreslerde tutulmasını sağlar
# program çalışırken ram'deki bu verileri kullanır

x = 10 # int olduğunu kendi belirler
y = "Python" # string olduğunu kendi belirler

print(x)
print(y)

# değişkenlere değişken dememizin sebebi değerlerinin değişebilir olmasından ötürüdür
# x'in değerini değiştirelim
x = 15
print(x)

# ---------------------------------------------------------------

# python'da bir değişkene ilk atandığı tip dışında bir tip değeri ataması yapabilir miyiz?
# evet. 
foo = 10
print(foo)
foo = "Deneme"
print(foo)

# python'da ve programlamada değişkenlerde kullanılan eşittir matematiktekinden farklıdır
# burdaki eşittir bir "atama" operatörüdür.

# ----------------------------------------------------------------

# CASTİNG İşlemi = Veri tipi değiştirme işlemi.
bar = str(7) # burdaki bar değişkeni string olarak 7 değeri alır
foq = int(7) # burdaki foq değişkeni int olarak 7 değeri alır
baz = float(7) # burdaki baz değişkeni float olarak 7.0 değeri alır 
# ondalıklı sayılar float olarak ifade edilir.

print(bar)
print(foq)
print(baz)

# -----------------------------------------------------------------

# TYPE Fonksiyonu = Veri türünü getiren fonksiyondur
print(type(bar))
print(type(foq))
print(type(baz))

# ------------------------------------------------------------------

# metinsel ifadeler de çift veya tek tırnak kullanabiliriz.

# ------------------------------------------------------------------

# variable case sensitive = büyük küçük harfa duyarlılık
# python büyük küçük harfe duyarlıdır yani;
# foo değişkeni ile FOO değişkeni birbirinden farklıdır.
