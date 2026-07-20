# choice() --> seçim / seçmek anlamına gelir
# verilen seriden rastgele bir öğe döndürür 
# bu bir string, list, tuple, range vs. olabilir 

import random

renkler = ["beyaz","kırmızı","mavi","sarı","lacivert","pembe","yeşil"]
# hangi renk olsun :)
print("Duvarlar", random.choice(renkler), "olsun :)")

text = "python"
print(random.choice(text)) # string içindeki harflerden birini rastgele seçer 