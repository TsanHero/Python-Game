'''
author: Jianchao Wang, Neha Wadhwa
since: 08/05/2015
modified:08/05/2015

'''
from Soldier import soldier
from Archer import archer
from Cavalry import cavalry
from Stack import stack

class army:

    '''
    instantiate an object
    Input: valid integer number
    Precondition:
    Postcondition: instantiate an player object
    Return:
    Complexity: Best and worst O(1)
    '''

    def __init__(self,player_name):
        self.player = player_name
        self.stack = stack()
        self.cost = 20
    '''
    Here we buy the army and push them on the stack
    Input:
    Precondition:
    Postcondition: form an army and return a stack
    Return: a stack
    Complexity: Best O(1) and worst O(n)
    n is the number of purchased army
    '''
    def setUp(self):
        #instantiate all the army
        self.fighter_solider = soldier()
        self.fighter_archer = archer()
        self.fighter_cavalry = cavalry()
        #get the price of each type of army
        self.cost_solider = self.fighter_solider.getCost()
        self.cost_archer = self.fighter_archer.getCost()
        self.cost_cavalry = self.fighter_cavalry.getCost()

        while True:
            # Here we need to validate if the input is not integer
            try:
                self.n_soldier = int(input("S: "))
                self.n_archer = int(input("A: "))
                self.n_cavalry = int(input("C: "))
            except:
                print("Please Enter valid input.")
                pass
            # Here we need to validate the total cost if it is greater than the budget
            try:
                print("")
                self.n_soldier = int(self.n_soldier)
                self.n_archer = int(self.n_archer)
                self.n_cavalry = int(self.n_cavalry)
                # to find out the total cost
                total_cost = (self.n_soldier * self.cost_solider + self.n_archer * self.cost_archer +
                          self.n_cavalry * self.cost_cavalry)
                # check if the inputs are positive number
                if self.n_soldier < 0 or self.n_archer < 0 or self.n_cavalry < 0:
                   raise IndexError
                # check if the total cost is greater than the budget
                elif total_cost > self.cost:
                    raise ValueError
                break
            except ValueError:
                
                print("Dude! You don't have enough money to build up the army.")
                
                
            except IndexError:
                
                print("You cannot buy negative number of military.")
                
                
        # push each army object on the stack
        if self.n_cavalry > 0:
            for i in range(int(self.n_cavalry)):
                # instantiate an cavalry object and push to the stack
                self.stack.push(cavalry())
        if self.n_archer > 0:
            for j in range(int(self.n_archer)):
                # instantiate an archer object and push to the stack
                self.stack.push(archer())
        if self.n_soldier > 0:
            for k in range(int(self.n_soldier)):
                # instantiate an soldier object and push to the stack
                self.stack.push(soldier())

        return self.stack


