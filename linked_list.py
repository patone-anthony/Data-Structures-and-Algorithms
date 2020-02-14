class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def list_print(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next


    def insert_head(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def insert_end_node(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def insert_between(self, middle_node, new_data):
        if middle_node is None:
            print('The mentioned node is absent')
            return

        new_node = Node(new_data)
        new_node.next = middle_node.next
        middle_node.next = new_node


    def remove_node(self, remove_key):
        head_node = self.head
        if not head_node:
            return

        if head_node.data == remove_key:
            self.head = head_node.next
            return

        while head_node:
            current = head_node
            next_node = head_node.next

            if next_node.data == remove_key:
                current.next = next_node.next
                break

            head_node = head_node.next


    def reverse_list(self):
        prev = None
        curr = self.head
        next_node = curr.next

        while curr:
            curr.next = prev
            prev = curr
            curr = next_node
            if next_node:
                next_node = next_node.next

        self.head = prev


list1 = LinkedList()
list1.head = Node('Mon')
e2 = Node('Tues')
e3 = Node('Wed')

list1.head.next = e2
e2.next = e3

list1.insert_head('Sun')
list1.insert_end_node('Fri')
list1.insert_between(list1.head.next.next.next, 'Thurs')

list1.list_print()
print('\n')
list1.reverse_list()
list1.list_print()
