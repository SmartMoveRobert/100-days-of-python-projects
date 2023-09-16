#100DaysofPython - Day 3 Project - Treasure Island Text Adventure

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('You\'ve come onto a crossroads. Would you go "left" or "right"? \n').lower()

if choice1 == "left":
  choice2 = input('You\'ve come upon a motorised bridge. You are afraid the noise from the bridge forming will attract unwanted attention. you can either "wait" for the bridge to come down or "swim" across the river.\n').lower()
  if choice2 == "wait":
    choice3 = input("You reached upon a warehouse. It presents you with three doors to walk through. Red. Yellow. Blue. Which one will you walk through?\n").lower()
    if choice3 == "red":
      print("You walk through the red door, unknowingly triggering the traps and are burned by the chemical fire. Game Over.")
    elif choice3 == "yellow":
      print("You open the door and infront of you lies a crate, you open it and you see the old familiar glint of gold. You Win!")
    elif choice3 == "blue":
      print("A bunch of zombie swarmed on you as you opened the door and eats your face alive. Game Over.")
    else:
      print("You chose something that doesn't exist. the void consumes you. Game Over.")  
  else:
    print("You are attacked by a school of mutated trout. Game Over.")   
else:
  print("You fell into a hole. Game Over.")