# ... py deneme.py  veya  python deneme.py
# (''')(''') yorum yapar. Veya satirlari sec ctrl+k+c  hepsi yorum satiri olur; kaldirmak icinde ctrl+k+u yaparak yorum satiri kaldirilir


"""
print("Merhaba")
"""


"""
# Integer = 5 tam sayi
# Floating = 2.1 , 0.0 , 2.5 virgullu
a = type(2.0)
print(a)

x, y, z = (1, 2.5, True)    # sirali degisken atama. True false bool konusudur.
print(x)
print(y)
print(z)
"""


"""
# Musteri adi , soyadi , cinsiyeti
musteriAdi = "Aa"
musteriSoyadi = 'Bb'
musteriCinsiyeti = True    # Erkek
print(musteriAdi)
"""


'''
x = input("1.sayi= ")
y = input("2.sayi= ")
toplam = x + y
print("Toplam sayi= ",toplam)   # String algilar 10 20 dersen sonucta 1020 yan yana yazar
toplam = int(x) + int(y)
print("Toplam sayi= ",toplam)   # int sayi algilar 10 20 dersen sonucta 30 olur
'''


'''
pi = 3.14
r = float(input("Yari cap= "))
alan = pi * r ** 2
print("Alan= ",alan)
print("Alan= " + str(alan))

name = 'Aa'
surname = 'Bb'
age = 20
print("My name is " + name + ' ' + surname + ' and I am ' + str(age) + ' years old.')
print("My name is " + name + ' ' + surname + ' and \n I am ' + str(age) + ' years old.')   # \n alt satira indirir
'''


'''
a = 'AaBb'
print(a[0])
print(a[1])
print(a[-1])
print(len(a))
length = len(a)
print(a[length - 1])
print(a[1:3])
print(a[1:])
print(a[:2])
print(a[1:3:1])   # 1 den baslar 3 e kadar 1 er 1 er demek
print(a[::])
print(a[::2])
print(a[::-1])   # Tersten yazar

a = a[0:1] + 'C' + a[2:]   # C ile degisti a[2]='C' yapamadim str oldugu icin...  
print(a)

b = a.replace('B','F')   # B gordugun yeri F yap demek.  
print(b)
'''


'''
name = 'Aa'
surname = 'Bb'
print("My name is {} {}" .format(name,surname))
print("My name is {0} {1}" .format(name,surname))
print("My name is {1} {0}" .format(name,surname))
print("My name is {n} {s}" .format( n=name, s=surname ))
print("My name is {s} {n}" .format( n=name, s=surname ))
print( f"My name is {name} {surname}")
'''


'''
# Pyton String Methods 'https://www.w3schools.com/python/python_ref_string.asp' & 'https://docs.python.org/2/library/string.html'
name = 'aa BB cc DD'
name = name.upper()   # Buyuk harfe donusturur
print(name)
name = name.lower()   # Kucuk harfe donusturur
print(name)
name = name.title()   # Bas harflerini buyuk yapar
print(name)
name = name.capitalize()   # Sadece ilk harf buyuk olur
print(name)
name = name.split()   # Cumleyi dizelere kelime kelime ayirir
print(name)
print(name[2])   # Ikinci dizeyi alir

name2 = 'aa. BB. cc. DD'
name2 = name2.split('.')   # . noktalardan ayirir
print(name2)
name2 = '*'.join(name2)   # Bir oncekiislemde ayirdik. Simdi birlestiriyoruz ve aralarina '*', * koyar.
print(name2)

name3 = "My name is Aa"
index = name3.find('is')   # is icinde var mi? arama. rfind dersen tersten saymaya baslar
print(index)   # 8. indexten itibaren var, diye cevap verir. Cevap -1 ise kelime yoktur demek
index = name3.find('is',0,10)   # 0,10 arasinda is var mi? arama  
print(index)

isFound = name3.startswith('M')   # Cumle M ile baslarsa True olur
print(isFound)

isFound2 = name3.endswith('a')   # Cumle a ile biterse True olur
print(isFound2)

name4 = 'My name is Aa'
name4 = name4.replace('Aa','Bb')   # Aa yı Bb ye donusturur
print(name4)
name4 = name4.replace('Aa','Bb').replace(' ','**')   # replace komutunu devam ettirdim. Bosluk yerlere ** ekledim.
print(name4)

name5 = 'My name is Aa'
name5 = name5.center(20,'*')   # 20 hucre ayarlar ve cumleyi ortalar
print(name5)
name5 = name5.count('a')   # 2 adet a vardir 
print(name5)

name6 = 'Merhaba'.center(50,'*')
print(name6)
'''


