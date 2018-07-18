# Name:             Zhoushuai (Andrew) Wu
# Course:           CPE 202
# Instructor:       Daniel Kauffman
# Assignment:       Problem Set 3: Queues
# Term:             Summer 2018


class Node:

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class ListQueue:

    def __init__(self, capacity):
        self.head = None
        self.capacity = capacity
        self.size = 0

    def enqueue(self, item):
        if self.size >= self.capacity:
            raise IndexError
        elif self.head == None:
            self.head = Node(item)
            self.size += 1
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(item)
            self.size += 1

    def dequeue(self):
        if self.size <= 0:
            raise IndexError
        else:
            temp = self.head
            self.head = temp.next
            self.size -= 1
            return temp.data 

    def display(self):
        current = self.head
        list_rep = []
        while current != None:
            list_rep.append(current.data)
            current = current.next
        return list_rep   


class CircularQueue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.size = 0
        self.head = 0
        self.tail = 0

    def is_full(self):
        return (self.head == (self.tail + 1) % self.capacity)

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            raise IndexError
        else:
            self.size += 1
            if self.size != 1:
                self.tail = (self.tail + 1) % self.capacity
                self.items[self.tail] = item
            else:
                self.items[self.tail] = item
            
    def dequeue(self):
        if self.is_empty():
            raise IndexError
        else:
            temp = self.items[self.head]
            self.items[self.head] = None
            if self.is_empty():
                self.head = 0
                self.tail = 0
            else:
                self.head = (self.head + 1) % self.capacity
            self.size -= 1
            return temp




