class Medic():

    def __init__(self, first_name, last_name, email, password, token = None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }


class LoginConfirm():
    
        def __init__(self, email, password):
            self.email = email
            self.password = password
    
        def to_json(self):
            return {
                "email": self.email,
            }