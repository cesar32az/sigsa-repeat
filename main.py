from time import time

from app.data.dicts import dias, pacientes
from app.data.paciente import Paciente
from app.scrap import buscar_paciente, cargar_pagina, ingresar_paciente


def main():
    cargar_pagina()

    for item in pacientes:
        paciente = Paciente(item)
        for dia in dias:
            print(f"Dia: {dia}, paciente: {paciente}")
            buscar_paciente(dia, paciente)
            ingresar_paciente(cie="z:20:8")


if __name__ == "__main__":
    start = time()
    main()
    print(f"Elapsed time: {round(time() - start, 4)} seconds.")
