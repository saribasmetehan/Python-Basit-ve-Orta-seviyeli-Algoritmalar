
"""""
#Araç yakıt hesaplanması

ikm = float(input("Kaç km şehir içinde yol aldınız : "))
dkm = float(input("Kaç km şehir dışında yol aldınız "))
icilitre = float(ikm*0.66*22.16)
disilitre = float(dkm*0.43*22.16)
print("Şehir içi litre tüketiminizin maliyeti : ", int(icilitre),"TL")
print("Şehir dışı litre tüketiminiz : ", int(disilitre),"TL")
print("Toplam maliyet : ",int(icilitre+disilitre),"TL")

""""""
#vücut kitle indeksine göre sağlık durumu hesaplamak

boy = float(input("Metre cinsinden boyunuzu giriniz : "))
kilo = float(input("Kg cinsinden kilonuzu giriniz : "))
indeks = kilo/(boy*boy)

if indeks <= 18.5 :
    print("Vücut kitle indeksiniz : {} Zayıfsınız.".format(indeks))
elif 18.5 <= indeks <= 25 :
    print("Vücut kitle indeksiniz : {} Normalsiniz.".format(indeks))
elif 25  <= indeks <= 30  :
    print("Vücut kitle indeksiniz : {} Fazla kilolusunuz.".format(indeks))
else:
    print("Vücut kitle indeksiniz : {} Obezsiniz.".format(indeks))

""""""

#2 vize 1 final notu ile ağırlıkları hesaplanarak harf notu bulma

vize1 = int(input("Vize 1'in notunu giriniz :"))
vize2 = int(input("Vize 2'nin notunu giriniz:"))
final = int(input("Final notunu giriniz:"))
toplamnot = (vize1*30/100)+(vize2*30/100)+(final*40/100)

if toplamnot >= 90 :
    print("Sınavlarınızın ortalaması {}, harf notunuz AA.".format(toplamnot))
elif toplamnot >= 85:
    print("Sınavlarınızın ortalaması {}, harf notunuz BA.".format(toplamnot))
elif toplamnot >= 80:
    print("Sınavlarınızın ortalaması {}, harf notunuz BB.".format(toplamnot))
elif toplamnot >= 75:
    print("Sınavlarınızın ortalaması {}, harf notunuz CB.".format(toplamnot))
elif toplamnot >= 70:
    print("Sınavlarınızın ortalaması {}, harf notunuz CC.".format(toplamnot))
elif toplamnot >= 65:
    print("Sınavlarınızın ortalaması {}, harf notunuz DC.".format(toplamnot))
elif toplamnot >= 60:
    print("Sınavlarınızın ortalaması {}, harf notunuz DD.".format(toplamnot))
elif toplamnot >= 55:
    print("Sınavlarınızın ortalaması {}, harf notunuz FD.".format(toplamnot))
elif toplamnot < 55:
    print("Sınavlarınızın ortalaması {}, harf notunuz FF.".format(toplamnot))

""""""""""""    
#geometrik şekil tahmin etme

kenar = input("Bulmak istediğiniz geometrik yapı üç kenarlı mı dört kenarlı mı?")


if  kenar == "3" or kenar == "üç":
    x = float(input("İlk kenarı giriniz:"))
    y = float(input("İkinci kenarı giriniz:"))
    z = float(input("Son kenarı giriniz:"))
    if abs(x-y)<z<x+y and abs(x-z)<y<x+z and abs(y-z)<x<y+z and x != y != z:
        print("Sıradan bir üçgene sahipsiniz...")
    elif abs(x-y)<z<x+y and abs(x-z)<y<x+z and abs(y-z)<x<y+z and x == y != z:
        print("İkizkenar bir üçgene sahipsiniz...")
    elif abs(x-y)<z<x+y and abs(x-z)<y<x+z and abs(y-z)<x<y+z and x != y == z:
        print("İkizkenar bir üçgene sahipsiniz...")
    elif abs(x-y)<z<x+y and abs(x-z)<y<x+z and abs(y-z)<x<y+z and x ==z != y:
        print("İkizkenar bir üçgene sahipsiniz...")
    elif abs(x-y)<z<x+y and abs(x-z)<y<x+z and abs(y-z)<x<y+z and x == z == y:
        print("Eşkenar bir üçgene sahipsiniz...")
    else:
        print("Girilen değerler üçgen belirtmiyor...")

elif kenar == "4" or kenar == "dört":
    x = float(input("İlk kenarı giriniz:"))
    y = float(input("İkinci kenarı giriniz:"))
    z = float(input("Üçüncü kenarı giriniz:"))
    q = float(input("Son kenarı giriniz:"))
    if x == y == z == q :
        print("Bir kareye sahipsiniz...")
    elif x == y and z== q :
        print("Bir dikdörtgene sahipsiniz...")
    elif x == z and y == q :
        print("Bir dikdörtgene sahipsiniz...")
    elif x == q and y == z :
        print("Bir dikdörtgene sahipsiniz...")
    else:
        print("Sıradan bir dörtgene sahipsiniz...")

else:
    print("Doğru komut girmediniz...")

""""""""
#while döngüsü ile kullanıcı  giriş algoritması (3 giriş hakkı ile)


kullaniciadi = "3424dsdsfdf"
parola = "sdasd12323"
girissayisi = 3

while True:
    username = input("Kullanıcı adınızı giriniz...")
    pasword = input("Parolanızı giriniz...")
    if (kullaniciadi != username and parola == pasword):
        girissayisi -=1
        print("Kullanıcı adı veya parola hatalı...")
    elif (kullaniciadi == username and parola != pasword):
        girissayisi -=1
        print("Kullanıcı adı veya parola hatalı...")
    elif (kullaniciadi != username and parola != pasword):
        girissayisi -=1
        print("Kullanıcı adı veya parola hatalı...")
    else:
        print("Sisteme hoşgeldiniz...")
        break
    if (girissayisi == 0):
        print("Sisteme giriş hakkınız kalmadı...")
        break

"""""
#while içinde while ile Atm programı

 #print("""#********** Hoşgeldiniz **********

