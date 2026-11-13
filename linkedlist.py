# Approach: create an object with one reference linking to the next and one containing the value
# Time per op (push_back / pop_front / peek_front / __len__): 
# Space:O(n)

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self): #O(1)
        return self._head is None

    def push_front(self, val): #O(1)
        temp = Node(val)
        temp.next = self._head
        if self.is_empty():
            self._tail = temp
        self._head = temp
        self._size += 1

    def push_back(self, val): #O(1) with tail
        if self.is_empty():
            self.push_front(val)
            return
        temp = Node(val)
        self._size += 1
        self._tail.next = temp
        self._tail = temp

    def push_at_position(self, val, position): #O(position)

        if not 1 <= position <= self._size+1:
            raise IndexError("Invalid position")

        if position == 1:
            self.push_front(val)
            return
        temp = Node(val)
        temp1 = self._head
        for i in range (1,position-1):
            temp1 = temp1.next
        temp.next = temp1.next
        temp1.next = temp
        if temp.next is None: 
            self._tail = temp
        self._size += 1

    def pop_front(self): #O(1)

        if self.is_empty():
            raise IndexError("Cannot remove from an empty LinkedList")
        else:
            temp = self._head.data
            self._head = self._head.next
            self._size -=1
            if self._head is None:
                self._tail = None
            return temp

    def pop_back(self): #O(n) even with tail pointer
        if self.is_empty():
            raise IndexError("Cannot remove from an empty LinkedList")
        elif self._head is self._tail:
            return self.pop_front()
        else:
            temp = self._head
            while temp.next is not self._tail:
                temp = temp.next
            return_data = self._tail.data
            temp.next = None
            self._tail = temp
            self._size -=1
            return return_data

    def pop_at_position(self, position): #O(position)

        if not 1 <= position <= self._size:
            raise IndexError("Invalid position")

        if position == 1:
            return self.pop_front()
        else:
            temp = self._head
            for i in range (1, position-1):
                temp = temp.next
            return_data = temp.next.data
            temp.next = temp.next.next
            if temp.next is None:
                self._tail = temp
            self._size -= 1
            return return_data
    
    def search(self, val): #O(n)
        temp = self._head
        while temp is not None:
            if temp.data == val: return True
            else: temp = temp.next
        return False
    
    def traverse(self): #O(n)
        temp = self._head
        L_list = []

        while temp is not None:
            L_list.append(f"{temp.data}->")
            temp = temp.next

        L_list.append("None")
        return "".join(L_list)

    def peek_front(self): #O(1)
        if self.is_empty():
            raise IndexError("LinkedList is empty")
        return self._head.data

    def __len__(self):
        return self._size
    
    def __repr__(self):
        return f"LinkedList({self.traverse()})"

if __name__ == "__main__":
    l1 = LinkedList()
    l1.push_back(1)
    l1.push_back(2)
    l1.push_back(3)
    print(len(l1))
    print(l1)
    #l1.pop_at_position(4)
    #l1.push_at_position(9,0)

    l2 = LinkedList()
    l2.push_front('a')
    l2.pop_front()
    #l2.peek_front()
    print(l2.is_empty())
    print(l2._tail is None)
    l2.push_front('b')
    print(len(l2))
    print(l2._tail)