'''
# List
name = 'My name is Aa'.split()
print(name)   # Kelimeleri dizi olusturur
print(name[0])

my_list = ['bir', 2, True, 5.6]   # Liste icerisinde str, boolen, int ve float ayni ayna olabilir.
print(my_list)
print(len(my_list))

user1 = [1,2]
user2 = [3,4]
users = user1 + user2   # Listeleri topladi
print(users)
print(users[0])   # 1 sonucunu verir

user1 = [1,2]
user2 = [3,4]
users = [user1, user2]   # Liste icerisinde 2 farkli liste olusturdu. Liste icinde listede olusturulabilir.
print(users)
print(users[0])   # Ilk listeyi verir [1,2]
print(users[0][1])   # Ilk listenin ilk ogesini verir 1

my_list2 = [1, 2, 3]
my_list2[0] = 5   # 0. degeri 5 ile degistirdi
print(my_list2)
my_list2 = 2 in my_list2   # 2 varsa listede True degerini verir , var mi yok mu
print(my_list2)

my_list3 = [1, 2, 3]
new_list = my_list3 + [4,5,6]   # Yeni liste eklendi
print(new_list)
del new_list[0]  # 0. elemani siler
print(new_list)

my_list4 = [1,2,3,4,5,6]
my_list4 = my_list4[::-1]   # Tersten yaz
print(my_list4)

my_list5 = ['Aa', 'Bb']
sentence = f'My name is {my_list5[0]} {my_list5[1]}'
print(sentence)

my_list6 = [1,2,3,4,5]
val = min(my_list6)   # En kucuk degeri verir
print(val)
val = max(my_list6)   # En buyuk degeri verir
print(val)
my_list6[1] = 9   # 1. degeri 9 ile degistirir
print(my_list6)
my_list6.append(6)   # 6 degeri eklenir
print(my_list6)
my_list6.insert(1, 99)   # 1. degere 99 ekler
print(my_list6)
my_list6.insert(-1, 99)   # 1. degere 99 ekler
print(my_list6)
my_list6.remove(5)   # 5 siler
print(my_list6)
my_list6.pop()   # son elemani siler
print(my_list6)
my_list6.pop(0)   # ilk (0.) elemani siler
print(my_list6)
index = my_list6.index(9)   # 9 kacinci indexte, diye sorar, 1. indexte
print(index)
my_list6.reverse()   # liste elemanlarini ters cevirir
print(my_list6)
my_list6.sort()   # listeleri alfabetik, sira ile yazar
print(my_list6)
count = my_list6.count(99)   # kac adet 99 var, 2 adet var
print(count)
my_list6.clear()   # tum listeyi siler  
print(my_list6)

# input kullanarak listeleme
my_list7 = []
ekle = input("Listeye ekle : ")
my_list7.append(ekle)
print(my_list7)
'''


'''
# Tuple 
my_tuple = 1, 2, 'Aa'   # () içinde de gosterilebilir
print(my_tuple)
print(my_tuple[0])   # 0. elemani gosterir
print(len(my_tuple))   # eleman sayilarini verir
#my_tuple[0] = 5   # error verir. Listelerdeki gibi tuple nin elemani degistirilemez
print(my_tuple.count(1))   # tuple nin icinde 1 kac adet var 
print(my_tuple.index(1))   # tuple nin icinde 1 kacinci indexte
my_tuple2 = ( 5, 6, 7)
my_tuple3 = my_tuple + my_tuple2   # tuple leri birlestirir
print(my_tuple3)
'''


