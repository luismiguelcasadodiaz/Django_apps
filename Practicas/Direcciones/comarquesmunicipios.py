import csv
municipis = {}
comarques = {}
comarquesProvincies = {}

f_municipis = open("municipis.csv","w", encoding="utf-8",newline='' )
spamwriter = csv.writer(f_municipis, delimiter=',', quoting=csv.QUOTE_ALL)
with open("Municipis_Catalunya_Geo.csv", "r", encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',',)
    for row in spamreader:
        spamwriter.writerow([row[0], row[1], row[2]])
        print(row)
        if row[2] not in comarques:
            comarques.setdefault(row[2], row[3])
        if row[1] not in municipis:
            municipis.setdefault(row[1], row[2])
        if row[2] not in comarquesProvincies:
            comarquesProvincies.setdefault(row[2], row[0][0:2])

#listacomarcas = listprint(sorted(comarquesProvincies, key=lambda x: x[0]))
# for c in sorted(comarquesProvincies, key=lambda x: x[0]):
#     print ("1")
#print(comarques)
# print(municipis)
lista_comarcas =comarques.items()
# print(sorted(lista_comarcas, key=lambda x: x[1]))
with open("comarques.csv", "w",encoding="utf-8") as f_comarcas:
    for e in sorted(lista_comarcas, key=lambda x: x[0]):
        if e[0] != "Codi comarca":
            f_comarcas.write(f"{e[0]},{e[1]}\n")
lista_comarcasProvincias = comarquesProvincies.items()
print(lista_comarcasProvincias)
with open("comarquesProvincias.csv", "w",encoding="utf-8") as f_comarcas:
    for e in sorted(lista_comarcasProvincias, key=lambda x: x[0]):
        if e[0] != "Codi comarca":
            f_comarcas.write(f"{e[0]},{e[1]}\n")
lista_municipis = municipis.items()
print(lista_municipis)
tot = 0
for c, m in lista_comarcas:
    tot += len(m)
    print(m, tot)