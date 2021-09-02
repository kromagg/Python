class Node:
    def __init__(self, data=None):
       self.data = data
       self.next = None
class Linkedlist:
    def __init__(self):
       self.headvalue = None
    def listprint(self):
        printvalue = self.headvalue
        while printvalue is not None:
            print (printvalue.data)
            printvalue = printvalue.next
            
list = Linkedlist()
list.headvalue = Node("first")
x2 = Node("second")
x3 = Node("third")
list.headvalue.next = x2
x2.next = x3
list.listprint()