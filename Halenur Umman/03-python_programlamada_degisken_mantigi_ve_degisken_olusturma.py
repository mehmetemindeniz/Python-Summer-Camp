---------- Variable (Degisken)----------
---------------------------------------- 

-- Variable (değişken), programlama dillerinde verileri saklamak için kullanılan bir isimlendirilmiş bellek alanıdır.
-- Python''da variable tanımlamak için herhangi bir veri türü belirtmeye gerek yoktur. 
-- Python, değişkenin değerine göre veri türünü otomatik olarak belirler.
- x = 7
  y = "Hello, World!"
  print(x)
  print(y)

-- Python''da bir veri, tam sayı olarak oluşturulduğunda sonrasında string olarak değiştirilebilir.
- x = 7
  x = "Hello, World!"
  print(x) # Cevap: Hello, World!
  
  ---- Veri Türünü Tanımlama (Casting)

--Python''da veri türünü değiştirmek için casting işlemi yapılır.
- x = str(3)    # x, str tipinde olur
- y = int(3)    # y, int tipinde olur
- z = float(3)  # z, float tipinde olur

--Veri türünü öğrenmek için type() fonksiyonu kullanılır.
- x = 5
- y = "Hello, World!"
  print(type(x)) # Cevap: <class 'int'>
  print(type(y)) # Cevap: <class 'str'>

-- Metinsel veri türleri (string) için tek tırnak veya çift tırnak kullanılabilir.
- x = "Hello, World!"
- y = 'Hello, World!'
  print(x) # Cevap: Hello, World!
  print(y) # Cevap: Hello, World!

--Python''da case sensitive (büyük/küçük harf duyarlılığı) vardır. 
  Bu nedenle değişken isimleri büyük/küçük harf duyarlıdır.
- x = 5
- X = "Hello, World!"
  print(x) # Cevap: 5
  print(X) # Cevap: Hello, World!

- name = "John"
- namE = "Doe"
  print(name) # Cevap: John
  print(namE) # Cevap: Doe 

