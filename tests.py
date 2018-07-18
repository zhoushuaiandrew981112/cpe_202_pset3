from pset3 import *
import unittest

class Test_Queue(unittest.TestCase):

    def test_Node_case_init_0(self):
        node_0 = Node(0)
        self.assertEqual(node_0.data, 0)
        self.assertEqual(node_0.next, None)


    def test_Node_case_init_1(self):
        node_1 = Node(1)
        self.assertEqual(node_1.data, 1)
        self.assertEqual(node_1.next, None)

    def test_Node_case_init_2_3(self):
        node_0 = Node(0)
        node_1 = Node(1)
        node_2 = Node(2, node_0)
        node_3 = Node(3, node_1)
        self.assertEqual(node_2.data, 2)
        self.assertEqual(node_2.next, node_0)
        self.assertEqual(node_3.data, 3)
        self.assertEqual(node_3.next, node_1)

    def test_ListQueue_init_1(self):
        lq = ListQueue(5)

        self.assertEqual(lq.head, None)
        self.assertEqual(lq.capacity, 5)
        self.assertEqual(lq.size, 0)

    def test_ListQueue_init_2(self):
        lq = ListQueue(4)

        self.assertEqual(lq.head, None)
        self.assertEqual(lq.capacity, 4)
        self.assertEqual(lq.size, 0)

    def test_ListQueue_init_3(self):
        lq = ListQueue(3)

        self.assertEqual(lq.head, None)
        self.assertEqual(lq.capacity, 3)
        self.assertEqual(lq.size, 0)

    def test_ListQueue_enqueue_0(self):
        lq = ListQueue(0)

        self.assertEqual(lq.head, None)
        self.assertEqual(lq.size, 0)
        with self.assertRaises(IndexError):
            lq.enqueue(1)


    def test_ListQueue_enqueue_cap_1(self):
        lq = ListQueue(1)
        
        self.assertEqual(lq.head, None)
        self.assertEqual(lq.size, 0)
        # queue: None       
        lq.enqueue(1)
        self.assertEqual(lq.head.data, 1)
        self.assertEqual(lq.size, 1)
        # queue: 1
        with self.assertRaises(IndexError):
            lq.enqueue(2) 

    def test_ListQueue_enqueue_cap_3(self):
        lq = ListQueue(3)

        self.assertEqual(lq.head, None)
        self.assertEqual(lq.size, 0)
        # queue: None
        lq.enqueue(1)
        self.assertEqual(lq.head.data, 1)
        self.assertEqual(lq.size, 1)
        # queue: 1
        lq.enqueue(2)
        self.assertEqual(lq.head.data, 1)
        self.assertEqual(lq.size, 2)
        # queue: 1 -> 2
        lq.enqueue(3)
        self.assertEqual(lq.head.data, 1)
        self.assertEqual(lq.size, 3)
        # queue: 1 -> 2 -> 3
        with self.assertRaises(IndexError):
            lq.enqueue(4)

    def test_listQueue_dequeue_cap_0(self):
        lq = ListQueue(0)
        
        self.assertEqual(lq.head, None)
        self.assertEqual(lq.size, 0)
        with self.assertRaises(IndexError):
            lq.dequeue() 

    def test_listQueue_dequeue_cap_2(self):
        lq = ListQueue(2)
        
        lq.enqueue(1)
        lq.enqueue(2)
        self.assertEqual(lq.head.data, 1)
        self.assertEqual(lq.size, 2)
        # queue: 1 -> 2
        self.assertEqual(lq.dequeue(), 1)
        self.assertEqual(lq.head.data, 2)
        self.assertEqual(lq.size, 1)
        # queue: 2
        self.assertEqual(lq.dequeue(), 2)
        self.assertEqual(lq.head, None)
        self.assertEqual(lq.size, 0)
        # queue: None
        with self.assertRaises(IndexError):
            lq.dequeue() 

        
    def test_listQueue_dequeue_cap_3(self):
        lq = ListQueue(3)
        
        lq.enqueue(1)
        lq.enqueue(2)
        lq.enqueue(3)
        self.assertEqual(lq.head.data, 1)
        self.assertEqual(lq.size, 3)
        # queue: 1 -> 2 -> 3
        self.assertEqual(lq.dequeue(), 1)
        self.assertEqual(lq.head.data, 2)
        self.assertEqual(lq.size, 2)
        # queue: 2 -> 3
        self.assertEqual(lq.dequeue(), 2)
        self.assertEqual(lq.head.data, 3)
        self.assertEqual(lq.size, 1)
        # queue: 3
        self.assertEqual(lq.dequeue(), 3)
        self.assertEqual(lq.head, None)
        self.assertEqual(lq.size, 0)
        # queue: None
        with self.assertRaises(IndexError):
            lq.dequeue() 

    def test_CircularQueue_init_cap_0(self):
        cq = CircularQueue(0)
        
        self.assertEqual(cq.capacity, 0) 
        self.assertEqual(cq.items, []) 
        self.assertEqual(cq.size, 0) 
        self.assertEqual(cq.head, 0) 
        self.assertEqual(cq.tail, 0) 

    def test_CircularQueue_init_cap_3(self):
        cq = CircularQueue(3)
        
        self.assertEqual(cq.capacity, 3) 
        self.assertEqual(cq.items, [None, None, None]) 
        self.assertEqual(cq.size, 0) 
        self.assertEqual(cq.head, 0) 
        self.assertEqual(cq.tail, 0) 

    def test_CircularQueue_init_cap_5(self):
        cq = CircularQueue(5)
        
        self.assertEqual(cq.capacity, 5) 
        self.assertEqual(cq.items, [None, None, None, None, None]) 
        self.assertEqual(cq.size, 0) 
        self.assertEqual(cq.head, 0) 
        self.assertEqual(cq.tail, 0) 

    def test_circularQueue_enqueue_3(self):
        cq = CircularQueue(3)
        # queue: [None, None, None] 
        self.assertEqual(cq.capacity, 3) 
        self.assertEqual(cq.items, [None, None, None]) 
        self.assertEqual(cq.size, 0) 
        self.assertEqual(cq.head, 0) 
        self.assertEqual(cq.tail, 0) 
        
        cq.enqueue(0)
        # queue: [0, None, None] 
        self.assertEqual(cq.capacity, 3) 
        self.assertEqual(cq.items, [0, None, None]) 
        self.assertEqual(cq.size, 1) 
        self.assertEqual(cq.head, 0) 
        self.assertEqual(cq.tail, 0) 
       
        cq.enqueue(1)
        # queue: [0, 1, None] 
        self.assertEqual(cq.capacity, 3) 
        self.assertEqual(cq.items, [0, 1, None]) 
        self.assertEqual(cq.size, 2) 
        self.assertEqual(cq.head, 0) 
        self.assertEqual(cq.tail, 1) 
         
        
        cq.enqueue(2)
        # queue: [0, 1, 2]
        self.assertEqual(cq.capacity, 3) 
        self.assertEqual(cq.items, [0, 1, 2]) 
        self.assertEqual(cq.size, 3) 
        self.assertEqual(cq.head, 0) 
        self.assertEqual(cq.tail, 2) 

    def test_CircularQueue_dequeue_3(self):
        cq = CircularQueue(3)

        cq.enqueue(0)
        cq.enqueue(1)
        cq.enqueue(2)
        # queue: [0, 1, 2]
        self.assertEqual(cq.capacity, 3) 
        self.assertEqual(cq.items, [0, 1, 2]) 
        self.assertEqual(cq.size, 3) 
        self.assertEqual(cq.head, 0) 
        self.assertEqual(cq.tail, 2) 

        cq.dequeue()
        # queue: [None, 1, 2]
        self.assertEqual(cq.capacity, 3) 
        self.assertEqual(cq.items, [None, 1, 2]) 
        self.assertEqual(cq.size, 2) 
        self.assertEqual(cq.head, 1) 
        self.assertEqual(cq.tail, 2) 
        
        cq.dequeue()
        # queue: [None, None, 2]
        self.assertEqual(cq.capacity, 3) 
        self.assertEqual(cq.items, [None, None, 2]) 
        self.assertEqual(cq.size, 1) 
        self.assertEqual(cq.head, 2) 
        self.assertEqual(cq.tail, 2) 

        cq.dequeue()
        # queue: [None, None, None]
        self.assertEqual(cq.capacity, 3) 
        self.assertEqual(cq.items, [None, None, None]) 
        self.assertEqual(cq.size, 1) 
        self.assertEqual(cq.head, 0) 
        self.assertEqual(cq.tail, 0) 







if __name__ == "__main__":
    unittest.main() 
