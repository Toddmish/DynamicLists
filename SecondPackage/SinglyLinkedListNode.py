from SecondPackage.SinglyListNodeInterface import SinglyLinkedListNodeInterface

class SinglyLinkedListNode(SinglyLinkedListNodeInterface):
    
    def __init__(self,data):
        self.__data=data
        self.__next=None
        
    def get_data(self):
        return self.__data
        
    def get_next(self):
        return self.__next
    
    def set_data(self,data):
        self.__data=data
        
        
    def set_next(self,newNode):
        self.__next=newNode
        