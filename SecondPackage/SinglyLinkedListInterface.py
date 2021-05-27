'''
Created on Mar 29, 2021

@author: Todd
'''
from abc import ABC,  abstractmethod

class SinglyLinkedListInterface(ABC):
    
    @abstractmethod
    def get_head(self):
        pass
    
    @abstractmethod
    def set_head(self,head):
        pass
    
    @abstractmethod
    def push(self, data):
        pass
    
    @abstractmethod
    def printList(self):
        pass
    
    @abstractmethod
    def insertToSortedList(self, sortedLst , newData):
        pass
    
    @abstractmethod
    def sortByInsertion(self):
        pass
    
    @abstractmethod
    def append(self):
        pass
    
    
    