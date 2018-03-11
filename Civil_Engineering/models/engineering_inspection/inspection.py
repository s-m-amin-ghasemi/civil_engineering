
from abc import ABC, abstractmethod

class Inspection(ABC):
    def __init__(self):
        self.__data_processing_method__ = None

    @abstractmethod
    def __add__raw_data_collection__(self, raw_data_collection):
        pass
    
    @abstractmethod
    def __add_result_data_collection__(self):
        pass
    
    @abstractmethod
    def __add__adopted_standard__(self, adopted_standard):
        pass
    
    @abstractmethod
    def __add_data_processing_method__(self, data_processing_method):
        pass
    

    