#İşlemler:

#1. Bakiye Sorgulama

#2. Para Yatırma

#3. Para Çekme

#Programı kapatmak için 'q' ya basınız...

""")

bakiye = int(1000)

while True:
    islem = input("Yapmak istediğiniz işlemin numarasını giriniz...")

    if (islem == "q"):
        print("Programdan çıktınız. İyi günler...")
        break
    if (islem == "1"):
        print("Bakiyeniz :", bakiye)
    elif (islem == "2"):
        yatirilan_para = int(input("Yatırmak istediğiniz parayı miktarını giriniz..."))
        bakiye += yatirilan_para
        print("Bakiyeniz: ", bakiye)
    elif (islem == "3"):
        while True:
           cekilen_para = int(input("Çekmek istediğiniz para miktarını giriniz..."))
           if (cekilen_para > bakiye):
               print("Bakiyenizden {} miktar fazla para istediniz, çekebileceğiniz para miktarına uygun miktar giriniz...".format(abs(bakiye-cekilen_para)))
               break
           else:
               bakiye -=cekilen_para
               print("Kalan bakiyeniz:",bakiye)

    else:
        print("Yanlış işlem seçeneği girdiniz...")

"""""
"""
# kullancıdan alınan iki sayının EBOB unu bulma

ilk = int(input("İlk sayi:"))
iki = int(input("İkinci sayi:"))
ebob = []
if ilk > iki:
    for i in range(1,iki+1):
        if ilk % i == 0 and iki % i == 0:
            ebob.append(i)
    print(ebob[-1])
elif iki > ilk:
    for i in range(1,ilk+1):
        if ilk % i == 0 and iki % i == 0:
            ebob.append(i)
    print(ebob[-1])
else:
    print("ebob:", ilk)

"""""""

#Kullanıcıdan alınan  bir sayının Armstrong sayısı olup olmadığını bulmak

sayi = input("Hangi sayının Armstrong sayısı olup olmadığını bulmak istiyorsunuz ? ")
basamak_sayisi= len(sayi)
basamak_sayisi_ilk= basamak_sayisi = len(sayi)
sayi2 = int(sayi)
kalan_listesi = []
kalan = 0
sonuc = 0

while sayi2 > 0:
    kalan = (sayi2 // (10**(int(basamak_sayisi)-1)))
    kalan_listesi.append(kalan)
    sayi2 -= (kalan * (10**(int(basamak_sayisi)-1)))
    basamak_sayisi -= 1
    kalan = 0


for toplam in kalan_listesi:
    sonuc += (toplam**basamak_sayisi_ilk)

if sonuc == int(sayi):
    print("Sayınız bir Armstrong sayısıdır...")
else:
    print("Sayınız bir Armstrong sayısı değildir...")

""""""

# input değerinin asal sayı olup olmadığını öğrenme (while)

sayi = int(input("Değeri giriniz:"))
bolenler = []
i= 2

if sayi>1:
    while i<=sayi:
        if sayi % i ==0:
            bolenler.append(i)
            i += 1
        else:
            i+=1
    if len(bolenler)== 1:
        print(sayi,"Asal sayıdır.")
    else:
        print(sayi,"Asal değildir.")
else:
    print("Geçersiz sayı girdiniz...")



""""""
#Kullanıcıdan alınan bir sayının Armstrong sayısı olup olmadığını bulmak EN KISA YÖNTEM İLE

sayi = input("Hangi sayının Armstrong sayısı olup olmadığını bulmak istiyorsunuz ? ")
basamak_sayisi = len(sayi)
rakamlar = []
sonuc = 0
for rakam in sayi:
    rakamlar.append(int(rakam))
for toplanılanlar in rakamlar:
    sonuc += (toplanılanlar **(basamak_sayisi))
if sonuc == int(sayi):
    print("Sayınız bir Armstrong sayısıdır...")
else:
    print("Sayınız bir Armstrong sayısı değildir...")

"""
#Geliştirilmiş hesap makinesi(While True kullanarak sonuç ile de işlem yapabilen ve sonuç sıfırlanabilinen


