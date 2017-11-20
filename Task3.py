'''
author: Jianchao Wang, Neha Wadhwa
since: 08/05/2015
modified:08/05/2015
'''

from Army import army

# The fighting function
def gladiatorialCombat(player_A_army, player_B_army):
    # if one of the stack is empty, it will jump out of the loop and the game is over
    while not(player_A_army.is_empty() or player_B_army.is_empty()):
        U1 = player_A_army.pop()
        U2 = player_B_army.pop()
        # if one of the unit is dead, it will jump out of the loop and the battle is over
        while U1.life != 0 and U2.life != 0 :
            # here we assign speed two different variable
            U1_speed = U1.getSpeed()
            U2_speed = U2.getSpeed()
            # By comparing two speed, it is deciding who is going to attack first.
            if U1_speed > U2_speed:
                #get Unit 1 damage
                U1_damage = U1.attack()
                #get the Unit 2 lostLife after attacking
                U2_lostLife = U2.defend(U1_damage)
                U2.life -= U2_lostLife
                if U2.isAlive():
                   #get Unit 2 damage
                    U2_damage = U2.attack()
                    #get the Unit 1 lostLife after attacking
                    U1_lostLife = U1.defend(U2_damage)
                    U1.life -= U1_lostLife
                    if not U1.isAlive():
                        break
                else:
                    break
                #check if both of them are alive, they are losing 1 life
                if U1.isAlive():
                    U1.life -= 1
                if U2.isAlive():
                    U2.life -= 1
            elif U1_speed < U2_speed:
                #get Unit 2 damage
                U2_damage = U2.attack()
                #get the Unit 1 lostLife after attacking
                U1_lostLife = U1.defend(U2_damage)
                U1.life -= U1_lostLife
                if U1.isAlive():
                    U1_damage = U1.attack()
                    #get the Unit 2 lostLife after attacking
                    U2_lostLife = U2.defend(U1_damage)
                    U2.life -= U2_lostLife
                    if not U2.isAlive():
                        break
                else:
                    break
                #check if both of them are alive, they are losing 1 life
                if U1.isAlive():
                    U1.life -= 1
                if U2.isAlive():
                    U2.life -= 1
            elif U1_speed == U2_speed:
                #get Unit 1 damage
                U1_damage = U1.attack()
                #get Unit 2 damage
                U2_damage = U2.attack()
                # Unit 1 attack Unit 2
                U2_lostLife = U2.defend(U1_damage)
                # Unit 2 lost life
                U2.life -= U2_lostLife
                # Unit 2 attack Unit 1
                U1_lostLife = U1.defend(U2_damage)
                # Unit 1 lost life
                U1.life -= U1_lostLife
                #check if both of them are alive, they are losing 1 life
                if U1.isAlive():
                    U1.life -= 1
                if U2.isAlive():
                    U2.life -= 1
        # push unit back on the stack
        if U1.life == 0 and U2.life == 0:
            pass
        elif U1.life == 0:
        # If unit 2 alive, we give 1 experience point to this object and push it back
            U2.exp += 1
            player_B_army.push(U2)
        elif U2.life == 0:
        # If unit 1 alive, we give 1 experience point to this object and push it back
            U1.exp += 1
            player_A_army.push(U1)

        #print(player_A_army)
        #print(player_B_army)
    if player_A_army.is_empty() and player_B_army.is_empty():
        remaining = []
        remaining.append("draw")
        return remaining

    elif player_A_army.is_empty():
        remaining = []
        remaining.append("B")
        while not player_B_army.is_empty():
            remaining.append(player_B_army.pop())
        return remaining

    elif player_B_army.is_empty():
        remaining = []
        remaining.append("A")
        while not player_A_army.is_empty():
            remaining.append(player_A_army.pop())
        return remaining



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
            raise ValueError
        break
    except ValueError:
        pass

player_A_army = player_A.setUp()
'''
while not player_A.stack.top is None:
    army_A.append(player_A_army.pop())
print(army_A)
'''
print("")
print("Set up Player 2")
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
######################################
print("")
print(name_B + " choose your army as S A C")
print("where S is the number of soldiers")
print("      A is the number of archers")
print("  and C is the number of cavalry")
while True:
    try:
        command = int(input("Press 1 to build up your army: "))
        if command != 1:
            raise ValueError
        break
    except ValueError:
        pass

player_B_army = player_B.setUp()
'''
while not player_B.stack.top is None:
    army_B.append(player_B_army.pop())
print(army_B)
'''
while True:
    try:
        command = int(input("Enter 1 to begin the combat: "))
        if command == 1:
            break
        else:
            raise ValueError
    except ValueError:
        pass
winner_list = gladiatorialCombat(player_A_army, player_B_army)
winner = winner_list[0]
if winner == "draw":
    print("No one win this game.")
elif winner == "A":
    print("The winner is "+ str(name_A))
    for i in range(1,len(winner_list)):
        print(str(winner_list[i]))
elif winner == "B":
    print("The winner is " + str(name_B))
    for i in range(1,len(winner_list)):
        print(str(winner_list[i]))
