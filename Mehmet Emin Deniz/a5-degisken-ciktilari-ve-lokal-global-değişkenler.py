# çıktı almak için print fonksiyonunu kullanırız
# fonksiyon çağırma => fonksiyon_adi( parametre )

# birden fazla değişken çıktılama
x = "Python"
y = "harika"
z = "bir"
t = "dil"
print(x,y,z,t)

# + da kullanabiliriz değişkenler arasındaü
print(x+y+z+t)
# fakat + ile ayırırsak aralarına boşluk koymaz
# virgül ile ayırdığımızda koyuyor

# + operatörü matematiksel bir operatördür de 
# integer değerleri toplar
sayi1 = 10
sayi2 = 20
print(sayi1 + sayi2)

# metinsel bir ifadeyle sayısal bir değşkeni birleştirmek için 
# + kullanırsak hata verecektir.
# farklı türde verileri print ile çıktı almak istiyorsak virgül kullanmamız lazım.

# ------------------------------------------------------

# Global Değişkenler
# hem fonksiyon içinde hem dışında her yerde kullanılabilir ve tanımlıdır.

text = "denemeler" # fonksiyonun dışındaki bir değişken tanımı.
# her yerde tanımlı kullanılabilir.

def benimFonksiyonum(): # fonksiyonu tanımlama
    print("getirilecek yazı fonksiyon içi:" + text)
benimFonksiyonum() # fonksiyonu çağırma 
# print("getirilecek yazı fonksiyon dışı:" + text)

# fonksiyon içinde aynı isimde bir değişken tanımlarsak;
# bu değişken lokal olur ve yalnızca fonksiyon içinde geçerlidir

# isim = 'emin'
# def yas_yazdır():
#     isim = "putin" #  lokal değişken
#     print(isim) # lokal değeri : putin'i yazdırır
# yas_yazdır()  
# print(isim) # global değişkendir, global değeri getirir : emin'i yazdırır.

# ---------------------------------------------------------

# fonksiyon içinde global tanımlama:
# fonksiyon içined bir değer tanımlandığında lokal olur
# ram, fonksiyon dışına çıkılıdğında bu değeri hafızasından siler
# fonksiyon içinde global tanımlamak içim global kullanmak gerekir

def yazdir_fonk():
    fooz = 10
    print(fooz)
# print(fooz) bu tanımsız olur hata verir

def yazdir_fonk2():
    global fooz2
    fooz2 = 20
    print(fooz2)
print(fooz2) # başında global var tanımldırı yukarda

# global bir değişkeni fonksiyon içinde değerini değiştirmek istiyorsak
# yine başına global ekleriz

# -----------------------------------------------------------

# değişken kullanmamızın nedenlerinden birisi programın bir hafızasının olmamasıdır.
# değişkenler değişen değerli veriler için uygundur kilo, not, süre gibi mesela
# değişkene kendisi + - li şekilde işlem yapıabilir

barx = 20
barx = barx + 20

# python da ve diğer yazılım dillerinde derleyici işlemleri sağdan sola doğru okuyarak gerçekleştirir
# önce barx + 20 işlenir
# sonra = barx işlenir
 