'''
# Dictionary, key value bilgisiyle calisir
listA = ['Aa', 'Bb', 'Cc']
listB = [1, 2, 3]
print(listB[listA.index('Aa')])   # Aa nin kacinci index e karsilik geldigini soyler

listC = {'Aa' : 10, 'Bb' : 20, 'Cc' : 30}
print(listC['Aa'])   # karsilik gelen degeri verir, 10
listC['Dd'] = 40   # olmayan bir degeri dictionary e ekler
print(listC)
listC['Aa'] = 50   # degistirir
print(listC)

users = {
    'Messi' : {
        'age' : 35,
        'country' : 'argentina',
        'number' : 10
    },
    'Ronaldo' : {
        'age' : 40,
        'country' : 'portugal',
        'number' : [20, 7]
    }
}
print(users['Messi'])   # tuple degerlerini verir
print(users['Messi']['age'])   # 35 cevabini verir
print(users['Ronaldo']['number'][1])   # number icindeki listedeki 7 numarasini verir
'''


'''
# Sets 
listA = {'Aa', 'Bb', 'Cc'}
print(listA)
#print(listA[0])   # indekslenemez. error verir
for x in listA:
    print(x)
listA.add('Dd')   # Dd eklenir
print(listA)
listA.update(['Ee', 'Ff'])   # karisik eklenir. not, var olan bir eleman yeniden eklenmez
print(listA)
listA.remove('Aa')   # Aa cikartilir
print(listA)
listA.remove('Bb')   # Bb cikartilir
print(listA)
listA.pop()   # Herhangi bir oge cikartilir
print(listA)

listD = [1, 1, 2, 2, 3, 3, 3]
print(set(listD))   # tekrarlanan sayilar cikarilir
'''


'''
# Atama Operatorleri
x, y, z = 1, 2, 3   # x=1, y=2, z=3
print(x, y, z)

x += 5   # x = x  + 5
print(x)

x, y = 1, 2
result = (x == y)   # x == y ise true 1, false ise 0 sonucunu verir 
print(result)
result = (x > y)   # x == y ise true 1, false ise 0 sonucunu verir 
print(result)
result = (x < y)   # x == y ise true 1, false ise 0 sonucunu verir 
print(result)
result = (x >= y)   # x == y ise true 1, false ise 0 sonucunu verir 
print(result)
print(True + 40)   # (True = 1) + 40 = 41 degerini verir

username = 'Aa'
password = '12'
user = username == 'Aa'
passw = password == '12'
print(f'Username: {user}, password:  {passw}')
'''


'''
# Mantiksal operatorler
x = 6
y = 5
result = 5 < x < 10
print(result)
result = (x > 5) and (y > 4)
print(result)
result = (x > 5) or (y > 6) 
print(result)
result = not(x > 5)
print(result)
'''


'''
# Identity Operator: is / Membership Operator: in
x = 5
y = 5
print(x is y)   # True verir

x = [1, 2, 3]
y = [4, 5]
print(x is y)   # False verir
print(x is not y)   # True verir
print(1 in x)   # True verir. 1 x in icinde vardir
'''


'''
# If ve else bloklari
x = 1
y = 1
result = x == y
if result:   # True ise if calisir 5
    print('Equal')

if  x == y:   # boyle de yazilabilir
    print('Equal')

x = int(input('x= '))
y = int(input('y= '))
if x < y : 
    print('x<y')
elif x == y :
    print('x=y')
else :
    print('not')

import datetime
x = datetime.datetime.now()
print(x)

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
'''


