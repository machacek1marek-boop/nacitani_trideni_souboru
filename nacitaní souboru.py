<<<<<<< Updated upstream
# prece se souborem
soubor = open('seznam_mest2.txt','r',encoding='utf-8')

nacteny_radek = []
for radek_souboru in soubor:
    nacteny_radek.append(radek_souboru[:])
soubor.close()

print(nacteny_radek)

mesto = []
for i, radek in enumerate(nacteny_radek):
    # prvni radek v kazde trojici
    if (i + 1) % 3 == 1:
        nazev_mesta = radek.strip().split('\t')[1]
    # druhy radek v kazde trojici
    elif (i + 1) % 3 == 2:
        pass # nedela se nic (prazdny radek)
    # treti radek v kazde trojici 
    else:
        nazev_okresu = radek.strip().split('\t')[2].split()[1]
        print('město:',nazev_mesta,',','okres:',nazev_okresu)
print("KONEC")