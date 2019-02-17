#Write Code to remove duplicates from an unsorted linked list

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None #Pointer points to nothing initially
class LinkedList
    def __init__(self,head=None):
        self.head = head
    def insert(self,value):
        new_Node = Node(value)
        new_Node.next = 

# I need to make another class that keeps track of Head value

if __name__ == '__main__':

    user_input = input()

    list_Nodes = user_input.split()

    print(list_Nodes)

    firstNode = Node("Current")

    currentNode = firstNode

    for i in range(len(list_Nodes)):
        nextNode = Node(list_Nodes[i])
        currentNode.next = nextNode
        currentNode = nextNode
        print("LOL")

    firstNode.next = None



    """"
    node1 = Node(14)
    node2 = Node(12)
    node3 = Node(13)
    node4 = Node(14)

    node1.next = node2
    node2.next = node3
    node3.next = node4


    #Code under here removes duplicates

    dictionary = {node1.val:1}

    currentNode = node1
    while currentNode.next is not None:
        if currentNode.next.val not in dictionary:
            dictionary[currentNode.next.val] = 1
            print(currentNode.next.val)
            currentNode = currentNode.next
        else:
            print("The value of removed Node: ", currentNode.next.val)
            currentNode.next = None
    """



