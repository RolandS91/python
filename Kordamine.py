# Kordamine
# Sobols
# 30.01.2025



# 1.1 Tervitus
# Koostada programm, mis väljastaks ekraanile teksti Tere, maailm! täpselt sellisel kujul - koma ja hüüumärgiga.

# print(f"Tere, maailm!")



# 1.2 Aasta liblikas
# Koostada programm, mille
# 1. real luuakse muutuja nimega aasta ning antakse sellele väärtuseks 2020 (arvuna);
# 2. real luuakse muutuja nimega liblikas ning antakse sellele väärtuseks "teelehe-mosaiikliblikas" (sõnena);
# 3. real luuakse muutuja nimega lause_keskosa ning antakse sellele väärtuseks ". aasta liblikas on " (sõnena);
# 4. real luuakse muutuja nimega lause, mille väärtuse saamiseks ühendatakse üheks sõnaks muutujad aasta, lause_keskosa ja liblikas (vajadusel tuleb kasutada funktsiooni, mis teisendab arvu sõneks);
# 5. real väljastatakse muutuja lause väärtus ekraanile.

# aasta = 2020
# liblikas = "teelehe-mosaiikliblikas"
# lause_keskosa = ". aasta liblikas on "
# lause = (f"{aasta}{lause_keskosa}{liblikas}")
# print(lause)



# 1.3. Pilved
# Pilvede alumise pinna (aluse) kõrguse järgi liigitatakse pilvi ülemise, keskmise ja alumise kihi pilvedeks. 
# Ülemiste pilvede alus on kõrgemal kui 6 km, keskmistel pilvedel on 2-6 km kõrgusel, alumistel pilvedel on madalamal kui 2 km. 
# Koostada programm, mis
# küsib kasutajalt pilvede aluse kõrgust (kilomeetrites),
# väljastab ekraanile Need on ülemised pilved, kui sisestatu on üle 6,0 km,
# väljastab Need ei ole ülemised pilved, kui kõrgus on 6,0 km või alla selle.
# Kasutaja peab saama sisestada pilvede kõrgust nii täisarvuna kui ka ujukomaarvuna, nt 7.5.

# korgus = float(input("Sisesta pilvede kõrgus: "))

# if korgus > 6:
#     print("Need on ülemised pilved.")
# elif korgus >= 2 and korgus <= 6:
#     print("Need on keskmised pilved.")
# else:
#     print("Need on alumised pilved.")



# 1.4. Bussid
# Meil on vaja transportida teatud arv inimesi mingi arvu identsete bussidega. Eeldame, et reisijaid on vähemalt üks. 
# Koostada programm, mis küsib transporditavate inimeste arvu ja ühe bussi kohtade arvu (just sellises järjekorras) ning väljastab ekraanile, mitu bussi on vaja ja mitu inimest on viimases bussis (eeldusel, et kõik eelnevad bussid on täis).
# Võib-olla on abi nendest tehetest
# // täisarvuline jagamine, 36 // 10 → 3
# % jäägi leidmine 36 % 10 → 6
# Testige oma programmi muuhulgas järgmiste algandmetega:
# inimeste arv: 60, kohtade arv: 40;
# inimeste arv: 80, kohtade arv: 40;
# inimeste arv: 20, kohtade arv: 40;
# inimeste arv: 40, kohtade arv: 40.
# Püüdke ka mõista, miks just sellised testandmed valiti.

# import math

# inimesed = int(input("Inimeste arv: "))
# kohad = int(input("Kohtade arv: "))
# jaak = inimesed%kohad

# if jaak>0:
#     busside_arv = (inimesed//kohad)+1
# else:
#     busside_arv = inimesed//kohad
# if jaak == 0:
#     jaak = kohad

# print(f"Busside arv: {busside_arv}")
# print(f"Viimases bussis inimesi: {jaak}")

# busside_arv = math.ceil(inimesed/kohad)
# if inimesed <= kohad:
#     viimane_inim_arv = inimesed
# else:
#     viimane_inim_arv = abs(inimesed - kohad)

# print(f"Busside arv: {busside_arv}")
# print(f"Viimases bussis on inimesi: {viimane_inim_arv}")


# 2.1 ÄRATUS
# Otil on hommikuti raske tõusta ja tal on äratuskell, mis äratab teda teatud arv kordi koos tervitustekstiga.
# Koostada programm, mis:

# 1. küsib kasutajalt, mitu korda äratus heliseb ning
# 2. väljastab sama arv kordi ekraanile "Tõuse ja sära!"

# kordused = int(input("Sisesta korduste arv: "))

# for _ in range(kordused):
#     print(f"Tõuse ja sära!")



# 2.2 MURELIKUD LAPSEVANEMAD
# Jänesevanemad on mures, et lapsed ei liigu piisavalt. 
# Laste motiveerimiseks mõtlesid nad välja süsteemi, kus 2. metsaringi läbimisel saab jänesepoeg 2 porgandit, 4. metsaringi läbimisel 4 porgandit juurde, 6. metsaringi läbimisel 6 porgandit juurde jne. Paarituarvulistel ringidel porgandeid juurde ei saa. 

# Koostada programm, mis
# küsib kasutajalt ringide arvu (mittenegatiivne täisarv);
# arvutab while-tsükli abil saadavate porgandite koguarvu;
# väljastab saadavate porgandite koguarvu ekraanile.
# Näiteks, kui kasutaja sisestas 6, siis summa on 12, sest 2 + 4 + 6 = 12. 
# Kui kasutaja sisestas 7, siis on summa samuti 12, sest 2 + 4 + 6 = 12.


# ringide_arv = int(input("Sisesta ringide arv: "))
# porgandid = 0

# while ringide_arv > 0:
#     # print(ringide_arv)
#     if ringide_arv%2==0:
#         porgandid += ringide_arv
#     ringide_arv-=1

# print(f"Porgandite koguarv on: {porgandid}")


# 2.5 ÕUNAD
# Lumivalgekesel oli 14 õuna ja ta tahtis neid pöialpoistega jagada. 
# Ta sai aru, et kui kõik seitse pöialpoissi tahavad õunu ja ta annaks kõigile kaks õuna, jääks ta ise üldse ilma. 
# Nüüd otsustas ta õunu jagada nii, et küsib, mitu pöialpoissi tahab õunu, ja seejärel loosib iga soovija korral, kas anda talle üks või kaks õuna. 
# Koostada programm, mis

# küsib kasutajalt, mitu pöialpoissi tahab õunu (võib eeldada, et sisestatakse täisarv lõigust [0; 7]);
# leiab ja väljastab eraldi ridadele, mitu õuna saab iga pöialpoiss (programm genereerib iga kord juhuslikult arvu 1 või 2);
# leiab ja väljastab eraldi reale, mitu õuna jääb Lumivalgekesele.

# import random

# ounad = 14
# pp = int(input("Mitu PP tahab õuna: "))

# for i in range(pp):
#     oun = random.randint(1,2)
#     print(oun)
#     ounad -= oun
    
# print(f"Lumivalgekesele jäi: {ounad}")


# 3.4 Jukebox
# Ada tahab valida plaadiautomaadist laulu ja uurib, milliseid laule masin mängib. Muusikapalad on kirjas failis, kus iga laul on eraldi real.
# Programmi testimiseks kasutatakse järgmisi faile, mida võite salvestada või koostada ise mõne tekstiredaktoriga (nt Notepad):

# jukebox.txt
# 80ndad.txt
# eesti_muusika.txt 
# edm.txt


