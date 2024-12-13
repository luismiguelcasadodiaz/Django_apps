import csv
secciones = {}
subsecciones = {}
divisiones = {}
grupos = {}
clases = {}
subclases = {}

secciones_c = 0
subsecciones_c = 0
divisiones_c = 0
grupos_c = 0
clases_C = 0
subclases_c = 0

seccion_actual = ""
subseccion_actual = ""
division_actual = ""
grupo_actual = ""
clase_actual = ""
subclase_actual = ""



with open("ccae-93-rev1-ca.csv", "r", encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        print(row)
        if row[0] == "Secciones":
            secciones.setdefault(row[1],row[2])
            secciones_c += 1
            seccion_actual =  row[1]

        if row[0] == "Subsecciones":
            subsecciones.setdefault(row[1],(row[2], seccion_actual))
            subsecciones_c += 1
            subseccion_actual =  row[1]

        if row[0] == "Divisiones":
            divisiones.setdefault(row[1],(row[2], subseccion_actual))
            divisiones_c += 1
            division_actual = row[1]

        if row[0] == "Grupos":
            grupos.setdefault(row[1],(row[2], division_actual))
            grupos_c += 1
            grupo_actual =  row[1]

        if row[0] == "Clases":
            clases.setdefault(row[1],(row[2], grupo_actual))
            clases_C += 1
            clase_actual =  row[1]

        if row[0] == "Subclases":
            subclases.setdefault(row[1],(row[2], clase_actual))
            subclases_c += 1
            subclase_actual =  row[1]

print(f"Total lineas {secciones_c + subsecciones_c + divisiones_c + grupos_c + clases_C+ subclases_c}")
            

lista_secciones = list(sorted(secciones.items()))
with open("secciones.csv", "w", encoding="utf-8") as resultado:
    for i, e in enumerate(lista_secciones):
        resultado.write(f"{i},{e[0]},\"{e[1]}\"\n")

lista = list(subsecciones.items())
with open("subsecciones.csv", "w", encoding="utf-8") as resultado:
    for i, e in enumerate(lista):
        resultado.write(f"{i},{e[0]},\"{e[1][0]}\",{e[1][1]}\n")

lista = list(divisiones.items())
with open("divisiones.csv", "w", encoding="utf-8") as resultado:
    for i, e in enumerate(lista):
        resultado.write(f"{i},{e[0]},\"{e[1][0]}\",{e[1][1]}\n")

lista_grupos = list(sorted(grupos.items()))
with open("grupos.csv", "w", encoding="utf-8") as resultado:
    for i, e in enumerate(lista_grupos):
        resultado.write(f"{i},{e[0]},{e[1][0]},{e[1][1]}\n")

lista = list(clases.items())
with open("clases.csv", "w", encoding="utf-8") as resultado:
    for i, e in enumerate(lista):
        resultado.write(f"{i},{e[0]},\"{e[1][0]}\",{e[1][1]}\n")

lista = list(subclases.items())
with open("subclases.csv", "w", encoding="utf-8") as resultado:
    for i, e in enumerate(lista):
        resultado.write(f"{i},{e[0]},\"{e[1][0]}\",{e[1][1]}\n")