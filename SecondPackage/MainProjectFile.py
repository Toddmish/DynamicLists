'''
Created on Mar 29, 2021

@author: Todd
'''

if __name__ == '__main__':
    pass

from SecondPackage.SinglyLinkedList import List

myList=List()

myList.push(7)
myList.push(6)
myList.push(5)
myList.push(10)
myList.push(9)
myList.push(8)

#a=insertToSortedList(a , 7)
#a=insertToSortedList(a , 4)
#a=insertToSortedList(a , 11)
#printList(a)

myList.printList()


myList.sortByInsertion()
print("After sorting")
myList.printList()

myList.append(24)
print("After appending")
myList.printList()