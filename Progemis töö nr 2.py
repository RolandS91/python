# Prog töö 2
# Sobols
# 04.02.2025

# Pangakonto

def pangakonto(algne_saldo, toiming, summa):
    if toiming == "deposiit":
        algne_saldo += summa
    elif toiming == "valjavote":
        if summa > algne_saldo:
            return "Viga: Ebapiisav saldo"
        algne_saldo -= summa
    else:
        return "Viga: Tundmatu toiming"
    
    return algne_saldo

# Näidis kasutamine

#saldo = 100
#saldo = pangakonto(saldo, "deposiit", 50)
#print(f"Saldo on: {saldo}")
#saldo = pangakonto(saldo, "valjavote", 20)
#print(f"Saldo on: {saldo}")

saldo = 100
tehing = input("Vali tehing: raha sisse või raha välja: ")

if tehing == "raha sisse":
    summa = int(input("Sisesta summa: "))
    saldo = pangakonto(saldo, "deposiit", summa)
    print(saldo)
elif tehing == "raha välja":
    summa = int(input("Sisesta summa: "))
    saldo = pangakonto(saldo, "valjavote", summa)
    print(saldo)
else:
    print("Viga: tundmatu tehing")