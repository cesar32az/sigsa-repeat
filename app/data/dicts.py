pacientes = [
    {
        "primer_nombre": "julio",
        "segundo_nombre": "cesar",
        "primer_apellido": "rodriguez",
        "segundo_apellido": "orozco",
    },
]

dias = [1, 2, 3]

if __name__ == "__main__":
    for paciente in pacientes:
        print(paciente["primer_nombre"])

    for dia in dias:
        print(dia)