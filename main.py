from time import time

from app.clases.paciente import Paciente
from app.data.dicts import dias, pacientes
from app.scrap import buscar_paciente, cargar_pagina, ingresar_paciente, suplementar


def main():
    user = "jrodriguez"
    password = "3124"
    responsable = "YESI CRISTINA BARRUTIA"
    mes = "6"
    cargar_pagina(user, password, responsable, mes)
    pacientes_ingresados = 0
    for paciente in pacientes:
        paciente = Paciente(paciente)
        for dia in dias: # dias   -    range(1, 3) -> 1, 2
            print(f"Dia: {dia}, paciente: {paciente}")
            buscar_paciente(dia, paciente)
            
            """ Opcion a suplementar o ingresar solo un diagnostico """
            #ingresar_paciente(cie=paciente.cie, ingresar=True)
            #suplementar(ingresar=False)
            pacientes_ingresados+=1
    print(f"Pacientes ingresados: {pacientes_ingresados}")


if __name__ == "__main__":
    start = time()
    main()
    print(f"Elapsed time: {round(time() - start, 4)} seconds.")