'''
# Donguler For, While, Break, Continue
# For
numbers = [1, 2, 3, 4]
for num in numbers:
    print(num)
for num in numbers:
    print('Hello')

names = ['Aa', 'Bb', 'Cc']
for name in names:
    print(f'My name is {name}')

name = 'AaBbCcDd'
for n in name:
    print(n)

tuple =  [(1,2), 5]
for a in tuple:
    print(a)

tuple =  [(1,2), (3,4)]
for a,b in tuple:
    print(a,b)
for a,b in tuple:   # a ya karsilik gelenler yazilir
    print(a)

dict = {'A':1, 'B':2}
for item in dict:   # sadece key bilgilerini verir
    print(item)
for item in dict.items():   # grup bilgilerini verir
    print(item)
for key,value in dict.items():   # sadece key bilgilerini verir
    print(key)
for key,value in dict.items():   # sadece value bilgilerini verir
    print(value)

# Alistirma
sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
 # hangileri 3 un katidir
for sayi in sayilar:  
    if ( sayi % 3 == 0 ):
        print(sayi)
# sayilar listesindeki sayilarin toplami
toplam = 0
for sayi in sayilar:   
    toplam = toplam + sayi
print (toplam)
# sayilar listesindeki tek sayilarin karesi
for sayi in sayilar:
    if sayi % 2 == 1:
        print(sayi**2)

# Alistirma
sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']
# sehirlerden hangileri en fazla 5 karakterlidir
for sehir in sehirler:
    if len(sehir) <= 5 :
        print(sehir)

# Alistirma
urunler = [
    {'name': 'samsung s6', 'price': '3000'},
    {'name': 'samsung s7', 'price': '4000'},
    {'name': 'samsung s8', 'price': '5000'},
    {'name': 'samsung s9', 'price': '6000'},
    {'name': 'samsung s10', 'price': '7000'}]
# urunlerin fiyatlari toplami 
for urun in urunler:
    print(urun)
for urun in urunler:
    print(urun['price'])
toplam = 0 
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print('Toplam urun fiyati: ', toplam)
# urunlerdem fiyati en fazla 5000 olan urunler
for urun in urunler:
    if int(urun['price']) <= 5000 :
        print(urun['name'])

# While
x = 0 
while x <= 10 :
    print(x) 
    x += 1
    
x = 0   # cift sayilari yazar
while x <= 10 :
    if x % 2 == 0 :
        print('cift sayi: ', x)
    x += 1

x = 0   # tek sayilari yazar
while x <= 10 : 
    if x % 2 == 1 :
        print('tek sayi: ', x)
    x += 1 

name = ''   # ici bos oldugu icin bu = False
while not name :   # yukarisi false oldugu icin while not True olur . name.strip() yazarsan bosluk karakterleri siler
    name = input('isim girin: ')
print(f'Merhaba {name}')   #bir isim girmezsen sonsuza kadar calisir

# Alistirma
# sayilar listesini while ile ekrana yazdirma
sayilar = [1, 3, 5, 7, 9, 12, 19, 21] 
i = 0
while i < len(sayilar) :
    print(sayilar[i])
    i += 1

# Alistirma
# 1 - 10 arasindaki sayilari azalan seklinde yazdirma
i = 10
while i > 0 :
    print(i)
    i -= 1 

# Alistirma
# kullanicidan 5 sayi al ve sirali sekilde ekrana yazdirma
numbers = []   # bos liste. burada saklanacak
i = 0
while i < 5 :
    sayi = int(input('sayi: '))
    numbers.append(sayi)
    i += 1
print(numbers)
numbers.sort()   #sayilari sirali sekilde verir
print(numbers)

# Alistirma
# kullanicidan alinan urun bilgisini urunler listesi icinde sinirsiz saklama
# urun sayisini kullaniciya sorun
# dictionary liste yapisi (name,price) seklinde olsun
# urun ekleme islemi bittiginde urunleri ekranda while ile listeleyin
urunler = []
adet = int(input('kac urun eklemek istiyorsunuz= '))
i = 0 
while i < adet : 
    name = input('urunn ismi: ')
    price = input('urun fiyati: ')
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1
for urun in urunler : 
    print(f'urun adi: {urun["name"]} urun fiyati: {urun["price"]}')

# Break and Continue 
name = 'AaBbCc'
for letter in name :
    if letter == 'b' :   #buraya geldiginde dongu durur
        break
    print(letter)

name = 'AaBbCc'
for letter in name :
    if letter == 'b' :   #buraya geldiginde sadece b iptal olur ve devam eder
        continue
    print(letter)

x = 0
while x < 5 :
    x += 1
    if x == 3 :
        break
    print(x)

x = 0
while x < 5 :
    x += 1
    if x == 3 :
        continue
    print(x)

# Dongu metotlari 
for item in range(10) :
    print(item)
for item in range(0,10,2) :   # 0 ile 10 arasinda artis miktari 2 
    print(item)

print(list(range(0,10,2)))   # list ile hizlica liste olusturulabilir

index = 0   # harfelerin kacinci index e karsilik geldigini gosterir
name = 'AaBbCc'
for letter in name :
    print(f'index: {index}  letter: {letter} ')
    index += 1

index = 0   # 2. yol, harfelerin kacinci index e karsilik geldigini gosterir
name = 'AaBbCc'
for letter in name :
    print(f'index: {index}  letter: {name[index]} ')
    index += 1

name = 'AaBbCc'    # 3. yol, harfelerin kacinci index e karsilik geldigini gosterir
for index,name in enumerate(name) :
    print(f'index: {index}  letter: {name} ')

name = 'AaBbCc'    # 4. yol, harfelerin kacinci index e karsilik geldigini gosterir
for item in enumerate(name) :
    print(item)

# zip metodu, listeleri birlestirme
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [100, 200, 300]
print(list(zip(list1, list2, list3)))

for item in zip(list1, list2, list3) :
    print(item)   #her elamana tek tek ulasilabilir

for a,b,c in zip(list1, list2, list3) :
    print(a)   #her elamana tek tek ulasilabilir

for a,b,c in zip(list1, list2, list3) :
    print(a,b)   #her elamana tek tek ulasilabilir

for a,b,c in zip(list1, list2, list3) :
    print(a,b,c)   #her elamana tek tek ulasilabilir

# List comprehensions
numbers = [ x for x in range(10) ]   # hazir liste olusturur [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

numbers = []
for x in range(10) :   # liste olusturur [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers.append(x)
print(numbers)

numbers = [ x**2 for x in range(10) ]   # liste olusturur [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
print(numbers)

# Alistirma
# Liste olustur, karesinin 3 bolunenleri, 10 a kadar
numbers = [ x*x for x in range(10) if x % 3 == 0 ]
print(numbers)

# Alistirma
# Liste olustur, kelimenin her harfini
name = 'AaBbCc'
letterList = []
for letter in name :   # 1. yol
    letterList.append(letter)
print(letterList)

letterList = [ letter for letter in name ]
# Alistirma
# Liste olustur, kelimenin her harfini

# Alistirma
# Yas hesaplama
years = [1990, 1995, 2000]
ages = [ 2020-year for year in years ]
print(ages)

# Alistirma
# Cift, Tek hesaplama
result  = [ x if x%2==0 else 'Tek' for x in range(1,10) ]   # liste olusturur ['Tek', 2, 'Tek', 4, 'Tek', 6, 'Tek', 8, 'Tek']
print(result)

# Alistirma 
# Random modulunu kullan, sayi tahmin uygulamasi
# 0-100 arasi rastgele sayi uret. asagi yukari ifadeleri ile sayiyi tahmin etmeye calis
# 100 uzerinden puanlama yap ve her soru 20 puan
import random
sayi = random.randint(1,10)
hak = 5 
sayac = 0
while hak > 0 :
    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin: '))
    if sayi == tahmin :
        print(f'tebrikler {sayac}. defada buldunuz puanınız: {100-(20)*(sayac-1)}')
        break
    elif sayi > tahmin :
        print('yukari')
    else : 
        print('asagi')
    if hak == 0 :
        print(f'hakkiniz bitti sayi: {sayi}')

# Alistirma 
# Asal sayi bulma 
sayi = int(input('sayi gir: '))
asalmi = True
if sayi == 1 :
    asalmi = False
for i in range(2,sayi) :
    if sayi % i == 0 :
         asalmi = False
         break
if asalmi :   # true ise asal 
    print('asal')
else : 
    print('asal degil')
'''


