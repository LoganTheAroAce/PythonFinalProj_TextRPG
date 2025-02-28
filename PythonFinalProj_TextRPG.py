#Logan Parrell :3
#Text Based RPG Fight

#imports the random library
import random
#All the Variables that change
playerhealth = 100
bosshealth = 500
blockchance = 0
turn = 0

#Asks for player name
name = input("Name:")

#Starts The Fight
while bosshealth >= 0:
    while turn == 0:
        print(name,":", playerhealth, "Health")
        print("John Code:", bosshealth, "Health")
        choice = input(")-Fight-(    )-Spells-(")
        if choice == "Fight":
            print("You Attack John Code!")
            damage = random.randint(10,20)
            bosshealth = bosshealth - damage
            print("You Dealt", damage, "Damage!")
            turn = 1
        elif choice == "Spells":
            spell = input(")-Hack (20 Damage)-(   )-Heal (25+ HP)-(   )-gun-(")
            if spell == "Hack":
                successchance = random.randint(0, 10)
                if successchance >= 5:
                    print("You Used Hack!")
                    bosshealth = bosshealth - 20
                    turn = 1
                else:
                    print("The Attack Failed!")
                    turn = 1
            elif spell == "Heal":
                healamount = random.randint(25, 100)
                if playerhealth >= 50:
                    successchance = random.randint(0, 100)
                    if successchance >= 2:
                        print("You Used Heal!")
                        playerhealth = playerhealth + healamount
                        print("You Healed", healamount, "HP!")
                        turn = 1
                    else:
                        print("Somehow, Despite making it very unlikely to fail this spell when under 50 hp, the spell failed.")
                        turn = 1
                else:
                    successchance = random.randint(0, 10)
                    if successchance >= 2:
                        print("You Used Heal!")
                        playerhealth = playerhealth + healamount
                        print("You Healed", healamount, "HP!")
                        turn = 1
                    else:
                        print("The Spell Failed!")
                        turn = 1
            elif spell == "gun":
                successchance = random.randint(1, 1000)
                if successchance == 1:
                    print("You Pull Out A Gun!")
                    bosshealth = bosshealth - 500
                    print("You Killed John Code!")
                else:
                    print ("Try Again :)")
                    turn = 1
            else:
                print("Invalid Spell!")
                spell = input(")-Hack (20 Damage)-(   )-Heal (25+ HP)-(   )-gun-(")
        else:
            print("...what?")
            print("you... you do know that you can only use the options i give you, right?")
            print("here, lets try again.")
            choice = input(")-Fight-(    )-Spells-(")
    blockchance = blockchance + random.randint(1, 2)
    while turn == 1:
        print("John Code Attacks!")
        if blockchance == 10:
            print("John Code Misses!")
            turn = 0
        else:
            bossattack = random.randint(5, 20)
            playerhealth = playerhealth - bossattack
            print("John Code Delt", bossattack, "Damage!")
            turn = 0
print(name, "Wins!")