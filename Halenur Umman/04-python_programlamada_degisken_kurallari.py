---------- Programlamada Değişken Kuralları ----------
-----------------------------------------------------------

-- Değişken isimleri, harf (a-z, A-Z), rakam (0-9) ve alt çizgi (_) karakterlerinden oluşabilir.
-- Değişken isimleri, rakam ile başlayamaz.
- x = 5
- 1x = 5 # GEÇERSİZ değişken ismi
- _x = 5 # Geçerli değişken ismi
- age1 = 25 # Geçerli değişken ismi
- total_amount = 100.50 # Geçerli değişken ismi 
- my-variable = "Hello" # GEÇERSİZ değişken ismi

-- Değişkenlerde boşluk karakteri kullanılamaz. Bunun yerine alt çizgi (_) kullanılabilir.
- first name = "John" # GEÇERSİZ değişken ismi
 
 -- Değişken isimleri, Python'da kullanılan anahtar kelimelerle aynı olamaz. Anahtar kelimeler, Python'un kendisi tarafından kullanılan özel kelimelerdir ve değişken isimleri olarak kullanılamaz.
- if = 5 # GEÇERSİZ değişken ismi

-- Çok kelimeli değişken isimleri için belli başlı yazım kuralları vardır. 
   Örneğin; camelCase, PascalCase veya snake_case kullanılabilir.
- firstName = "John" # camelCase: İlk kelimenin ilk harfi küçük, sonraki kelimelerin ilk harfi büyük yazılır.
- FirstName = "John" # PascalCase: Tüm kelimelerin ilk harfi
- first_name = "John" # snake_case: Tüm kelimeler küçük harflerle yazılır ve kelimeler alt çizgi ile ayrılır.

-- Farklı değişkenleri aynı satırda tanımlamak için virgül (,) kullanılabilir.
- x, y, z = 1, 2, 3
  print(x) # Cevap: 1
  print(y) # Cevap: 2
  print(z) # Cevap: 3

-- Variable sayısı, değer sayısı ile eşleşmelidir. Aksi takdirde hata oluşur.
- x, y = 1, 2, 3 # HATA: Değişken sayısı ile değer sayısı eşleşmiyor.

-- Aynı değeri tek bir satırda birden fazla değişkene atamak için eşittir (=) operatörü kullanılabilir.
- x = y = z = 0
  print(x) # Cevap: 0
  print(y) # Cevap: 0
  print(z) # Cevap: 0

-- Bir variable''daki değeri başka bir variable''a atamak için eşittir (=) operatörü kullanılabilir.
- x = 5
- y = x # y değişkenine x değişkeninin değeri atanır
  print(y) # Cevap: 5

-- Bir liste içinde değerler dizini varsa python değerleri variable''lara atayabilir. Bu işleme "UNPACKING" denir.
- car = ["ford", "ferrari", "bmw"]
- x, y, z = car # car listesindeki değerler sırasıyla x, y ve z değişkenlerine atanır
  print(x) # Cevap: ford
  print(y) # Cevap: ferrari
  print(z) # Cevap: bmw