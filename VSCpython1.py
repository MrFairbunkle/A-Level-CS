import random

playerHealth = 200
monsterHealth = 100
turns=0
healPots=3
manaPots=3

def game():
    global playerHealth, monsterHealth, turns
    
    while playerHealth > 0 and monsterHealth > 0:
        diceRollArray = []
        
        for i in range(5):
            diceRollArray.append(random.randint(1, 6))

        choice=input("Do you want to: A. take your turn, or B. use an item? ")
        choice=choice.upper()
        if choice=="A":
            total = sum(diceRollArray)
            print(f"Turn {turns+1}")
            print(f"You rolled {diceRollArray} and got a total of {total}.")
            
            if total < 20:
                playerHealth -= 10
                print(f"Player lost 10 health and now has {playerHealth} health left.\n")
            else:
                monsterHealth -= 10
                print(f"Monster lost 10 health and now has {monsterHealth} health left.\n")
            turns+=1
        elif choice=="B":
            bagChoice=input(f"You have {healPots} Heal Potions and {manaPots} Mana Potions. What would you like to do?\nA. Use a Heal Pot (Qty:{healPots})\nB. Use a Mana Pot (Qty:{manaPots})\nC. Exit bag")
        else:
            print("Not a valid option")

        

    if playerHealth<=0:
        print(f"\n\nPlayer lost in {turns} turns.")
    else:
        print(f"\n\nPlayer won in {turns} turns.")

game()