'''
# Fonksiyonlar
# Metotlar   , nokta ile metotlar gorulur
myString  = 'hello'
print(myString.upper())   # buyuk harfle yazar

# Fonksiyonlar
def sayHello() :   # Fonksiyon
    print('Hello')
sayHello()   # Fonksiyon calisir

def sayHello(name) :
    print('Hello ' + name)
sayHello('Aa')   # Hello Aa cevabini verir

def sayHello(name) :
    return 'Hello ' + name
msg = sayHello('Aa')
print(msg)   # Hello Aa cevabini verir

def total(num1, num2) :
    return num1 + num2
a = total(2,3)
print(a)

def yasHesapla(dogumyili) :
    return 2020 - dogumyili
print( yasHesapla(1990) )

def emeklilikKacYilKaldi(dogumyili, isim) : 
    yas = yasHesapla(dogumyili)   # fonksiyon icinde fonksiyon var bir ustteki fonksiyon
    emeklilik = 65 - yas
    if emeklilik > 0 :
        print(f'emekliliginize {emeklilik} yil kaldi')
    else :
        print('zaten emekli oldunuz')
emeklilikKacYilKaldi(1974, 'aa')
'''

# # Resmi fonksiyon boyle kullanilir ve help(fonkismi) ile bilgileri okunur, ogrenilir
# # not : basindan # yorunlari kaldir...
# def emeklilikKacYilKaldi(dogumyili, isim) : 
#     '''
#     DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi
#     INPUT: Dogum yili
#     OUTPUT: Hesaplanan yil bilgisi
#     '''
#     yas = yasHesapla(dogumyili)   
#     emeklilik = 65 - yas
#     if emeklilik > 0 :
#         print(f'emekliliginize {emeklilik} yil kaldi')
#     else :
#         print('zaten emekli oldunuz')
# help(emeklilikKacYilKaldi)   # help(fonkismi) ile '''xxx''' bilgileri okunur, ogrenilir
# print(help(emeklilikKacYilKaldi))   # aynisi

