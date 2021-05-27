'''
Created on Mar 29, 2021

@author: Todd
'''


from SecondPackage.SinglyLinkedListNode import SinglyLinkedListNode
from SecondPackage.SinglyLinkedListInterface import SinglyLinkedListInterface



class List(SinglyLinkedListInterface):
    
    def __init__(self,head=None):
        self.__head=head
    
    def get_head(self):
        return  self.__head
    
    def set_head(self,head):
        self.__head=head
        
    #adding element to the begining of the list        
    def push(self, data):
        newNode=SinglyLinkedListNode(data)
        newNode.set_data(data)
        newNode.set_next(self.get_head())
        self.set_head(newNode)
        #return head
    
    def printList(self):

        temp=self.get_head()
        while( temp != None ):
            
            print(temp.get_data())
            temp=temp.get_next()              
        print("\n")
        
    # This method assumes that list is sorted        
    def insertToSortedList(self, sortedLst , newData):
        
        newNode=SinglyLinkedListNode(newData)
        
        #find the place to add the node
        
        #if None==head :
        #    head=newNode
        #    return head
        
        #adding the element to empty list or at the begining
        if None==sortedLst.get_head() or newNode.get_data()<sortedLst.get_head().get_data():
            newNode.set_next(sortedLst.get_head())
            sortedLst.set_head(newNode)
            return sortedLst
            
        curr=sortedLst.get_head()   
        while curr.get_next()!=None and newNode.get_data()>curr.get_next().get_data():
            curr=curr.get_next()
        
        if None==curr.get_next():
            curr.set_next(newNode)  
        else:
            newNode.set_next(curr.get_next())
            curr.set_next(newNode)
        
        return sortedLst

   
    def sortByInsertion(self):
        
        if None==self.__head or None==self.__head.get_next():
            return List()   
    
        curr=self.__head
        sortedList =List()
        
        while(curr!=None):
            sortedList=self.insertToSortedList(sortedList , curr.get_data())
            curr=curr.get_next()        

        self.__head=sortedList.get_head()
        
    
    def append(self, dataValue):
        #SinglyLinkedListInterface.append(self)
        
        curr=self.get_head()
        
        while(None!=curr.get_next()):
            curr=curr.get_next()
        
        newNode=SinglyLinkedListNode(dataValue)
        
        curr.set_next(newNode)
        
            
        
        
        
    
    
    
    





