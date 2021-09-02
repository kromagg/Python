class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def Atbegining(self, data_n):
        NewNode = Node(data_n)
        NewNode.next = self.head
        self.head = NewNode
    def RemoveNode(self, Removekey):
        Headvalue = self.head
        if (Headvalue is not None):
            if (Headvalue.data == Removekey):
                self.head = Headvalue.next
                Headvalue = None
                return
        while (Headvalue is not None):
            if Headvalue.data == Removekey:
                break
            previous = Headvalue
            Headvalue = Headvalue.next
        if (Headvalue == None):
            return
        previous.next = Headvalue.next
        Headvalue = None
    def list_print(self):
        printvalue = self.head
        while (printvalue):
            print(printvalue.data),
            printvalue = printvalue.next
my_list = Linkedlist()
my_list.Atbegining("jan")
my_list.Atbegining("feb")
my_list.Atbegining("march")
my_list.RemoveNode("jan")
my_list.list_print()