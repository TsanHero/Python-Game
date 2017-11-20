'''
author: Jianchao Wang, Neha Wadhwa
since: 08/05/2015
modified:08/05/2015
'''

from Node import node

class stack:

    def __init__(self):
        self.top = None

    def is_empty(self):
        if self.top is None:
            return True
        elif self.top is not None:
            return False

    def push(self,item):
        self.top = node(item,self.top)

    def pop(self):
        assert not self.is_empty(), "Stack is empty"

        item = self.top.item
        self.top = self.top.next
        return item

    '''
    def __str__(self):
        current=self.top
        string=""

        while(current is not None):
            string+=str(current.item)+", "
            current=current.next()
        return string
    '''
