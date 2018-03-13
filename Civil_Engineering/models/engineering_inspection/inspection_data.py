from abc import ABC, abstractmethod
from astropy.units import  unit
from astropy.units.quantity import Quantity

class Insp_Data(ABC):
    @property
    @abstractmethod
    def __value__(self, **value):
        pass
    @__value__.getter
    @abstractmethod
    def __value__(self):
        pass
    
class Insp_Data_String(Insp_Data):
    pass

class Insp_Data_Numberi(Insp_Data):
    pass

class Insp_Data_Category(Insp_Data):
    pass

class Insp_Data_Nomina(Insp_Data):
    pass

class Insp_Data_ordinal(Insp_Data):
    pass
