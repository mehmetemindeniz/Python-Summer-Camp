age = 34
name = "Veysel KUŞ"
price = 19.563480

# text = "My name is {0} , I am {1}".format(name,age)
# print(text)

text =f"My name is {name}, I am {age}" #! kullanım amacı string içinde değişken yazabilmektir , C#'ta bu yapı $"{değişken}" şeklinde, JS'de `${değişken}` şeklindedir
print(text)

print(f"The price is {price:.2f} turkish lira")
#* price:.2f , virgülden sonra 2 basamak alır


# Not Hesaplama
notVize = input("Vize notunu giriniz: ")
notFinal = input("Final notunu giriniz: ")
ortalama = (float(notVize)+float(notFinal))/2

result = f"Vize notun: {notVize}   Final notun: {notFinal}   Sınav ortalaman: {ortalama}"

print(result)


#? Biçimlendirme Türleri

#* {:<4} 4 adet boşluk bırakır formatı sola yaslar
metin = "My name is Veysel {:<4} , I am 18"
print(metin.format(7))

#* {:>4} 4 adet boşluk bırakır formatı sağa yaslar
metin = "My name is Veysel {:>4} , I am 18"
print(metin.format(7))

#* {:^4} formatı ortaya yazar
metin = "My name is Veysel {:^4} , I am 18"
print(metin.format(7))

#* {:-} formatı pozitif sayıysa + diye belirtme 
metin = "My name is Veysel {:-} , I am 18"
print(metin.format(7))

#* {:+} formatı pozitif sayıysa + diye belirt 
metin = "My name is Veysel {:+} , I am 18"
print(metin.format(7))

#* {: } formatı pozitif sayıysa sayıdan önce 1 boşluk bırakır
metin = "My name is Veysel {: } , I am 18"
print(metin.format(-7))

#* {:,} & {:_}  formatı binlik ayırır(para ayırıcı gibi)
metin = "Benim {:,} param var"
print(metin.format(543854055867))

#* {:b} formatın binary şeklinde yazar
metin = "Benim {:b} param var"
print(metin.format(6))

#* {:c} formatın unicode şeklinde yazar
metin = "unicode: {:c}"
print(metin.format(199))

#* {:d} format binaryden sayısal şeklinde yazar
metin = "sayısal: {:d}"
print(metin.format(0b101))

#* {:e} formatı bilimsel şekilde gösterir 
metin = "sayısal: {:e}"
print(metin.format(5))

#* {:o} formatı oktal tabanda gösterir
metin = "{0}'un oktal(8lik) tabanda gösterimi: {0:o}"
print(metin.format(19))

#* {:x} formatı hexadecimal tabanda gösterir
metin = "{0}'un hexadecimal(16lık) tabanda gösterimi: {0:x}"
print(metin.format(250))




