# Ülesanne 7
# Sobols
# 19.12.2024


# 1. ALIKA – “Bridges”
# 2. Anett x Fredi – “Read Between The Lines”
# 3. villemdrillem – “leekiv armastus”
# 4. Clicherik & Mäx – “PAKSUD”
# 5. nublu – “ära ärata”
# 6. NOËP – “Move Your Feet”
# 7. Trad.Attack! – “Bring It On”
# 8. Bedwetters – “It Is What It Is”
# 9. Reket – “Panama paberid”
# 10. Grete Paia – “Võluväel”

#nimi = ["ALIKA – “Bridges”", "Anett x Fredi – “Read Between The Lines”", "Villemdrillem – “leekiv armastus”", "Clicherik & Mäx – “PAKSUD”", "Nublu – “ära ärata”", "NOËP – “Move Your Feet”", "Trad.Attack! – “Bring It On”", "Bedwetters – “It Is What It Is”", "Reket – “Panama paberid”", "Grete Paia – “Võluväel”"]

#for i in nimi:   # ilma numbriteta loend
#    print(i)
    
#for i in range(10):      # loome listi
#    print(f"{i+1}. {nimi[i]}")
    
#valik = int(input("Vali lugu (1-10): "))   # küsime, mis lugu soovib ja kuvame mängitava loo
#print(f"Mängin: {nimi[valik-1]}") #blabla

# “jaanuar”,-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3
# Kuva mõõdetava kuu nimetus
# Kuva viimase mõõtmise tulemus
# Kuva ainult temperatuurid
# Leia kuu maksimaalne ja minimaalne temperatuur
# Leia kuu keskmine temperatuur
# Mitu korda esines -20 kraadi
# Eemalda element nr 5
# Lisa 5. elemendi kohale temperatuur, mis on sinu vanus
# Sorteeri temperatuurid nimekirjas kasvavas järjekorras

jtemp = ["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]

print(f"Mõõdetav kuu: {jtemp[0]}")
print(f"Viimane mõõtmise tulemus: {jtemp[-1]} kraadi")

maks = -100
mini = 100
summa = 0
kokku = 0
kordused = 0

for t in range(1,len(jtemp)):
    print(jtemp[t], end=" ")    # Prindi kõik temperatuurid
    if jtemp[t]>maks:           # max temp kontroll
        maks = jtemp[t]         
    if jtemp[t]<mini:           # min temp kontroll
        mini = jtemp[t]
    summa+=jtemp[t]
    kokku+=1
    if jtemp[t]== -20:
        kordused+=1

jtemp.pop(5)            # Kustutab viienda
jtemp.insert(5,33)      # Lisab viienda
# jtemp.sort()          # Sorteerib

print()
print(f"Maksimum temperatuur on: {maks} kraadi")
print(f"Miinimum temperatuur on: {mini} kraadi")
print(f"Keskmine temperatuur on: {summa/kokku:0.0f}")
print(f"-20 esineb: {kordused} korda")
print(jtemp)