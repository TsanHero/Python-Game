'''
author: Jianchao Wang, Neha Wadhwa
since: 08/05/2015
modified:08/05/2015
This task is providing a menu for users to choose
Input: valid integer number
Precondition:
Postcondition: Buying a item
Return:
Complexity: Best and worst O(1)

'''
from Soldier import soldier
from Archer import archer
from Cavalry import cavalry

def menu():
    print("")
    print("Welcome to the game of which I don't even know the name")
    print("Menu")
    print("1. Buy Soldier")
    print("2. Buy Archer")
    print("3. Buy Cavalry")
    print("4. End")





__main__ = 'Main Program'

money = 20
quit = True
army_list = []

while quit:
    menu()
    print("Your Balance: "+ "$" + str(money))
    # Here to print out the army that you have bought.
    if len(army_list) > 0:
        print("Your military:")
        for i in range(len(army_list)):
            print(army_list[i])
    else:
        print("Your don't even have an army")
    print("")

    while True:
        try:
            command = int(input("Please Enter your choice here: "))
            break
        except:
            print("Please enter valid input.")

    if command == 1:
        # here we do exception handling if the budget is not enough for buying an soldier
        while True:
            try:
                if money < 1:
                    raise ValueError
                break
            except ValueError:
                raise ValueError("Your Balance is less than 1")
        # create an object of soldier
        S1 = soldier()
        # After each purchasing, reduce the money from the wallet
        money -= S1.getCost()
        # append the army in the list, which consisted of your military.
        army_list.append(str("solider"))

    if command == 2:
        # here we do exception handling if the budget is not enough for buying an archer
        try:
            if money < 2:
                raise ValueError
        except ValueError:
            raise ValueError("Your Balance is less than 2")
        # create an object of archer
        A1 = archer()
        # after each purchasing, reduce the money from the wallet
        money -= A1.getCost()
        # append the army in the list, which consisted of your military.
        army_list.append(str("soldier"))

    if command == 3:
        # here we do exception handling if the budget is not enough for buying an cavalry
        while True:
            try:
                if money < 3:
                    raise ValueError
                break
            except ValueError:
                raise ValueError("Your Balance is less than 3")
        # create an object of cavalry
        C1 = cavalry()
        # After each purchasing, reduce the money from the wallet
        money -= C1.getCost()
        # append the army in the list, which consisted of your military.
        army_list.append(str("cavalry"))

    if command == 4:
        quit = False

    if command < 1 or command > 4:
        print("please enter an valid number.")

