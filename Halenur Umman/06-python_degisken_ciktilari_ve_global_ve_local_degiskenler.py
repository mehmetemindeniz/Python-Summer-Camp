---------- Değişken Çıktıları ve Global ve Local Değişkenler ----------
---------------------------------------------------------------------------------

-- Çıktı değişkenleri:
1- print(): 
   - Ekrana metin veya değişkenlerin değerlerini yazdırmak için kullanılır.
   - print() içinde birden fazla variable alınabilir ve virgül (,) kullanılır.
     - x = "Merhaba"
       y = "Dünya"
       print(x, y)  # Çıktı: Merhaba Dünya
   - Bitişik yazdırmak için '+' operatörü kullanılabilir.
     - x = "Merhaba"
       y = "Dünya"
       print(x + y)  # Çıktı: MerhabaDünya
   - Bitişiklik olmasın diye araya boşluk eklenilebilir.
     - x = "Merhaba " #boşluk ekledik
       y = "Dünya"
       print(x + y)  # Çıktı: Merhaba Dünya
   - print()''te plus operatörü ile sayısal değerler toplanabilir.
     - a = 5
       b = 10
       print(a + b)  # Çıktı: 15
   - Hem integer hem string ifadeler print()''te plus operatörü ile birleştirilemez. Bunun için str() fonksiyonu kullanılabilir.
     - a = 5
       b = "python"
       print(a + b)  # HATA verir.
       print(str(a) + b)  # Çıktı: 5python
   - Birden fazla değişken print() içinde virgül ile yazdırılabilir.
     - a = 5
       b = 10
       c = "python"
       print(a,b,c)  # Çıktı: 5 10 python

-- Global ve Local Değişkenler:
1- Global Variables:
    - Fonksiyonların dışında tanımlanan değişkenlerdir.
    - Tüm fonksiyonlar tarafından kullanılabilir.
    - Global değişkenler, fonksiyonların içinde de kullanılabilir.
    - Global değişkenler, fonksiyonların içinde değiştirilemez. (global keyword ile değiştirilebilir.)
       - Örnek1:
         x = 10  # Global değişken
         def fonksiyon():
             print(x)  # Global değişkeni kullanabilir
         fonksiyon()  # Çıktı: 10
         print(x)  # Çıktı: 10

       - Örnek2:
         x = 10  # Global değişken
         def fonksiyon():
             global x  # Global değişkeni değiştirmek için global keyword kullanılır.
             x = 5  # Global değişkeni değiştirdi
         fonksiyon()  
         print("x:", x)  # Çıktı: 5

       - Örnek3:
         x = "python"  # Global değişken
         def fonksiyon():
             global x  # Global değişkeni değiştirmek için global keyword kullanılır.
             x = "java"  # Global değişkeni değiştirdi  
         fonksiyon()  
         print("Global x:"+x)  # Çıktı: Global x: java

2- Local Variables:
    - Fonksiyonların içinde tanımlanan değişkenlerdir.
    - Sadece tanımlandığı fonksiyon içinde kullanılabilir.
    - Fonksiyon dışında kullanılamaz.
       - Örnek1:
         def fonksiyon():
             y = 5  # Local değişken
             print(y)  # Local değişkeni kullanabilir
         fonksiyon()  # Çıktı: 5
         print(y)  # HATA verir. (y tanımlı değil)
       
       - Örnek2:
         x = 10  # Global değişken
         def fonksiyon():
             x = 5  # Local değişken
             print(x)  # (Local) Çıktı: 5
         fonksiyon()  
         print(x)  # (Global) Çıktı: 10

-- Neden Değişkenler Kullanılır?
   - Programın hafızasının olmaması.
   - Variable''ler sürekli değiştiğiği için, programın hafızasında saklanması gerekir.
   