class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        prev = None
        while current:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next

# Ejemplo de uso
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    print("¿Existe el nodo con valor 20?", linked_list.find(20))  # Debería imprimir True
    linked_list.delete(20)
    print("¿Existe el nodo con valor 20 después de eliminarlo?", linked_list.find(20))  # Debería imprimir False