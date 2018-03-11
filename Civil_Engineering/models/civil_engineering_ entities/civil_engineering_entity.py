from abc import ABC, abstractmethod, ABCMeta

class CivilEngineeringEntity(ABC):
    pass
x = CivilEngineeringEntity()
print(CivilEngineeringEntity.__base__.__instancecheck__(x))

