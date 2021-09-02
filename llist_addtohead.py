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
    def Atbegining(self,newdata):
         NewNode = Node(newdata)
         NewNode.next = self.headvalue
         self.headvalue = NewNode

my_list = Linkedlist()
my_list.headvalue = Node("jan")
x2 = Node("feb")
x3 = Node("march")
my_list.headvalue.next = x2
x2.next = x3
my_list.Atbegining("dec")
my_list.listprint()