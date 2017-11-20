'''
author: Jianchao Wang, Neha Wadhwa
since: 08/05/2015
modified:08/05/2015
'''

import unittest
from Archer import archer
from Soldier import soldier
from Cavalry import cavalry

class Test_All_army(unittest.TestCase):
    #This part is to test the archer
    def test_initialise_life_archer(self):
        test_object = archer().life
        self.assertEqual(3,test_object)
    '''
    def test_initialise_life_archer(self):
        test_object = archer().life
        self.assertEqual(-3,test_object)
    '''
    def test_initialise_exp_archer(self):
        test_object = archer().exp
        self.assertEqual(0,test_object)
    
    '''
    def test_initialise_exp_archer(self):
        test_object = archer().exp
        self.assertEqual(-3,test_object)
    '''
    def test_isAlive_True_archer(self):
        test_object = archer().isAlive()
        self.assertTrue(test_object)
        
    def test_isAlive_False_archer(self):
        test_object = archer()
        test_object.life = 0
        test_object = test_object.isAlive()
        self.assertFalse(test_object)
    '''
    def test_isAlive_False_archer(self):
        test_object = archer()
        test_object.life = -2
        test_object = test_object.isAlive()
        self.assertFalse(test_object)
    '''
    def test_lostLife_archer(self):
        test_object = archer().loseLive(1)
        self.assertEqual(2,test_object)
    '''
    def test_lostLife_archer(self):
        test_object = archer().loseLive(1)
        self.assertEqual(-2,test_object)
    '''
    def test_getExp_archer(self):
        test_object = archer().gainExperience(2)
        self.assertEqual(2,test_object)
    ''' 
    def test_getExp_archer(self):
        test_object = archer().gainExperience(2)
        self.assertEqual(-2,test_object)
    '''
    def test_attack_1_archer(self):
        test_object = archer().attack()
        self.assertEqual(1,test_object)

    def test_attack_2_archer(self):
        test_object = archer()
        test_object.exp = 3
        test_object = test_object.attack()
        self.assertEqual(4,test_object)
    '''
    def test_attack_2_archer(self):
        test_object = archer()
        test_object.exp = 3
        test_object = test_object.attack()
        self.assertEqual(4,test_object)
    '''
    def test_getCost_archer(self):
        test_object = archer().getCost()
        self.assertEqual(2,test_object)
    '''
    def test_getCost_archer(self):
        test_object = archer().getCost()
        self.assertEqual(-4,test_object)
    '''
    def test_getSpeed_archer(self):
        test_object = archer().getSpeed()
        self.assertEqual(3,test_object)

    def test_defend_success_archer(self):
        damage = 1
        test_object = archer().defend(damage)
        self.assertEqual(1,test_object)
    '''
    def test_defend_success_archer(self):
        damage = 4
        test_object = archer().defend(damage)
        self.assertEqual(1,test_object)
    '''
    def test_defend_fail_archer(self):
        damage = 0
        test_object = archer().defend(damage)
        self.assertEqual(1,test_object)

    #This part is to test soldier

    def test_initialise_life_soldier(self):
        test_object = soldier().life
        self.assertEqual(3,test_object)

    def test_initialise_exp_soldier(self):
        test_object = soldier().exp
        self.assertEqual(0,test_object)
        
    def test_isAlive_True_soldier(self):
        test_object = soldier().isAlive()
        self.assertTrue(test_object)

    def test_isAlive_False_soldier(self):
        test_object = soldier()
        test_object.life = 0
        test_object = test_object.isAlive()
        self.assertFalse(test_object)

    def test_lostLife_soldier(self):
        test_object = soldier().loseLive(2)
        self.assertEqual(1,test_object)

    def test_getExp_soldier(self):
        test_object = soldier().gainExperience(3)
        self.assertEqual(3,test_object)

    def test_attack_1_soldier(self):
        test_object = soldier().attack()
        self.assertEqual(1,test_object)

    def test_attack_2_soldier(self):
        test_object = soldier()
        test_object.exp = 2
        test_object = test_object.attack()
        self.assertEqual(3,test_object)

    def test_getCost_soldier(self):
        test_object = soldier().getCost()
        self.assertEqual(1,test_object)

    def test_getSpeed_1_soldier(self):
        test_object = soldier().getSpeed()
        self.assertEqual(1,test_object)

    def test_getSpeed_2_soldier(self):
        test_object = soldier()
        test_object.exp = 3
        test_object = test_object.getSpeed()
        self.assertEqual(4,test_object)

    def test_defend_success_soldier(self):
        damage = 1
        test_object = soldier().defend(damage)
        self.assertEqual(1,test_object)

    def test_defend_fail_soldier(self):
        damage = 1
        test_object = soldier()
        test_object.exp = 2
        test_object = test_object.defend(damage)
        self.assertEqual(0,test_object)

    # This part is to test the cavalry

    def test_initialise_life_cavalry(self):
        test_object = cavalry().life
        self.assertEqual(4,test_object)

    def test_initialise_exp_cavalry(self):
        test_object = cavalry().exp
        self.assertEqual(0,test_object)

    def test_isAlive_True_cavalry(self):
        test_object = cavalry().isAlive()
        self.assertTrue(test_object)

    def test_isAlive_False_cavalry(self):
        test_object = cavalry()
        test_object.life = 0
        test_object = test_object.isAlive()
        self.assertFalse(test_object)

    def test_lostLife_cavalry(self):
        test_object = cavalry().loseLive(2)
        self.assertEqual(2,test_object)

    def test_getExp_cavalry(self):
        test_object = cavalry().gainExperience(3)
        self.assertEqual(3,test_object)

    def test_attack_1_cavalry(self):
        test_object = cavalry().attack()
        self.assertEqual(1,test_object)

    def test_attack_2_cavalry(self):
        test_object = cavalry()
        test_object.exp = 2
        test_object = test_object.attack()
        self.assertEqual(5,test_object)

    def test_getCost_cavalry(self):
        test_object = cavalry().getCost()
        self.assertEqual(3,test_object)

    def test_getSpeed_cavalry(self):
        test_object = cavalry().getSpeed()
        self.assertEqual(2,test_object)

    def test_defend_success_cavalry(self):
        damage = 1
        test_object = cavalry().defend(damage)
        self.assertEqual(1,test_object)

    def test_defend_fail_cavalry(self):
        damage = 1
        test_object = cavalry()
        test_object.exp = 2
        test_object = test_object.defend(damage)
        self.assertEqual(0,test_object)

if __name__ == '__main__':
    unittest.main()
