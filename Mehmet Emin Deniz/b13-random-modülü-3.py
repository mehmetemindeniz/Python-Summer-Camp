import random # kütüphanemizi import ettik

# bu konular ileri seviye konular
# daha çok istatistiğin olasılığın ve matematiğin konuları 

# --------------------------------------------------------

# betaveriate() beta dağılımına göre 0 ile 1 arasında rastgele ondalıklı bir sayı döndürür

print(random.betavariate(1,8)) # ilk parametre ve ikinci parametre 0'a ve 1'e olan uzaklıklarını etkiler.
# ilk parametre sıfıra ne kadar yakın olacağını ikinci parametre 0'dan ne kadar uzak olacağını ifade eder.

# ---------------------------------------------------------

# expovariate() ===> üstel dağılıma göre rastgele bir ondalıklı sayı döndürür, istatistikte kullanılır
print(random.expovariate(0.4))

# ----------------------------------------------------------

# gammaveriate() ==> gamma dağılımına göre rastgele bir ondalıklı sayı döndürür
# alfa ve beta olarak 2 adet parametre alır 
print(random.gammavariate(100,2))

# ----------------------------------------------------------

# gauss() ==> gaus dağılımına göre rastgele ondalıklı bir sayı üretir,  olasılık teorilerinde kullanılır 
print(random.gauss(100,2))

# ----------------------------------------------------------

# lognormvariate(0, 0.25)
print(random.lognormvariate(0,25))

# ----------------------------------------------------------

# normalvariate() ===> normal dağılıma göre ondalıklı sayılar üretir. olasılık teorilerinde kullanılır.
print(random.normalvariate(100,50))

# -----------------------------------------------------------

# vonmisesvariate() ===> vonmises dağılımına göre bir ondalıklı sayı üretir
# yön istatistiklerinde kullanılır.
print(random.vonmisesvariate(0,5))

# -----------------------------------------------------------

# paretovariate() ===> pareto dağılımına göre rastgele ondalıklı bir sayı üretir
# olasılık teorilerinde kullanılır. 
print(random.paretovariate(6))

# ------------------------------------------------------------

# weilbullvariate() ===> weibull dağılımına göre rastgele ondalıklı bir sayı üretir.
# istatitstikte kullanılır.
print(random.weibullvariate(1,5))

# -------------------------------------------------------------

# random modülü ileri seviye programalamlarda işimize yaramaktadır.

# -------------------------------------------------------------