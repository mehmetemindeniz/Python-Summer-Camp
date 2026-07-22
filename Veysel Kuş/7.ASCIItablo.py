print(ord("F")) #* ASCII kodda karşılığını verir
# ASCII: american standart code for information interchange
print(bin(70)) #* 2'lik taban(binary) karşılığını verir

print((127).bit_length()) #* bit adetini verir

print(int("c3a7",16)) #* 16'lık sistemde karşılığını verir

text = "\x50\x79\x74\x68\x6F\x6E"
result = text.encode("ascii") #* Stringi ASCII koda çevirir
result2 = result.decode() #* ASCII kodu stringe çevirir
print(text)
print(result)
print(result2)

metin = "Şükrü"
degisken1 = metin.encode(encoding="ascii",errors="backslashreplace") #* ascii kodda olmayanın 16'lık karşılığını verir
degisken2 = metin.encode(encoding="ascii",errors="ignore") #* ascii kodda olmayanı görmezeden gelir
degisken3 = metin.encode(encoding="ascii",errors="namereplace") #* ascii kodda olmayanın açıklamasını yapar
degisken4 = metin.encode(encoding="ascii",errors="replace") #* ascii kodda olmayanın yerine ? atar
degisken5 = metin.encode(encoding="ascii",errors="xmlcharrefreplace") #* ascii kodda olmayanın xml karşılığını verir
print(degisken1)
print(degisken2)
print(degisken3)
print(degisken4)
print(degisken5)

degisken = metin.encode(encoding="utf-8")
print(degisken)
