from utils.DateFormat import DateFormat

class Patient():

    def __init__(self, full_name, id, age, gender, corporal_temp, discomfort, date, eps, type_id = None):
        self.full_name = full_name
        self.id = id
        self.age = age
        self.gender = gender
        self.corporal_temp = corporal_temp
        self.discomfort = discomfort
        self.date = date
        self.eps = eps
        self.type_id = type_id

    def to_json(self):
        return {
            "Nombre": self.full_name,
            "No. id": self.id,
            "Edad": self.age,
            "Género": self.gender,
            "Temperatura corporal": self.corporal_temp,
            "Malestar": self.discomfort,
            "Fecha de ingreso": DateFormat.convert_date(self.date),
            "eps": self.eps,
            "Tipo de documento": self.type_id,
        }