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

nimi = ["ALIKA – “Bridges”", "Anett x Fredi – “Read Between The Lines”", "Villemdrillem – “leekiv armastus”", "Clicherik & Mäx – “PAKSUD”", "Nublu – “ära ärata”", "NOËP – “Move Your Feet”", "Trad.Attack! – “Bring It On”", "Bedwetters – “It Is What It Is”", "Reket – “Panama paberid”", "Grete Paia – “Võluväel”"]

#for i in nimi:   # ilma numbriteta loend
#    print(i)
    
for i in range(10):      # loome listi
    print(f"{i+1}. {nimi[i]}")
    
valik = int(input("Vali lugu (1-10): "))   # küsime, mis lugu soovib ja kuvame mängitava loo
print(f"Mängin: {nimi[valik-1]}") #blabla