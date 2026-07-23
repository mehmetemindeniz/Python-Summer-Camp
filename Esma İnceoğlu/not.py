#veri türleri ve birleştirme 
#--------------------------------------


#+ opretörü ile integer olan bir sayıyı string ile birleştirme yapamayız 
#print("isim:"+name+"yas:"+age+"kilo:"+weight)  burada name=string , age=integer,weight =float veri tipindedir
#farklı veri türlerini birleştirmek itersek , kullanarak yapmamaız gerekir 
#print("isim:",name,"yas:",age,"kilo:",weight) ya da tür dönüşümleri yapmamız lazım ;
#print("isim: "+name+"yas: "+str(age)+"kilo: "+str(weight)) ile de tip dönüşümleri sayesinde birleştirme yapabiliriz
# , ile birleştirmede kendisi boşluk bırakır ama + ile birleştirmede bizim boşluk bırakmamaız lazım yoks hepini birleşik yazar 


#sıra türleri(tuple,list,range)  bunlar da veri türleridir 
#---------------------------------------


#list:
#myList=["apple","banana","cherry"]-->köşeli parantez 
#tuple:
#myTuple=("apple","banana","cherry")-->normal parantez
#tuple ın listelerden en büyük farkı değiştirilemezbyapılardan oluşmasıdır,
#tuple ın içindeki bir eleman ancak listeye dönüştürülmesinin ardından değiştirilebilir.
#list(myTuple) ile tuple ımı listeye dönüştürmem lazım ,
#dönüştürdükten son bir variazble a atamam lazım yani x=list(myTuple) yapmam lazım 
#range:
#0 dan fonksiyonun içine yazdığımız saynın bir eksiğğii kadar sayı dizisi oluturuyor 
#myRange=range(5)-->0 dan 4 e kadar (1-2-3-4) 
#döngülerde kullanılır


#dict data type 
#-------------------------------

#myDict={"name":"esma","age":21} anahtar değer çifti name-esma ve age-21  
#--------------------------
 #none null anlamındadır boş demektri bir veri trüdür

