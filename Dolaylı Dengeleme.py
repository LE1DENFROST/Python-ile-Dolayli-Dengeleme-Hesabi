
import numpy as np
import math
import time
from blessed import Terminal

t = Terminal()

def matris_olustur():
    satir = int(input("Lütfen matrisin satır sayısını girin: "))
    sutun = int(input("Lütfen matrisin sütun sayısını girin: "))

    matris = np.zeros((satir, sutun))
    
    for i in range(satir):
        for j in range(sutun):
            matris[i, j] = float(input("Lütfen matrisin {}. satırının {}. sütununu girin: ".format(i+1, j+1)))
    print(t.clear + t.move(0,0) +"Matris Oluşturuluyor...")
    time.sleep(1)
    return matris


anahtar = 0
while True:
    try:
         OlcuSayisi = int(input("Dengelemeye Başlamadan Önce Kontrol İçin Ölçü Sayısını Giriniz ----> "))       
         BilinmeyenSayisi = int(input("Bilinmeyen Sayısını Giriniz ----> "))
         f = OlcuSayisi - BilinmeyenSayisi
         print(t.clear + t.move(0,0) +"Bilgiler İşleniyor...")
         time.sleep(2)
         print(t.clear + t.move(0,0) +"Serbestlik Derecesi Hesaplanıyor...")
         time.sleep(2)
         if f > 0:
            print(t.clear + t.move(0,0) +"Program Başlatılıyor.....")
            time.sleep(2)
            anahtar = 1
            break
         else:
            print(t.clear + t.move(0,0) +"Serbestlik Derecesi 0'dan küçük olduğundan Dengeleme Yapılamaz !")
            time.sleep(2)
            print(t.clear + t.move(0,0) +"Lütfen Değerleri Kontrol Ediniz...")
            time.sleep(2)
            print(t.clear, end="")
    except ValueError:
         print("Hatalı Giriş ! Lütfen Tekrar Deneyin.")
         time.sleep(1)

    
while anahtar == 1:
        print(t.clear, end="")
        print("############# DOLAYLI ÖLÇÜLER DENGELEMESİ Versiyon 1.0 EJDER ERDOGAN ############# ")
        print("...................................................................................")
        print(" A Matrisini Oluştur (1)   L Matrisini Oluştur (2)    P Matrisini Oluştur (3) \n A Matrisini Görüntüle (4) L Matrisini Görüntüle (5)  P Matrisini Görüntüle (6) \n N Matrisi Hesapla (7)     N Matrisini Görüntüle (8)  N*-1 Matrisini Görüntüle (9) \n n Matrisini Hesapla (10)  n Matrisini Görüntüle(11)  Kesin Değeri Hesapla (12) \n Kesin Değeri Görüntüle (13)")
        print("...............................................................................")
        print(".............................----[KOH HESABI]----.............................")
        print("")
        print(" V Matrisini Hesapla (14) V Matrisini Görüntüle (15) vTPv Hesapla (16) \n vTPv Görüntüle (17)      m0 Hesapla (18)            m0 Görüntüle (19)")
        print(" mX Hesapla (20)          nx Görüntüle (21)          mY Hesapla (22)    \n mY Görüntüle (23)        mZ Hesapla(24)             mZ Görüntüle (25) \n ATPv Kontrolü yap (26)   Programı Kapat (0)")
        print("")
        print("")
        
        while True:
            try:
                secenek = int(input("Yapmak İstediğiniz İşlem Numarasını Giriniz ---->  "))
                break
            except ValueError:
                print("Hatalı Giriş ! Lütfen Tekrar Deneyin.")
                time.sleep(1)
        
        if secenek ==1:
            a = matris_olustur()
            print(t.clear + t.move(0,0) +"Katsayılar Matrisi Oluşturuldu")
            time.sleep(2)
            at = a.T
        elif secenek == 2:
            l = matris_olustur()
            print(t.clear + t.move(0,0) +"Ölçü Vektörü Oluşturuldu")
            time.sleep(2)
        elif secenek == 3:
            p = matris_olustur()
            print(t.clear + t.move(0,0) +"Ağırlık Matrisi Oluşturuldu")
            time.sleep(2)
        elif secenek == 4: 
            print(a)
            time.sleep(2)
        elif secenek == 5:
            print(l)
            time.sleep(2)
        elif secenek == 6:
            print(p)
            time.sleep(2)
        elif secenek == 7:
            aTP = at.dot(p)
            n = aTP.dot(a)
            print("N Matrisi Oluşturuldu...")
            time.sleep(2)
        elif secenek == 8:
            print(n)
            time.sleep(2)    
        elif secenek == 9:
            n_eksi1 =  np.linalg.matrix_power(n, -1)  
            print(n_eksi1)
            time.sleep(2)   
        elif secenek ==10:
            aTPl = aTP.dot(l)
            print("n Matrisi Hesaplandı....")
            time.sleep(2)
        elif secenek ==11:
            print(aTPl)
            time.sleep(2)
        elif secenek == 12:
            x = n_eksi1.dot(aTPl)
            print("Kesin Değer Hesaplandı...")
            time.sleep(2)
        elif secenek == 13:
            print(x)    
            time.sleep(2)
        elif secenek == 14:
            v = a.dot(x) - l
            print("v Matrisi Hesaplandı...")
            time.sleep(2)
        elif secenek == 15:
            print(t.clear + t.move(0,0) +v)
        elif secenek == 16:
            vT = np.transpose(v)
            vTP = vT.dot(p)
            vTPv = vTP.dot(v)
            print("vTPv Hesaplandı...")
            time.sleep(2)
        elif secenek == 17:
            print(vTPv)
            time.sleep(2)
        elif secenek == 18:
            m0 = math.sqrt(vTPv / (OlcuSayisi - BilinmeyenSayisi))
            print("m0 hesaplandı")
            time.sleep(2)
        elif secenek == 19:
            print(m0)
            time.sleep(2)
        elif secenek == 20:
            qxx = n_eksi1[0,0]
            mX = m0 * math.sqrt(qxx)
            print("mX hesaplandı ...")
            time.sleep(2)
        elif secenek == 21:
            print(mX)
            time.sleep(2)
        elif secenek == 22:
            qyy = n_eksi1[1,1]
            mY = m0 * math.sqrt(qyy)  
            print("mY hesaplandı ...")
            time.sleep(2)
        elif secenek == 23:
            print(mY)
            time.sleep(2)
        elif secenek == 24:
            qzz = n_eksi1[2,2]
            mZ = m0 * math.sqrt(qzz)  
            print("mZ hesaplandı ...")
            time.sleep(2)
        elif secenek == 25:
            print("mZ")
            time.sleep(2)
        elif secenek == 26:
            aTPv = int(aTP.dot(v))
            if aTPv == 0:
                print(t.clear + t.move(0,0) +"aTPv Kontrolü Sağlanıyor...")
                time.sleep(2)
                print(t.clear + t.move(0,0) +"PASS")
                time.sleep(2)
            else:                
                print(t.clear + t.move(0,0) +"aTPv Kontrolü Sağlanıyor...")
                time.sleep(2)
                print(t.clear + t.move(0,0) +"ERROR")
                time.sleep(2)
        elif secenek == 0:
            print(t.clear + t.move(0,0) +"Program Kapatılıyor...")
            time.sleep(2)
            anahtar = 0        