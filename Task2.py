'''
author: Jianchao Wang, Neha Wadhwa
since: 08/05/2015
modified:08/05/2015
'''

from Army import army

__main__ = "main program"
army_A = []
army_B = []
print("")
print("Set up Player 1")
name_A = str(input("Enter your name here: "))
player_A = army(name_A)
print("")
print(name_A + " choose your army as S A C")
print("where S is the number of soldiers")
print("      A is the number of archers")
print("  and C is the number of cavalry")
while True:
    try:
        command = int(input("Press 1 to build up your army: "))
        if command != 1:
            raise Exception
        break
    except :
        print("Please enter valid number here")

player_A_army = player_A.setUp()

while not player_A.stack.top is None:
    army_A.append(player_A_army.pop().type())
print(army_A)

print("")
print("Set up Player 2")
name_B = ''
while True:
    try:
        name_B = str(input("Enter your name here: "))
        player_B = army(name_B)
        if player_B.player == player_A.player:
            raise Exception
        break
    except:
        print("You cannot enter the same name")
        pass

##############################
print("")
print(name_B + " choose your army as S A C")
print("where S is the number of soldiers")
print("      A is the number of archers")
print("  and C is the number of cavalry")
while True:
    try:
        command = int(input("Press 1 to build up your army: "))
        if command != 1:
            raise Exception
        break
    except:
        print("Please Enter value number here")


player_B_army = player_B.setUp()

while not player_B.stack.top is None:
    army_B.append(player_B_army.pop().type())
print(army_B)
