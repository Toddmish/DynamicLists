'''
Created on Mar 29, 2021

@author: Todd
'''
from abc import ABC,abstractmethod

class SinglyLinkedListNodeInterface(ABC):
    
    @abstractmethod
    def get_next(self):
        pass
    
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_next(self):
        pass
    
    @abstractmethod
    def set_data(self):
        pass
