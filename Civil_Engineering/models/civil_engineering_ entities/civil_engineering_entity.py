from abc import ABC, abstractmethod, ABCMeta

class CivilEngineeringEntity(ABC):
    def __init__(self):
        self.__inspection__ = {}
    @abstractmethod
    def add_inspection(self, inspection_name, inspection):
        pass


