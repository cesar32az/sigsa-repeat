import json

f = open("app/data/pacientes.json", )
data = json.load(f)
f.close()
pacientes = data["pacientes"]

dias = [1, 2, 3, 4, 7, 8, 9, 10, 11, 12]

suple = [
    {
        "nombre": "ferro",
        "presentacion": "tableta",
        "concentracion": "300",
        "cantidad": "12",
    },
    {
        "nombre": "foli",
        "presentacion": "tableta",
        "concentracion": "5",
        "cantidad": "12",
    },
]
