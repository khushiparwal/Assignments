class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def add_node(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print("Added head node with data: ",data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            print("Added node with data: ",data)
    def print_list(self):
        if not self.head:
            print("The list is empty")
            return
        current = self.head
        print("Linked list: ",end=" ")
        while current:
            print(current.data, end='-->')
            current = current.next
        print("None")
    def delete_nth_node(self,n):
        if not self.head:
            raise Exception("Cannot delete from an empty linked list.")
        if n<=0:
            raise IndexError("Index should be 1 or greater than 1.")
        if n==1:
            print("Deleting node at position", n ,"with data: ",self.head.data)
            self.head = self.head.next
            return
        current = self.head
        prev = None
        count = 1
        while current and count<n:
            prev = current
            current = current.next
            count += 1
        if not current:
            raise IndexError("Index out of range")
        print("Deleting node at position", n ,"with data: ",current.data)
        prev.next = current.next

if __name__ == "__main__":
    l1 = LinkedList()
    l1.add_node(10)
    l1.add_node(20)
    l1.add_node(30)
    l1.add_node(40)
    l1.add_node(50)
    l1.print_list()
    try:
        l1.delete_nth_node(10)
    except Exception as e:
        print("Error: ",e)
    
    l1.delete_nth_node(4)
    l1.print_list()
