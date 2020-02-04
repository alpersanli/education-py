"""
#integer
a=5
print(a)





#float
type(a)





#integer
name='aa'
surname='bb'
print(name + surname)





#type change - float str int bool
thisisnumber=5.5
print(int(thisisnumber))
aa="alp"
print(str(aa))
a=0
aa=5
aaa=""
aaaa="aaa"
print(bool(a))  #deger 0 ise false digerlerinde true verir
print(bool(aa))
print(bool(aaa))    #bosluk varsa false digerlerinde true verir
print(bool(aaaa))





#print sep end \n   ()varsa fonksiyon belirtir
a=5
b="bbb"
print(a,b,"adsadsad")  #virgül koydum ama sonucunda bosluk verdi
print('T','B','M','M',sep="---")
print('T','B','M','M',end="\n")
print('T','B','\n','M','M',end="---")





#kimlik karti uygulamasi
name="a"
surname="b"
print("====================")
print("Name    =",name)
print("Surname =",surname)
print("====================")





#input
isim= input("Isminizi Giriniz:")
print("Isminizi soyle girdiniz:",isim)

x=5
y=input("y degeri girin:")
print(x+int(y)) #y degeri int turune cevrildi





#hesap makinesi
birinci_sayi=float(input("Birinci Sayi="))
ikinci_sayi=float(input("İkinci Sayi="))
print("============================")
print("Toplama Sonucu:",birinci_sayi+ikinci_sayi)
print("Cikarma Sonucu:",birinci_sayi-ikinci_sayi)
print("Carpma Sonucu:",birinci_sayi*ikinci_sayi)
print("Bolme Sonucu:",birinci_sayi/ikinci_sayi)





#if else
x=int(input("Bir sayi gir="))
if x==5:    #if eger ise ise isareti ==
    print("Dogru sayi girdin.") #4 spece bosluk var
else:
    print("Yanlis sayi girdin.")

x=input("Bir sayi gir=")
if bool(x):
    print("Sayi girdin.")
else:
    print("Sayi girmedin.") #program cokmez





#hesap makinesi #bunu kaldir
print("[1] Toplama [2] Cikarma ")        #aralarında  var alt satıra gecmek icin
giris=input("Giris Sec=")
if giris=="1":  #"" var cunku int w cevirmedik
    print("Sonuc=",1+2)





#aritmetik operatorler
print(20*"a")   #20 tane a yazar
print(5**2)     #5 in 2 üssünü yazar
print("Normal Bolme:",5/2)
print("Taban Bolme:",5//2)

x=5
if x % 2 == 0 : #% mod alma kalan
    print("x cift sayidir.")
else:
    print("x tek sayidir.")





#arsilastirma operatorleri == esit, != esit degil, > buyuk, < kucuk, >= buyuk esit, >= kucuk esit
giris=input("Parola=")
sifre="deneme"
if giris == sifre :
    print("Parola dogru.")
if giris != sifre :
    print("Parola yanlis.")

giris=int(input("1 ile 10 arasinda sayi gir:"))
if giris > 50 :
    print("50 den buyuk.")
elif giris < 50 :
    print("50 den kucuk")
else:
    print("sayi 50")





#bool operatorleri and or not (not false u true ; true da false yapar)
x=int(input("Sayi gir:"))
if x>5 and x==6:
    print("Dogru.")





#deger atama yontemleri
x=5
print("ilk hal:",x)
x=x+1
print("ikinci hal:",x)
x+=1 #ustteki ifadeyle aynidir
print("ucuncu hal:",x)





#aitlik operatoru in islemci
x="abc"
if "b" in x:    #b yi kesme isaretleri arasina almayi unutma
    print("Ait.")
x="asdfg"
if "e" not in x:
    print("e yoktur.")
else:
    print("vardır.")





#is islemci, id islemci
a=5
b=5
if a==b:
    print("ayni")
if a is b:
    print("ayni")
print(id(a))
print(id(b))
print(id(5))    #ayni kimlik atanir





#for dongusu, while dongusu
x="asdfghjkli"
for harf in x:
    print(harf)     #alt alta print komutunu tekrar eder
for harf in x:
    print(harf,end = "")    #yan yana yazar
for harf in x:
    print(harf,end = "\n")  #alt alta yazar ama a yukarda kaldi dikkat
for harf in x:
    print(harf,end = "---")


#BU COK ONEMLI
alfabe="asdfghj"
sayi=0
for x in alfabe:    #x onemli degil i de yazabilirsin
    sayi += 1
print(sayi)         #alfabenin oge sayisi kadar islem yapti





#
for sayi in range(0,10):
    print(sayi)        #0 dahil, 10 dahil degil

for sayi in range(0,10):
    print("Bu",str(sayi) + "'ıncı dongu")   #bu onemli

for sayi in range(10):
    print(sayi)

for sayi in range(0,10,2):
    print(sayi)





#while dongusu durdurmazsan sonsuza kadar gider
x=0
while x <= 10 :
    print(x)
    x+=1
print("degeri",x)   #11 oldugunda durdu





#FONKSIYONLAR
#print, len, range
#tanimlama islemi:
def topla():
    sonuc = 3+5
    print(sonuc)    #tanimlama yapildi
topla()     #8 cevabını verir
topla()
topla()
topla()

#parametrize edilme ozelligi
def topla(birincisayi,ikincisayi):
    sonuc = birincisayi + ikincisayi
    print(sonuc)
topla(5,6)      #ærasinda virgul var dikkat et

def topla(birincisayi,ikincisayi):
    sonuc = birincisayi + ikincisayi
    return sonuc
print(topla(6,8))





#ucgen kontrol uygulamasi
def ucgenmi(a,b,hipotenus):
    if a**2 + b**2 == hipotenus**2:
        return "Bu bir ucgendir"
    else:
        return "Bu bir ucgen degildir."
print(ucgenmi(3,4,6))
print(ucgenmi(3,4,5))





#ornek bicimlendirme denemesi
#her nesnenin metodlari vardir .koyarak gorebiliriz
cumle="English:Hello World ve Turkish:{} {}"
print(cumle)    #bir altta .format ile {} icini dolduracagim
cumle="English:Hello World ve Turkish:{} {} ".format("Merhaba","Dunya")
print(cumle)

#bir altta .format ile {} icini dolduracagim
cumle="English:Hello World ve Turkish:{1} {0}".format("Merhaba","Dunya")       #ilki 0 ikincisi 1 dir
print(cumle)

karakterler="asdfgh"
for i in karakterler:
    print("Bastirila karakterler {}".format(i))     #bu onemli

degisken1 = "alp"
degisken2 = "er"
ifade1 = "{ad} {soyad}".format(ad=degisken1,soyad=degisken2)
print(ifade1)
ifade2 = "{0} {1}".format(degisken1,degisken2)
print(ifade2)
ifade3 = "{:>15}".format(degisken1)      #saga sola yasla
print(ifade3)
ifade4 = "{:^15}".format(degisken1)     #ortaliyor
print(ifade4)
#:s yalnizca string, :d yalnizca sayisal, :b ikilik sistemde karsiligini verir
ifade5 = "{:,}".format(2136238213621)   #sayilari basamaklarina ayirir
print(ifade5)





#Kacis Dizileri
print("a")
print("b")

print("a",end="")
print("b")

print("a",end="\n")
print("b")

print("\tALPER")        #1 sekme kadar tab boslugu kadar bosluk birakir

print("Hello\vWorld")    #\v düşey sekme kaçış dizisi





#Liste
kitaplar = []
#veya
kitaplar = list()   #ile liste yazilabilir
kitaplar = ["abc",12,5.3]
for i in kitaplar:
    print(i)
for i in kitaplar:
    print("Kitabin adi: {}".format(i))
#liste icerisine kitap ekleme
eklenecek = input("Eklenecek kitap: ")
kitaplar += eklenecek
print(kitaplar)     #her harfi ayri ayri aldı
kitaplar += [eklenecek]
print(kitaplar)     #tek bir kitap olarak alir





#Kutuphane uygulamasi
kitaplistesi= list()
menu= "[1]Kitap ekle,[2]Kitaplar cikar, [3]Kitaplari goster, [q]Cikis yap"
def kitapekle(kitap,liste):
    liste += [kitap]    #koseli paranteze almazsak harf harf alir
    print("Kitap eklendi.")
    input("Menuye donmek icin entera bas.")
def kitapcikar():
    pass
def listele(liste):
    for i in liste:
        print("Kitaplar : {}".format(i))
    input("Menuye donmek icin entera bas.")
def cik():
    quit()
while True:
    print(menu)
    secim = input("Seciminiz: ")
    if secim == "1":
        kitapadi = input("Kitap ekle: ")
        kitapekle(kitapadi,kitaplistesi)
    elif secim == "2":
        kitapcikar()
    elif secim == "3":
        listele(kitaplistesi)
    elif secim == "q" or secim == "Q" :
        cik()
    else:
        print("Hatali girdiniz")
        input("Menuye donmek icin entera bas.")





#liste ogelerine erisim
liste = ["asd","123",1,["a",5]]     #direkt a yazamazsin "a" yazman lazim
print(liste[0])
print(liste[1])
print(liste[2])
print(liste[-1])
print(liste[-1][1])     #icindeki listeninde elemanlarina iner
print(liste[0][2])      #d yi verir. sadece listede degil stringde de gecerlidir yani bir altta
kelime = "alper"
print(kelime[2])





#Sozlukler      icindeki siralama surekli degisir o yuzden yanindaki anahtar kelimelerle cagirilir
sozluk = {"home":"ev" , "book":"kitap" , "pen":"kalem"}
print(sozluk["home"])

karakter = {"ad":"aaaa" }
print("Karakter bilgileri adi {}".format(karakter["ad"]))





#Demetler tuple()
demet = ("degisken",)   #sonunda virgul varsa demet olur
print(type(demet))      #tuple yani demet oldugunu anladik
#listeden farki ekleme cikartma yapilamaz. listeler cok hizli oldugu icin kullanilir





#dir() komutu
liste = ["a","b"]
for i in dir(liste):
    print(i)    #tum metotlari gosterecek mesela arasinda append ve remove onemli. Ayrica noktaya basildiginde de gorunur
liste.append("c")
print(liste)    #"c" eklendi
liste.remove("a")
print(liste)
#bu olay stringde de kullanilabilir
string =  "abc"
for i in dir(string):
    print(i)    #tum metodlari gosterecek, nokta ile de yapilabilir
#liste.sort() siralar, liste.count() sayar, index vb.... bir suru var





#Kumeler set() kume, add, difference(fark), discard, remove, intersection(kesisim)
# []liste, {}sozcuk, ()demet, ""string, kumede de set() kullanilir
#kume icinde sadece sayi kullanilamaz. liste, sozcuk, demet, string yapisinda olmali
string = "asdasd"
kume = set(string)
print(kume)     #hepsini almaz her ogeden sadece 1 kere alir





#Hata yakalama
#try ve except
bolunen = float(input("Bolunen: "))     #input ile girdigi icin float olarak belirttik
bolen = float(input("Bolen: "))
try:
    print("Sonuc: ",bolunen/bolen)
except ZeroDivisionError:
    print("0a bolunemez")

bolunen = float(input("Bolunen: "))
bolen = input("Bolen: ")
try:
    print("Sonuc: ",bolunen/bolen)
except TypeError:
    print("Veri tipi desteklenmiyor")
finally:
    print("Bu komut hep var")

bolunen = float(input("Bolunen: "))
bolen = float(input("Bolen: "))
try:
    print("Sonuc: ",bolunen/bolen)
except:         #hata turu ne olursa olsun except hepsini kapsar ERROR VERMEZ
    print("0a bolunmez")





#raise  python tarzi hata verir kirmizi renkler ile
x = int(input("Bir sayi gir: "))
if x == 5 :
    raise Exception("Bu programda 5 sayisini kullanma!")





#String ileri seviye
string = "asdfghj"
print(string[2])
print(string[2:6])  #ama 6yi dahil etmez
print(string[2:])
print(string[:6])
print(string[::-1])    #-tersinden yazilir, 1 dilimi belirtir
print(string[::2])      #2 dilimi belirtir





#Dosya Olusturmak
#w yazmak,a yazmak(dosyayi silmez 2. satirdan kaldigi yerden devam eder), x yazmak (varsa hata verir),
# r+ okuma ve yazma (var olmasi gerekir), w+ okuma ve yazma(varsa siler), a+ okuma ve yazma, x+ okuma ve yazma
dosya = open("deneme.txt","w")  #dosyayi acar, w dosya yoksa olusturur
yazilacaklar = "dosyanin icine yaziliyor"
dosya.write(yazilacaklar)   #soldan txt tikla dosyaya yazilmis olacak
dosya.close()

dosya = open("deneme.txt","r")  #r dosyayi okur
okunan = dosya.readlines()
print(okunan)
dosya.close()

dosya = open("deneme.txt","a")
dosya.write("deneme satiri 2 ")





#Lokanta Uygulamasi
import os
masalar = dict()    #Sozcuk veri tipini kullanarak yapacagız
for i in range(10):
    masalar[i]=0    #0dan 10a kadar masalar olusturuldu
def hesapekle():
    masano=int(input("Masa numarasi girin: "))
    gecerliucret=masalar[masano]
    eklenecek=float(input("Eklenecek ucret: "))
    toplam=gecerliucret+eklenecek
    masalar[masano]=toplam
def hesapcikar():
    masano=int(input("Masa numarasi girin: "))
    gecerliucret=masalar[masano]
    cikarilacak=float(input("Cikarilacak ucret: "))
    cikan=gecerliucret-cikarilacak
    masalar[masano]=cikan
def hesapkontrol(dosya_adi):
    try:
        dosya = open(dosya_adi)
        veriler = dosya.read()
        veriler = veriler.split("\n")   #\n oldugu her yerden veriler bolunecek
        veriler.pop()   #split te son veri bos olacagi icin sildik
        dosya.close()
        flag = True
    except FileNotFoundError:
        dosya = open(dosya_adi,"w")
        dosya.close()
        print("Kayit dosyasi olusturuldu")
        flag = False
    if flag:
        for i in enumerate(veriler):   #enumerate iyi demet olarak veri gonderir
            masalar[i[0]] = float(i[1])    #yani text icinde ilk satir 45 ise programda 0.masa 45 tir
        else:
            pass
def kayitguncelle():
    dosya = open(dosya_adi, "w")
    for i in range(10):
        ucret = masalar[i]
        ucret = str(ucret)
        dosya.write(ucret + "\n")
    dosya.close()
def main():
    hesapkontrol("kayitlar.txt")
    while True:
        os.system("cls")
        print("[]Masalari goruntule\n[2]Hesap ekle\n[3]Hesap Cikar\n[q]Cikis")
        secim=input("Islemini Sec: ")
        if secim == "1" :
            for i in range(10):
                print("Masa {} icin hesap: {}".format(i,masalar[i]))
            print("Islem tamamlandi. Ana menuye donmek icin entera bas")
            input()
        elif secim == "2" :
            hesapekle()
            print("Islem tamamlandi. Ana menuye donmek icin entera bas")
            input()
        elif secim == "3" :
            hesapcikar()
            print("Islem tamamlandi. Ana menuye donmek icin entera bas")
            input()
        elif secim == "q" :
            print("Cikiliyor")
            quit()
        else :
            print("Hatali secim")
            print("Islem tamamlandi. Ana menuye donmek icin entera bas")
            input()
main()   #FONKSIYON CAGIRILIR, CALISIR





#lambda fonksiyonu
def ucgenmi(a,b,c):
    if a**2+b**2==c**2 :
        return True
    else:
        return False
print(ucgenmi(3,4,5))
#bunun aynisi aslinda:
fonk = lambda a,b,c : a**2+b**2==c**2
print(fonk(3,4,5))





#Ozyinelemeli fonksiyon recursion
def faktoriyel(sayi):
    if sayi == 1:
        return 1
    else:
        return sayi * faktoriyel(sayi-1)
print(faktoriyel(5))





#import etmek
import os   #os.py dosyanin hepsi artik burada os. bastiginda bir suru modul cikacak
from os import system   #os modulunden sadece system i davet et
system("cls")
from os import system as komut  #ismini degistirdin
komut("cls")
import os as sistemdosyasi
sistemdosyasi.system("cls")





#os modulu
import os
for i in dir(os):
    if "__" not in i:
        print(i)

import os
bulundugum_dizin = os.getcwd()
print(bulundugum_dizin)

import os
print("bir seyleeer")
input("entera bas")
os.system("cls")    #terminali sifirlar






#time modulu
import time
for i in dir(time):
    if "__" not in i:
        print(i)
print("Bu birinci satir")
print(time.localtime())
time.sleep(5)   #5 sn sonra ikinci satir ekrana gelecek
print("ikinci satir")

import time
zaman1 = time.time()
zaman2 = time.time()
print("fark : {}".format(zaman2-zaman1))





#random modulu
import random
for i in dir(random):
    if "__" and "_" not in i:
        print(i)

from random import randint
from os import system as komut
komut("cls")
rastgelesayi = randint(10,50)
print(rastgelesayi)





#Nesne tabanli programlama (OOP) insan türü siniftir, her insan bu sinifin nesneleridir
class Asker():  #class isimleri Büyük Harfle baslar
    saglik = 100
    isim = "ahmet"
    silah = "tufek"
print(Asker.saglik)
Asker.mermisayisi = 200     #boyle niteliklerde uretilebilir
print(Asker.mermisayisi)

class Siparis():
    urun = ""
    miktar = ""
gofret = Siparis()
gofret.urun = "cikolatali"
gofret.miktar = 10
su = Siparis()
su.urun = "temiz"
su.miktar = 100
print(gofret.urun)
print(gofret.miktar)
print(su.urun)
print(su.miktar)

class Siparis():
    urunler = []
    miktar = ""
gofret = Siparis()
gofret.urunler += ["cikolatali"]        #beraber yazdi
gofret.miktar = 10
su = Siparis()
su.urunler += ["temiz"]
su.miktar = 100
print(gofret.urunler)
print(gofret.miktar)
print(su.urunler)
print(su.miktar)





#Ornek nitelikleri
class Asker:
    kabiliyetler = []               #Sinifa ait
    def __init__(self,isim,guc):    #Ornege ait
        self.isim = isim
        self.gucu = guc
        self.kabiliyetler = []
ahmet = Asker("Ahmet",80)
mehmet = Asker("Mehmet",60)
print(ahmet.isim)               #Ornegi aldı
print(mehmet.gucu)              #Ornegi aldı
print(mehmet.kabiliyetler)      #usttekini aldı





#Basit Oyun Uygulamasi
import random
class Dusman():     #dusman sinifi olusturduk
    def __init__(self): #her ornek farkli farki. 10 dusman var hepsinin ozellikleri farkli
        self.sagmi = True
        self.saglik = random.randint(30,70)
        self.kalkan = random.randint(0,10)
        self.guc = random.randint(20,50)
    def vur(self,player):      #ornege aittir ve self hemen . fonk
        damage = self.guc - player.kalkan
        player.saglik -= damage
        if player.saglik <= 0 :
            player.sagmi = False
class Player():     #kendimizi yaziyorum
    def __init__(self):
        self.sagmi = True
        self.saglik = 500
        self.kalkan = 20
        self.guc = 55
    def vur(self,dusman):      #ornege aittir ve self hemen gelir. fonk
        damage = self.guc - dusman.kalkan
        dusman.saglik -= damage
        if dusman.saglik <= 0 :
            dusman.sagmi = False
            dusmanlar.remove(dusman)
dusmanlar = list()
for i in range(10):
    dusmanlar.append(Dusman())    #dusmanlar listesine 1 tane dusman eklendi
player = Player()
while True:
    print("Player. Saglik={} Guc={} Kalkan={}:".format(player.saglik, player.guc, player.kalkan))
    if player.sagmi == False :
        print("Game Over")
        quit()
    if not dusmanlar:
        print("Kazandın")
        quit()
    for i in dusmanlar:
        print("{}. dusman. Saglik={} Guc={} Kalkan={}:".format(dusmanlar.index(i),i.saglik,i.guc,i.kalkan))
    secim = int(input("Bir dusman secimi: "))
    dusman = dusmanlar [secim]
    player.vur(dusman)





#Banka Uygulamasi
from os import system as komut
class Musteri():
    def __init__(self,id,parola,isim):      #selfin yaninda veya altta da tanitabilirsin. Ama once selfi unutma
        self.id = id
        self.isim = isim
        self.parola = parola
        self.bakiye = 0
class Banka():
    def __init__(self):
        self.musteriler = list()        #bos listesi olur
    def musteriol(self, id:str, parola:str, isim:str):
        self.musteriler.append(Musteri(id,parola,isim))
        print("Bankamiza kayit old icin tesekkürler")
def main():     #ileri programlamada her sey class icinde oluyor
    banka = Banka()
    while True:
        komut("cls")
        print("[1]Musteriyim  [2]Musterisi olmak istiyorum")
        secim = int(input("Seciminiz: "))
        if secim == 1 :
            ids = [i.id for i in banka.musteriler]
            ID = input("ID: ")
            if ID in ids:
                for musteri in banka.musteriler:
                    if ID == musteri.id:        #musteri bulundu
                        print("Hosgeldiniz {}".format(musteri.isim))
                        parola = input("Parola gir: ")
                        if parola == musteri.parola:
                            print("Giris basarili")
                            while True:
                                komut("cls")
                                print("[1]Bakiye sorgula [2]Para Yatir kendi hesabina [3]Para Yatir baskasinin hesabina [4]Para cek [q]Cikis")
                                secim2=input("Isleminiz: ")
                                if secim2 == 1 :
                                    print("Bakiyeniz {}".format(musteri.bakiye))
                                    input("Ana menuye donmek icin entera bas")
                                elif secim2 == 2 :
                                    miktar = int(input("Miktar: "))
                                    onay = input("Kendi hesabiniza {} TL para yatirmayi onayliyor musunuz? e/h\n".format(miktar))
                                    if onay == "e" :
                                        musteri.bakiye += miktar
                                        print("Paraniz yatirildi.")
                                        input("Ana menuye donmek icin entera bas")
                                    elif onay == "h":
                                        print("İptal edildi")
                                        input("Ana menuye donmek icin entera bas")
                                    else:
                                        print("Hatali girildi, islem iptal")
                                        input("Ana menuye donmek icin entera bas")
                                elif secim2 == 3 :
                                    arananid = input("Musteri ID: ")
                                    if arananid in ids:
                                        for digermusteri in banka.musteriler:
                                            if arananid == digermusteri.id:  #musteri bulunmus oldu
                                                miktar = int(input("Miktar: "))
                                                if  miktar <= musteri.bakiye:
                                                    onay = input("{} adli musteriye {} TL para yatirmayi onayliyor musun? e/h\n".format(arananid,miktar))
                                                    if onay == "e" :
                                                        digermusteri.bakiye +=miktar
                                                        musteri -= miktar
                                                        print("Para aktarildi")
                                                        input("Ana menuye donmek icin entera bas")
                                                    elif onay == "h":
                                                        print("İptal edildi")
                                                        input("Ana menuye donmek icin entera bas")
                                                    else:
                                                        print("Hatali girildi, islem iptal")
                                                        input("Ana menuye donmek icin entera bas")
                                                else:
                                                    print("Bakiye yetersiz")
                                                    input("Ana menuye donmek icin entera bas")
                                    else:
                                        print("Musteri bulunamadi")
                                        input("Ana menuye donmek icin entera bas")
                                elif secim2 == 4 :
                                    miktar = int(input("Miktar: "))
                                    if miktar <= musteri.bakiye:
                                        musteri.bakiye -= miktar
                                        print("Islem tamamlandi")
                                        input("Ana menuye donmek icin entera bas")
                                    else:
                                        print("Bakiye yetersiz")
                                        input("Ana menuye donmek icin entera bas")
                                elif secim2 == "q" :
                                    break
        elif secim == 2 :
            id = input("Id: ")
            parola = input("Parola: ")
            isim = input("Isminiz: ")
            banka.musteriol(id,parola,isim)
if __name__=="__main__":      #def main() den kalan
    main()





#Miras alma heritage
class Tasit():
    def __init__(self,tekersayisi,kapisayisi):
        self.tekerleklerininsayisi = tekersayisi
        self.kapilarininsayisi = kapisayisi
class Araba(Tasit):
    pass
#print(Araba.kapilarininsayisi)  #BU HATA VERIR
araba = Araba(4,2)
print(araba.kapilarininsayisi)





#Miras alma turleri
class Tasit():
    def __init__(self,tekersayisi,kapisayisi):
        self.tekerleklerininsayisi = tekersayisi
        self.kapilarininsayisi = kapisayisi
    def kapiac():
        print("Kapi acildi")
class Tir(Tasit):
    def dorsebirak():
        print("Dorse birakildi")





#Sesli komutla kontrol
#(venv) C:\Users\alptunga\Desktop\test>pip install speechrecognition    terminale yaz ve indir
#You are using pip version 10.0.1, however version 20.0.2 is available.
#You should consider upgrading via the 'python -m pip install --upgrade pip' command.
#(venv) C:\Users\alptunga\Desktop\test>pip install PySpeech
#pip install pipwin     #pyaudio icin
#pipwin install pyaudio
#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import speech_recognition as sr
# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio,language="tr"))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
"""





#Sesli komutla kontrol
import speech_recognition as sr
from os import system as komut
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
flag = False
try:
    text = r.recognize_google(audio,language="tr")
    print("You said: " + text )
    flag = True
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
if flag :
    if text == "Program çalıştır" :
        print("ben")
    else:
        print("Tekrar dene")









#son
