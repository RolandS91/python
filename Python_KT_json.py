import requests
from datetime import datetime

# JSON andmete lugemine URL-ist
def loe_json_urlist(url):
    vastus = requests.get(url)
    if vastus.status_code == 200:
        return vastus.json()
    else:
        print("❌ Viga andmete lugemisel:", vastus.status_code)
        return None

# Massaaži broneeringute koguarv
def loenda_massaaz(broneeringud):
    count = sum(1 for br in broneeringud if br['teenus'].lower() == "massaaž")
    print(f"💆 Massaaži broneeringuid kokku: {count}")

# Broneeringud pärast kella 12:00
def broneeringud_peale_12(broneeringud):
    print("\n⏰ Broneeringud pärast kella 12:00:")
    for br in broneeringud:
        aeg = datetime.strptime(br['aeg'], "%H:%M")
        if aeg.hour >= 12:
            print(f"- {br['kuupäev']} {br['aeg']} | {br['klient']} | {br['teenus']}")

# Kliendid, kelle broneering on nädalavahetusel
def naedalavahetuse_kliendid(broneeringud):
    print("\n📅 Kliendid nädalavahetuse broneeringutega:")
    kliendid = set()
    for br in broneeringud:
        paev = datetime.strptime(br['kuupäev'], "%Y-%m-%d").weekday()
        if paev in [5, 6]:  # 5 = laupäev, 6 = pühapäev
            kliendid.add(br['klient'])
    for nimi in sorted(kliendid):
        print("-", nimi)

# Päev, millel on kõige rohkem broneeringuid
def enim_broneeringuid_paev(broneeringud):
    päevad = {}
    for br in broneeringud:
        kp = br['kuupäev']
        päevad[kp] = päevad.get(kp, 0) + 1
    max_päev = max(päevad, key=päevad.get)
    print(f"\n📈 Kõige rohkem broneeringuid on kuupäeval {max_päev} ({päevad[max_päev]} broneeringut)")

# Unikaalsed teenused ja nende arvud
def teenuste_statistika(broneeringud):
    print("\n📊 Teenuste broneerimise statistika:")
    teenused = {}
    for br in broneeringud:
        teenus = br['teenus']
        teenused[teenus] = teenused.get(teenus, 0) + 1
    for teenus, arv in sorted(teenused.items()):
        print(f"- {teenus}: {arv} broneeringut")

# Peaprogramm
def main():
    url = "https://metshein.com/kordamine/json/broneeringud.json"
    andmed = loe_json_urlist(url)

    if andmed and "broneeringud" in andmed:
        broneeringud = andmed["broneeringud"]
        loenda_massaaz(broneeringud)
        broneeringud_peale_12(broneeringud)
        naedalavahetuse_kliendid(broneeringud)
        enim_broneeringuid_paev(broneeringud)
        teenuste_statistika(broneeringud)
    else:
        print("⚠️ JSON struktuur vigane või tühi.")

if __name__ == "__main__":
    main()