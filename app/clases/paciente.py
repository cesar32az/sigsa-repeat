class Paciente:
    def __init__(self, paciente):
        self.primer_nombre = paciente["primer_nombre"]
        self.segundo_nombre = paciente["segundo_nombre"]
        self.primer_apellido = paciente["primer_apellido"]
        self.segundo_apellido = paciente["segundo_apellido"]

    def __str__(self) -> str:
        return f"{self.primer_nombre} {self.segundo_nombre}, {self.primer_apellido} {self.segundo_apellido}"
