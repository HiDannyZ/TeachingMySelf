class Node:
    def __init__(self,data, nextNode = None):
        self.data = data
        self.next = nextNode

class linkedList:
    def __init__(self,head):
        self.head = head
        self.size = 0

    def addNode(self,data):
        new_Node = Node(data)
        new_Node.next = self.head
        self.head = new_Node

    def size(self):
        current = self.head
        while current is not None:
            current = current.next
            self.size += 1

    def deleteNode(self,data):
        current = self.head
        while current.next.data != data:
            current = current.next
        current.next = current.next.next
        nextNode = current.next
        nextNode.next = None

    def searchNode(self,data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
        return False

    def insertEnd(self,data):
        current = self.head
        while current.next is not None:
            current = current.next
        new_Node = Node(data)
        current.next = new_Node

    def printLinkedList(self):
        current = self.head
        while current is not None:
            #current = current.next
            print(current.data)
            current = current.next

if __name__ == '__main__':

    head_input = input("Insert Head Value:")

    user_input = input()

    listNodes = user_input.split()

    dictionary = {}

    headNode = linkedList(Node(head_input))

    for i in range(len(listNodes)):
        if listNodes[i] in dictionary:
            continue
        else:
            dictionary[listNodes[i]] = 1
    for key in dictionary.keys():
        headNode.insertEnd(key)
        #headNode.addNode(key)

    headNode.printLinkedList()
