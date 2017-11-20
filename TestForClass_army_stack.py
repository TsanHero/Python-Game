'''
author: Jianchao Wang, Neha Wadhwa
since: 08/05/2015
modified:08/05/2015
'''

import unittest
from Stack import stack
from Army import army


class Test_Stack_army(unittest.TestCase):

    def test_push_pop_1(self):
        test_object_stack = stack()
        test_object_stack.push(1)
        test_object_stack.push(2)
        test_object_stack.push(3)
        test_object_stack.push(4)
        test_object = []
        while not test_object_stack.is_empty():
            test_object.append(test_object_stack.pop())
        self.assertEqual([4,3,2,1],test_object)
    '''
    def test_push_pop_2(self):
        test_object_stack = stack()
        #self.assertEqual([],test_object)
        self.assertRaises(AssertionError,test_object_stack.pop())
    '''

    def test_isEmpty_Success(self):
        test_object_stack = stack()
        test_object = test_object_stack.is_empty()
        self.assertEqual(True,test_object)

    def test_isEmpty_Fail(self):
        test_object_stack = stack()
        test_object_stack.push(1)
        test_object = test_object_stack.is_empty()
        self.assertEqual(False,test_object)

    def test_army(self):
        test_object = army("Fan").player
        self.assertEqual("Fan",test_object)

    
    def test_setUp(self):
        test_object_stack = army("Fan").setUp()
        test_object = []
        while not test_object_stack.is_empty():
            test_object.append(test_object_stack.pop())
        self.assertEqual([],test_object)
    
if __name__ == '__main__':
    unittest.main()