'''
# Fonksiyon parametreleri
# Return anlamak icin. Bu 2 ornekte ayni. return fonksiyon icini dis dunyaya aktarmayi saglar. return ile fonksiyon icinde yapilan islemler dis dunyaya tanitilir
def fonk(x) :   # 1.ORNEK return = dis dunyaya aktarmaya yarar
    return 10 - x   
print( fonk(2) )
def fonk(x) :   # 2.ORNEK return = dis dunyaya aktarmaya yarar
    print(10 - x)   
fonk(2)

def changeName(n) :
    n = 'Aa'
name = 'Bb'
changeName(name)
print(name)   # fonksiyon icini degistirdi, sonuc Bb olur

def changeCity(n) :
    n[0] = 'istanbul'
sehirler = ['ankara', 'izmir']
changeCity(sehirler)   # fonksiyon listenin 0. ogesini degistirmeye yonelik, sonuc ['istanbul', 'izmir'] olur
print(sehirler)

def add(a,b) :
    return sum((a,b))
print(add(5,4))

def add(a, b, c = 0) :  # c=0 dersek (a,b) de calisir (a,b,c) de calisir
    return sum((a, b, c))
print(add(2,3))   # a, b de calisti
print(add(2, 3, 4))   # a, b, c de calisti

def add( *params ) :   # sonsuz deger atanabilir . tuple da * / dict ** kullanilir
    return sum((params))
print(add(10, 20, 30, 40))
print(add(10, 20, 30, 40, 50, 60))

def add( *params ) :   # sonsuz deger atanabilir 
    print(params)   # tum params lari gorebiliriz
    return sum((params))
print(add(10, 20, 30, 40, 50, 60))

# Alistirma 
# sum kullanmadan topla
def add( *params ) :
    sum = 0
    for n in params :
        sum = sum + n
    return sum
print(add(10, 20, 30, 40, 50, 60))

# Alistirma 
# Bilgileri tanimlayan bir fonk yaz
def displayUser( **params ) :   # sonsuz deger atanabilir . tuple da * / dict ** kullanilir
    for key, value in params.items():
        print('{} is {}'.format(key, value))
displayUser(name='Aa', age=10)
displayUser(name='Aa', age=10, city='istanbul')

def fonk(a, b, c, *args, **kwargs) :   # tuple da * / dict ** kullanilir
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
fonk(10, 20, 30, 40, 50, key1='value1')   # once a b c yi aldi, sonra tuple aldi, sonra dict aldi
fonk(10, 20, 30, 40, 50, key1='value1', key2='value2')   # once a b c yi aldi, sonra tuple aldi, sonra dict aldi
'''
# Alistirma 


