class Paciente:
    def __init__(self, paciente):
        self.nombres = paciente["nombres"]
        self.apellidos = paciente["apellidos"]
        self.cie = paciente["cie"]

    def get_full_nombres(self):
        return list(filter(lambda x: x, self.nombres.split(" ")))

    def get_full_apellidos(self):
        return list(filter(lambda x: x, self.apellidos.split(" ")))

    @property
    def primer_nombre(self):
        return self.get_full_nombres()[0]

    @property
    def segundo_nombre(self):
        full_names = self.get_full_nombres()
        if len(full_names) > 1:
            segundo_nombre = full_names[-1]
        else:
            segundo_nombre = ""
        return segundo_nombre

    @property
    def primer_apellido(self):
        return self.get_full_apellidos()[0]

    @property
    def segundo_apellido(self):
        full_apellidos = self.get_full_apellidos()
        if len(full_apellidos) > 1:
            segundo_apellido = full_apellidos[-1]
        else:
            segundo_apellido = ""
        return segundo_apellido

    def __str__(self) -> str:
        return f"{self.primer_nombre} {self.segundo_nombre}, {self.primer_apellido} {self.segundo_apellido} - {self.cie}"

