# Random Number = Rastgele Sayılar
# python'da rastgele sayı üreten bir fonksiyon yoktur
# random sayı üretebilmek için bir modülü dahil etmemiz gerekir
import random # random sayı üretebilmek için kullanılan modül / kütüphane 

# seed => rastgele sayı üretecinin başlatıcısı
# print(random.random) # random modülündeki random fonksiyonunu çağırdı rastgele bir sayı üretir 
# bu kullanımda başlangıç değeri olarak sistem saatini kullanır default olarak
# biz başlangıç değerini kendimiz vermek istiyorsak seed kullanmamız gerekiyor
random.seed(7)
print(random.random())
# seed yani sabit başlangıç değeri verirsek hep aynı sayıyı üretir
# fakat seed vermezsek bilgisayar başlangıç değeri olarak sistem saatini kullanır
# sistem saati ise sürekli değiştiği için çıktı değeri de değişecektir 

# getstate = mevcut durumu çeker
# setstate = seçilen durumu geri yükler

print(random.random()) # ===> 1
state = random.getstate() # şuan burdaki durumu kaydetti değişkene
print(random.random()) # ===> 2
random.setstate(state) # değişkene tutturduğumuz durumu setstate ile geri yükledik
print(random.random) # ===> 3
# 1. ile 3. aynı değerleri verir bizem 

# getrandbits() : rastgele bitleri temsil eden bir sayı döndürür 
# bu method belirtilen boyutta bit şeklinde olacak şekilde bir tam sayı döndürür
print(random.getrandbits(8)) # 8 bit boyutunda bir sayı üret 

# randrange() : verilen aralıkta rastgele bir sayı döndürür 
print(random.randrange(1,10)) # 1 ile 10 arasından rastgele bir sayı üretir 
# 1 dahildir başlangıç / 10 dahil değildir son

# randrange(x,y,z) 3. bir parametre vererek kaç adımda bir seçmesi gerektiğini de sağlayabiliriz
# randrange(0,11,2) 0'dan başla 2şer 2şer ilerle 10a kadar ==> 0,2,4,6,8,10 değerlerini alabilir

# --------------------------------------

# randint() -  randrange()'den farklı olarak bitiş parametresini de dahil eder
print(random.randint(0,10)) # 0'dan 10'a kadar sayılar üretir 10 da dahildir 