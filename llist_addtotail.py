class Node:
    def __init__(self, data=None):
       self.data = data
       self.next = None

class Linkedlist:
    def __init__(self):
       self.headvalue = None
    def AtEnd(self,newdata):
         NewNode = Node(newdata)
         if self.headvalue is None:
             self.headvalue = NewNode
             return
         last = self.headvalue
         while(last.next):
             last = last.next
         last.next=NewNode
    def listprint(self):
         printvalue = self.headvalue
         while printvalue is not None:
             print (printvalue.data)
             printvalue = printvalue.next

my_list = Linkedlist()
my_list.headvalue = Node("jan")
x2 = Node("feb")
x3 = Node("march")
my_list.headvalue.next = x2
x2.next = x3
my_list.AtEnd("april")
my_list.listprint()