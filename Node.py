'''
author: Jianchao Wang, Neha Wadhwa
since: 08/05/2015
modified:08/05/2015
This class is used to create node in order to build up the link stack
Input: item, link
Precondition:
Postcondition: node created
Return:
Complexity: Best and worst O(1)
'''

class node:
    #instantiate the node object
    def __init__(self,item,link):
        self.item = item
        self.next = link
    #return the item of the node object
    def __str__(self):
        return str(self.item)
