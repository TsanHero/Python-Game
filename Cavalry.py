'''
author: Jianchao Wang, Neha Wadhwa
since: 08/05/2015
modified: 08/05/2015
'''


class cavalry:
    '''
    instantiate an object
    Input:
    Precondition:
    Postcondition: instantiate an cavalry object
    Return:
    Complexity: Best and worst O(1)
    '''
    def __init__(self):
        self.life = 4
        self.exp = 0
    '''
    check if the archer is alive(comparing the life)
    Input:
    Precondition:
    Postcondition: return a boolean variable
    Return:True or False
    Complexity: Best and worst O(1)
    '''
    def isAlive(self):
        if self.life > 0:
            return True
        else:
            return False
    '''
    reduce the life with a lostLife number
    Input: valid integer number
    Precondition:
    Postcondition: life is decreased
    Return: life
    Complexity: Best and worst O(1)
    '''
    def loseLive(self,lostLife):
        try:
            if lostLife < 0:
                raise ValueError
        except ValueError:
            raise("The lostLife is negative.")

        self.life -= lostLife
        return self.life
    '''
    increasing experience
    Input: valid integer number
    Precondition:
    Postcondition: experience is increasing
    Return: exp
    Complexity: Best and worst O(1)
    '''
    def gainExperience(self,gainedExperience):
        try:
            if gainedExperience < 0:
                raise ValueError
        except ValueError:
            raise("The Experience is negative.")

        self.exp = self.exp + gainedExperience
        return self.exp
    '''
    extract the cost of each unit
    Input:
    Precondition:
    Postcondition: get the price and return the price
    Return: cost
    Complexity: Best and worst O(1)
    '''
    def getCost(self):
        cavalry_cost = 3
        return cavalry_cost
    '''
    extract the speed of each unit
    Input:
    Precondition:
    Postcondition: get the speed and return the speed
    Return: speed
    Complexity: Best and worst O(1)
    '''
    def getSpeed(self):
        cavalry_speed = 2
        return cavalry_speed
    '''
    extract the damage of each unit
    Input:
    Precondition:
    Postcondition: get the damage and return the damage
    Return: damage
    Complexity: Best and worst O(1)
    '''
    def attack(self):
        cavalry_damage = self.exp*2 + 1
        return cavalry_damage
    '''
    unit need to defend the coming damage by comparing the input attack and exp
    Input: attack
    Precondition:
    Postcondition: it will lose 1 life or will not lose life.
    Return: lostLife
    Complexity: Best and worst O(1)
    '''
    def defend(self,damage):
        try:
            if damage < 0:
                raise ValueError
        except ValueError:
            raise("The damage value is negative.")

        if damage > self.exp/2:
            lost = 1
        else:
            lost = 0
        return lost

    '''
    Here we redefine the method str() to print out a customize string
    Input:
    Precondition:
    Postcondition: print out a customize string
    Return: string
    Complexity: Best and worst O(1)
    '''
    def __str__(self):
        string = str("This unit is cavalry " + "Life: " + str(self.life) + " Experience: " + str(self.exp))
        return string

    def type(self):
        item = "cavalry"
        return item
