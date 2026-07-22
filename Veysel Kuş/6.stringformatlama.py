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


#?
metin = "My name is Veysel {:<3} , I am 18"
#* {:<3} 3 adet boşluk bırakır sola yaslar
#* {:>3} 3 adet boşluk bırakır sağa yaslar
print(metin.format(7))