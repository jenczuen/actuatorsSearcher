from enum import Enum
from math import pi

data_table = {
#    "OSPE-BHD1-20" : {
       "column_A" : 5750,
        "column_B" : 1600,
        "column_C" : 1600,
        "column_D" : 21,
        "column_E" : 150,
        "column_F" : 150,
        "column_J" : 3,
        "column_K" : 50,
        "column_L" : 25,
        "column_M" : 0.8,
        "column_" : 0.6
#    }
}



class ActuatorType(Enum):
    CARRIAGE = 1
    PISTON_ROD = 2
    PION = 3
    ETT = 4

class CarriagePosition(Enum):
    HORIZONTAL_TOP = 1
    HORIZONTAL_BOTTOM = 2
    HORIZONTAL_SIDE = 3
    VERTICAL = 4

class PistonPosition(Enum):
    VERTICAL = 1
    HORIZONTAL = 2

class CenterOfMassCalculator():
    def calculate(self, postition):
        if isinstance(postition, CarriagePosition):
            self.__calculate_for_carriage(postition)
        elif isinstance(postition, PistonPosition):
            self.__calculate_for_piston(postition)

    def __calculate_for_carriage(self, position):
        if position == CarriagePosition.VERTICAL_TOP or \
                        position == CarriagePosition.VERTICAL_BOTTOM:
            # Fz = m * g
            Fz = data_table["column_B"]
            # Mx = l * m * g
            Mx = data_table["column_D"]
            #My = l * m * g
            My = data_table["column_F"]
        elif position == CarriagePosition.VERTICAL_SIDE:
            # Fy = m * g
            Fy = data_table["column_C"]
            # Mx = I * m * g,
            Mx = data_table["column_D"]
        elif position == CarriagePosition.HORIZONTAL:
            # Mz = I * m * g
            Mz = data_table["column_E"]
            # My = Iz * m * g,
            My = data_table["column_F"]

    def __calculate_for_piston(self, position):
        Ftotal = 0
        if position == PistonPosition.HORIZONTAL:
            # Ftotal = F + Fg data_table["column_?"]
            Ftotal = 1
        elif position == PistonPosition.VERTICAL:
            # Ftotal = F data_table["column_?"]
            Ftotal = 2
        self.__calculate_parameters_for_piston(Ftotal)

    def __calculate_parameters_for_piston(self, Ftotal):
        pass
        # k = Ftotal / Fmax
        # M = Mmax * k




class Actuator():
    def __init__(self):
        self.type = ActuatorType.CARRIAGE
        self.step = 5750  # A
        self.position = CarriagePosition.HORIZONTAL