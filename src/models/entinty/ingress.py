class IngressPatient():
    def __init__(self, medic_name, traitment, bed_number, diagnostic, level_sick):
        self.medic_name = medic_name
        self.traitment = traitment
        self.bed_number = bed_number
        self.diagnostic = diagnostic
        self.level_sick = level_sick
    
    def to_json(self):
        return {
            "Nombre del médico": self.medic_name,
            "Tratamiento": self.traitment,
            "Número de cama": self.bed_number,
            "Diagnóstico": self.diagnostic,
            "Nivel de gravedad": self.level_sick
        }