
"""
1. PODAJEMY DANE WEJSCIOWE
2. DLA KAZDEGO A Z BAZY:
    2. WYLICZAMY VMAX ORAZ MMAX NA PODSTAWIE DANYCH WEJSCIOWYCH I MODELU
       UZYWAJAC MovementParams123 W ZALEZNOSCI OD WYBRANEGO PROFILU RUCHU

    1. BIERZEMY ACTUATOR
"""

class Validator:
    def __init__(self, actuator):
        self.actuator = actuator
        self.log_list = []

    def validateColumnA(self, value):
        if self.actuator.column < value:
            self.log_list.append("actuator.column < value")

    def validateColumnG(self, value):
        if self.actuator.column < value:
            self.log_list.append("actuator.column < value")

    def validateColumnH(self, value):
        if self.actuator.column < value:
            self.log_list.append("actuator.column < value")

    def validateColumnI(self, value):
        if self.actuator.column < value:
            self.log_list.append("actuator.column < value")

    def validateColumnE(self, value):
        if self.actuator.column < value:
            self.log_list.append("actuator.column < value")

    def validateColumnF(self, value):
        if self.actuator.column < value:
            self.log_list.append("actuator.column < value")

    def validateColumnJ(self, value):
        if self.actuator.column < value:
            self.log_list.append("actuator.column < value")

    def validateColumnK(self, value):
        if self.actuator.column < value:
            self.log_list.append("actuator.column < value")