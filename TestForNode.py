'''
author: Jianchao Wang, Neha Wadhwa
since: 08/05/2015
modified:08/05/2015
'''

import unittest
from Node import node

class TestForNode(unittest.TestCase):

    def test_node(self):
        test_object = node(3,None).item
        self.assertEqual(3,test_object)

    def test_str(self):
        test_object = str(node(3,None))
        self.assertEqual('3',test_object)


if __name__ == '__main__':
    unittest.main()
