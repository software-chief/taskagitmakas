#Powered by Hasan Basri Azder
#Twitter @hsnbsrpy
import random
Secenekler = ["TAŞ", "KAĞIT", "MAKAS"]
while True:
    Bot1 = random.choice(Secenekler)
    Bot2 = random.choice(Secenekler)
    Bot3 = random.choice(Secenekler)
    Liste = [Bot1, Bot2, Bot3]
    #Yukarıda bir liste oluşturuluyor. Daha sonrasında, Botlar listedeki değerleri rastgele değiştiriyor.
    #Sonra ise biz liste'de değişenlere göre oyunda 2 veya 3 tane alırsak kazanıyoruz.
    Liste2 = [" ", " ", " "]
    Liste3 = [" ", " ", " "]
    print(" ")
    print('Tek seferde 3 değer alıyoruz. Çıkmak için "çık" yazınız...')
    print("3 Bot'a karşı sen! Hadi göster gücünü!")

    Soru1 = input("1. sırada hangisi savaşsın?: ").upper() #Burada upper() kullanıldı. Liste içerisindekilerin hepsi büyük.
    Liste2[0] = Soru1
    if Soru1 == "ÇIK":
        print("Çıkılıyor...")
        break
    Soru2 = input("2. Sırada hangisi olsun? (Aynı olabilir, bot acımayacak!): ").upper()
    Liste2[1] = Soru2
    if Soru2 == "ÇIK":
        print("Çıkılıyor...")
        break
    Soru3 = input("3. Sırada hangisi olsun? (Aynı olabilir, bot acımayacak!): ").upper()
    Liste2[2] = Soru3
    if Soru3 == "ÇIK":
        print("Çıkılıyor...")
        break
    """print(" ")
    print("Senin listen: ", Liste2)
    print("             vs")
    print("Botlar: ", Liste)"""
    #Bot1 / Raunt3
    if Liste2[0] == Liste[0]:
        Raunt1 = "BERABERE"
        Liste3[0] = Raunt1
    elif Liste2[0] == "TAŞ" and Liste[0] == "KAĞIT":
        Raunt1 = "KAYBETTİNİZ"
        Liste3[0] = Raunt1
    elif Liste2[0] == "KAĞIT" and Liste[0] == "MAKAS":
        Raunt1 = "KAYBETTİNİZ"
        Liste3[0] = Raunt1
    elif Liste2[0] == "MAKAS" and Liste[0] == "TAŞ":
        Raunt1 = "KAYBETTİNİZ"
        Liste3[0] = Raunt1
    elif Liste2[0] == "KAĞIT" and Liste[0] == "TAŞ":
        Raunt1 = "KAZANDINIZ!"
        Liste3[0] = Raunt1
    elif Liste2[0] == "MAKAS" and Liste[0] == "KAĞIT":
        Raunt1 = "KAZANDINIZ!"
        Liste3[0] = Raunt1
    elif Liste2[0] == "TAŞ" and Liste[0] == "MAKAS":
        Raunt1 = "KAZANDINIZ!"
        Liste3[0] = Raunt1
    #Bot2 / Raunt3
    if Liste2[1] == Liste[1]:
        Raunt2 = "BERABERE"
        Liste3[1] = Raunt2
    elif Liste2[1] == "TAŞ" and Liste[1] == "KAĞIT":
        Raunt2 = "KAYBETTİNİZ"
        Liste3[1] = Raunt2
    elif Liste2[1] == "KAĞIT" and Liste[1] == "MAKAS":
        Raunt2 = "KAYBETTİNİZ"
        Liste3[1] = Raunt2
    elif Liste2[1] == "MAKAS" and Liste[1] == "TAŞ":
        Raunt2 = "KAYBETTİNİZ"
        Liste3[1] = Raunt2
    elif Liste2[1] == "KAĞIT" and Liste[1] == "TAŞ":
        Raunt2 = "KAZANDINIZ!"
        Liste3[1] = Raunt2
    elif Liste2[1] == "MAKAS" and Liste[1] == "KAĞIT":
        Raunt2 = "KAZANDINIZ!"
        Liste3[1] = Raunt2
    elif Liste2[1] == "TAŞ" and Liste[1] == "MAKAS":
        Raunt2 = "KAZANDINIZ!"
        Liste3[1] = Raunt2
    #Bot3 / Raunt3
    if Liste2[2] == Liste[2]:
        Raunt3 = "BERABERE"
        Liste3[2] = Raunt3
    elif Liste2[2] == "TAŞ" and Liste[2] == "KAĞIT":
        Raunt3 = "KAYBETTİNİZ"
        Liste3[2] = Raunt3
    elif Liste2[2] == "KAĞIT" and Liste[2] == "MAKAS":
        Raunt3 = "KAYBETTİNİZ"
        Liste3[2] = Raunt3
    elif Liste2[2] == "MAKAS" and Liste[2] == "TAŞ":
        Raunt3 = "KAYBETTİNİZ"
        Liste3[2] = Raunt3
    elif Liste2[2] == "KAĞIT" and Liste[2] == "TAŞ":
        Raunt3 = "KAZANDINIZ!"
        Liste3[2] = Raunt3
    elif Liste2[2] == "MAKAS" and Liste[2] == "KAĞIT":
        Raunt3 = "KAZANDINIZ!"
        Liste3[2] = Raunt3
    elif Liste2[2] == "TAŞ" and Liste[2] == "MAKAS":
        Raunt3 = "KAZANDINIZ!"
        Liste3[2] = Raunt3

    print("Siz: ", Liste2)
    print("Botlar: ", Liste)
    print("Sonuç: ", Liste3)












