print("****Hesap Makinesi****\n 1.Toplama İşlemi \n 2.Çıkartma işlemi\n 3.Çarpma İşlemi\n 4.Bölme İşlemi\n '5' Çıkmak için kullanın")



while True:
    sayi1 = float(input("İlk sayiyi girin..."))
    sayi2 = float(input("Diğer sayiyi girin..."))
    islem = int(input("Kaç numaralı işlem yapmak istiyorsunuz ? "))
    sonuc= 0
    if islem == 1:
        print("Sonuc :",sayi1+sayi2  )
        sonuc = sayi1 + sayi2
        while True:
            cevap = input(" Sonuca göre islem yapmak istiyorsanız 'e' Hayır ise 'h' tuşunu giriniz...")
            if cevap == "h":
                break
            elif cevap == "e":
                sayi3 = float(input("Diğer sayıyı giriniz: "))
                islem2 = int(input("Kaç numaralı işlemi yapmak istiyorsunuz: "))
                if islem2 == 1:
                    print("Sonuç :" , sonuc+sayi3 )
                    sonuc += sayi3
                elif islem2 == 2:
                    print( "Sonuc :" , sonuc-sayi3 )
                    sonuc -= sayi3
                elif islem2 == 3:
                    print("Sonuç :" , sonuc*sayi3 )
                    sonuc *= sayi3
                elif islem2 ==4:
                    sonuc /= sayi3
                else:
                    print("Geçersiz komut girdiniz...")
                    continue
            else:
                print("Yanlış değer girdiniz...")
                continue
    elif islem == 2:
        print("Sonuc :" , sayi1-sayi2 )
        sonuc = sayi1 - sayi2
        while True:
            cevap = input(" Sonuca göre islem yapmak istiyorsanız 'e' Hayır ise 'h' tuşunu giriniz...")
            if cevap == "h":
                break
            elif cevap == "e":
                sayi3 = float(input("Diğer sayıyı giriniz: "))
                islem2 = int(input("Kaç numaralı işlemi yapmak istiyorsunuz: "))
                if islem2 == 1:
                    print("Sonuc :" , sonuc+sayi3 )
                    sonuc += sayi3
                elif islem2 == 2:
                    print("Sonuc :" , sonuc-sayi3 )
                    sonuc -= sayi3
                elif islem2 == 3:
                    print("Sonuç :" , sonuc*sayi3)
                    sonuc *= sayi3
                elif islem2 == 4:
                    print("Sonuc :" , sonuc/sayi3)
                    sonuc /= sayi3
                else:
                    print("Geçersiz komut girdiniz...")
                    continue
            else:
                print("Geçersiz komut girdiniz...")
                continue
    elif islem == 3:
         print("Sonuç :" , sayi1*sayi2)
         sonuc = sayi1*sayi2
         while True:
            cevap = input(" Sonuca göre islem yapmak istiyorsanız 'e' Hayır ise 'h' tuşunu giriniz...")
            if cevap == "h":
                 break
            elif cevap == "e":
                sayi3 = float(input("Diğer sayıyı giriniz: "))
                islem2 = int(input("Kaç numaralı işlemi yapmak istiyorsunuz: "))
                if islem2 == 1:
                    print("Sonuc : ", sonuc+sayi3)
                    sonuc+= sayi3
                elif islem2 ==2:
                    print("Sonuc :" , sonuc - sayi3)
                    sonuc -= sayi3
                elif islem2 ==3:
                    print("Sonuç :" , sonuc*sayi3)
                    sonuc *= sayi3
                elif islem2 ==4:
                    print("Sonuc :" , sonuc/sayi3)
                    sonuc /=sayi3
                else:
                    print("Geçersiz komut girdiniz...")
                    continue
            else:
                print("Geçersiz komut girdiniz...")
                continue
    elif islem == 4:
        print("Sonuç :" , sayi1/sayi2)
        sonuc = sayi1/sayi2
        while True:
            cevap = input(" Sonuca göre islem yapmak istiyorsanız 'e' Hayır ise 'h' tuşunu giriniz...")
            if cevap == "h":
                break
            elif cevap == "e":
                sayi3 = float(input("Diğer sayıyı giriniz: "))
                islem2 = int(input("Kaç numaralı işlemi yapmak istiyorsunuz: "))
                if islem2 ==1:
                    print("Sonuc : ", sonuc+sayi3)
                    sonuc += sayi3
                elif islem2 == 2:
                    print("Sonuc : ", sonuc-sayi3)
                    sonuc -= sayi3
                elif islem2 == 3:
                    print("Sonuc : ", sonuc*sayi3)
                    sonuc *= sayi3
                elif islem2 ==4:
                    print("Sonuc : ", sonuc/sayi3)
                    sonuc /= sayi3
                else:
                    print("Geçersiz komut girdiniz...")
                    continue
            else:
                print("Geçersiz komut girdiniz...")
                continue
    elif islem == 5:
        print("Güle güle")
        break
    else:
        print("Geçersiz komut girdiniz")
        continue

