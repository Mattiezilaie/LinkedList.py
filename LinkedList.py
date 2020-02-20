# Author: Mahtab Zilaie
# Date: February 19 2020
# Description: LinkedList class that has recursive implementations of the
# add, display, remove, contains, insert, and reverse methods with helper functions

class Node:
    """
    Represents a node in a linked list
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A linked list implementation of the List ADT
    """

    def __init__(self):
        self.head = None

    def rec_add(self, temp, val):  # helper function
        if temp is None:  # if current is equal to None
            return Node(val)
        else:
            temp.next = self.rec_add(temp.next, val)
            return temp

    def add(self, val):
        """
        Adds a node containing val to the linked list
        """
        self.head = self.rec_add(self.head, val)

    def rec_insert(self, head, pos, val):  # helper function # 1 -> 2 -> 4 -> 3 -> None
        if pos < 0:
            return
        if head is None and pos > 0:
            return
        if pos == 0:
            new_node = Node(val)
            new_node.next = head
            return new_node
        else:
            head.next = self.rec_insert(head.next, pos - 1, val)
            return head

    def insert(self, val, pos):
        """
        inserts a node containing a val to the linked list at specific position
        """
        self.head = self.rec_insert(self.head, pos, val)

    def rec_display(self, head):  # helper function
        if head is None:
            return
        else:
            print(head.data, end=" ")  # 1-> 2 -> 3 -> None
            self.rec_display(head.next)

    def display(self):
        """
        Prints out the values in the linked list
        """
        self.rec_display(self.head)
        print()

    def rec_remove(self, head, val):  # helper function # 1 -> 2 -> 3 -> None
        if head is None:
            return
        elif head.data == val:
            return head.next
        else:
            head.next = self.rec_remove(head.next, val)
            return head

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        self.head = self.rec_remove(self.head, val)

    def rec_reverse(self, head):  # helper function
        if head is None:
            return head
        if head.next is None:
            return head
        temp = self.rec_reverse(head.next)
        head.next.next = head
        head.next = None
        return temp

    def reverse(self):
        """
        Reverses nodes in linked list
        """
        self.head = self.rec_reverse(self.head)

    def rec_contains(self, head, val): #helper function
        if head is None:
            return False
        elif head.data == val:
            return True
        else:
            return self.rec_contains(head.next, val)

    def contains(self, key):
        """
        Checks if key is in linked list
        """
        return self.rec_contains(self.head, key)

# test cases
#LL = LinkedList()
#LL.add(5)
#LL.add(6)
# LL.add(9)
# LL.add(11)
# print(LL.contains(11))
#print(LL.contains(10))

# LL.insert(100, 2)
#LL.display()
# LL.insert(109, 3)
# LL.display()
# LL.remove(109)
# LL.display()
# LL.remove(5)
# LL.display()
# LL.reverse()
# LL.display()
