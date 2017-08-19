"""
Interview Practice
File Structure
Linked List and Stack and Queue handling

            Tatsuya Arai

"""


class Node(object):
    """A single node of a linked list."""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def lstToLinkedList(lst):
    """A list to a single node linked list"""
    if not lst: return
    LinkedList = Node(lst[0])
    LinkedList.next = lstToLinkedList(lst[1:])
    return LinkedList

def lstToLinkedList2(lst):
    """A list to a single node linked list"""
    """Not So Smart Way"""
    if not lst: return
    tail = Node(lst[-1])
    for i0 in range(len(lst) - 2, -1, -1):
        fakehead = Node(lst[i0])
        fakehead.next = tail
        tail = fakehead
    return tail

def linkedLstToList(Llst):
    """A list to a single node linked list"""
    if not Llst: return []
    return [Llst.value] + linkedLstToList(Llst.next)

"""Lst -> LL"""
lst = [1,2,3,4,5,6]
Llst = lstToLinkedList(lst)
Llst2 = lstToLinkedList2(lst)

"""LL -> Lst"""
lst2 = linkedLstToList(Llst)
lst2

""" Stack and Queue -List-"""
class StackNQueue(object):
    """A list to a stackNqueue"""
    def __init__(self, lst):
        self.lst = lst
    """Push and Pop from the tail i.e. lst[-1]"""
    def push(self, value): ################# <- 
        """Push a value onto the stack."""
        self.lst = self.lst +[value]
    def pop(self): ##################### <-
        """Pops a value from the stack."""
        value = self.lst[-1]
        self.lst = self.lst[:-1]
        return value
    """Enqueue from the tail and Dequeue from the head"""
    def enqueue(self, value): ################# <- 
        """Enqueue a value into the Queue."""
        self.lst = self.lst +[value]
    def dequeue(self): ##################### <-
        """Dequeue a value from the Queue."""
        value = self.lst[0]
        self.lst = self.lst[1:]
        return value

snq = StackNQueue(lst)


""" Stack and Queue -Linked List-"""
class StackNQueueLL(object):
    """Simple Stack implementation with push, pop."""
    def __init__(self):
        """Initialize a Stack object."""
        self.top = None
    def push(self, value): ################# <- 
        """Push a value onto the stack."""
        self.top = Node(value, next=self.top)
    def pop(self): ##################### <-
        """Pops a value from the stack."""
        value = self.top.value
        self.top = self.top.next
        return value
    def enqueue(self, value): ################# <- 
        """Enqueue a value onto the Queue."""
        self.top = Node(value, next=self.top)
    def dequeue(self): ##################### <-
        """Dequeue a value from the Queue."""
        """Llst -> lst, dequeue, lst -> Llst"""
        top = self.top
        def linkedLstToList(Llst):
            """A list to a single node linked list"""
            if not Llst: return []
            return [Llst.value] + linkedLstToList(Llst.next)
        def lstToLinkedList(lst):
            """A list to a single node linked list"""
            if not lst: return
            LinkedList = Node(lst[0])
            LinkedList.next = lstToLinkedList(lst[1:])
            return LinkedList
        self.top = lstToLinkedList(linkedLstToList(top)[:-1])
        return linkedLstToList(top)[-1]
    def printSNQ(self):
        """Print StackNQueue."""
        def PSNQ(top):
            if top: 
                print(top.value)
                PSNQ(top.next)
        PSNQ(self.top)

""" Stack and Queue -Linked List2-"""
""" Dequeue does not return value..."""
class StackNQueueLL2(object):
    """Simple Stack implementation with push, pop, peek and is_empty."""
    def __init__(self):
        """Initialize a Stack object."""
        self.top = None
    def push(self, value): ################# <- 
        """Push a value onto the stack."""
        self.top = Node(value, next=self.top)
    def pop(self): ##################### <-
        """Pops a value from the stack."""
        value = self.top.value
        self.top = self.top.next
        return value
    def enqueue(self, value): ################# <- 
        """Enqueue a value onto the Queue."""
        self.top = Node(value, next=self.top)
    def dequeue(self): ##################### <-
        """Dequeue a value from the Queue."""
        top = self.top
        def dQsub(top):
            if not top.next: return
            else:
                if top.next.next:
                    topDQ = Node(top.value)
                    topDQ.next = dQsub(top.next)
                else:
                    topDQ = Node(top.value)
            return topDQ
        self.top = dQsub(top)
    def printSNQ(self):
        """Print StackNQueue."""
        def PSNQ(top):
            if top: 
                print(top.value)
                PSNQ(top.next)
        PSNQ(self.top)

snqLL = StackNQueueLL()
snqLL.enqueue(1)
snqLL.enqueue(2)
snqLL.enqueue(3)
snqLL.enqueue(4)
snqLL.enqueue(5)
snqLL.enqueue(6)

snqLL.printSNQ()
snqLL.dequeue()

""" This is a copy from someone else's work """
class Stack(object):
    """Simple Stack implementation with push, pop, peek and is_empty."""
    def __init__(self):
        """Initialize a Stack object."""
        self.top = None
    def peek(self):
        """Return the top value of the stack without popping."""
        return self.top.value
    def push(self, value): ################# <- 
        """Push a value onto the stack."""
        self.top = Node(value, next=self.top)
    def pop(self): ##################### <-
        """Pops a value from the stack."""
        value = self.top.value
        self.top = self.top.next
        return value
    def is_empty(self):
        return self.top is None
    def to_list(self):
        lst, node = [], self.top
        while node:
            lst.append(node.value)
            node = node.next
        return lst
    def __str__(self):
        return str(self.to_list())
