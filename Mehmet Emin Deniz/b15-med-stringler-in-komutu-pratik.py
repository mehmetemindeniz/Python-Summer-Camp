# Örnek:
#Bir mesaj tarama programı yazmanı istiyorum. 
# Kullanıcıdan 4 mesaj alacağım ve bu mesajlar içerisinde aratmak istediği bir ifadeyi soracağım. 
# Eğer bu ifade mesajlar içerisinde geçiyorsa kullanıcıya bunu bildireceğim.
# Bir whatsapp konuşması gibi düşünelim. Ahmet ve Necip arasında geçen bir konuşma olsun.
# Kullanıclar ikişer mesaj atmış olacaklar.
# Atılan her mesaj string olarak bir değişkene kaydedilecek.
# Sonrasında kullanıcıdan aratmak istediği ifadeyi soracağım 
# Bu ifade mesajlar içerisinde geçiyorsa kullanıcıya bunu bildireceğim.
# Bu kontrolü in komutu ve if koşulu ile yapmanı bekliyorum.



# === Mesaj Tarama Programı ===

ahmet_ilk_mesaj = input("Ahmetin ilk mesajını giriniz: ")
necip_ilk_mesaj = input("Necip'in ilk mesajını giriniz: ")
ahmet_ikinci_mesaj = input("Ahmet'in ikinci mesajını giriniz: ")
necip_ikinci_mesaj = input("Necip'in ikinci mesajını giriniz: ")

aranan = input("Konuşma içinde aratmak istediğiniz ifadeyi yazınız: ") 

if aranan in ahmet_ilk_mesaj or ahmet_ikinci_mesaj or necip_ilk_mesaj or necip_ikinci_mesaj:
    print("\n\nKonuşma içerisinde", aranan, "geçmektedir.") 