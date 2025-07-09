class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:  # list is empty
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_at_begin(data)
            return

        current_node = self.head
        position = 0
        while current_node is not None and position < index - 1:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            return "Index not present"

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node  # new_node next is already None

    def remove_node_beginning(self):
        if self.head is None:
            return

        self.head = self.head.next

    def remove_node_from_index(self, index):
        if self.head is None:  # list is empty
            return

        if index == 0:
            self.head = self.head.next
            return

        position = 0
        previous_node = self.head
        current_node = self.head.next

        while current_node.next is not None and position != index - 1:
            position += 1
            current_node = current_node.next
            previous_node = previous_node.next

        previous_node.next = current_node.next
        # current_node.next = previous_node

    def remove_node_from_value(self, value):
        if self.head is None:  # list is empty
            return

        if self.head.data is value:  # single element in the list
            self.head = None
            return

        previous_node = self.head
        current_node = self.head.next

        while current_node.next is not None and current_node.data != value:
            current_node = current_node.next
            previous_node = previous_node.next

        if current_node is None:  # Not found
            return

        previous_node.next = current_node.next
        # current_node.next = previous_node

    def remove_node_from_end(self):
        if self.head is None:  # list is empty
            return

        if self.head.next is None:  # single node in the list
            self.head = None
            return

        previous_node = self.head
        current_node = self.head.next

        # we need to find the one previous node from the last node
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = None

    def search_ll(self, value):
        current_node = self.head
        position = 0

        while current_node.next is not None:
            if current_node.data == value:
                return position
            current_node = current_node.next
            position += 1

        return "Value not present in the list"

    def size_of_llist(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def print_ll(self):
        current_node = self.head
        print('head ->', end=' ')
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print('None')


def main():
    llist = LinkedList()
    llist.insert_at_begin('a')
    llist.insert_at_begin('b')
    llist.insert_at_begin('c')
    llist.insert_at_begin('d')

    llist.insert_at_end(12)

    llist.insert_at_index('e', 2)

    llist.print_ll()

    # remove
    llist.remove_node_from_value('c')
    # print('\n')

    llist.print_ll()

    # print(llist.size_of_llist())


if __name__ == '__main__':
    main()
