#Game variables 

#Intro
intro = "Lets rob a bank"
introQ1 = input("What is your name:  ")
introQ2 = int(input("Is that your real name? 1. yes, 2. no:  "))

#scene one
sceneOne = "We are off to a good start. As we approuch the building we notice three points of entry. "
scene1Q1 = int(input("Where should we enter? 1. Main Entrance, 2. Side Entrance, 3. Back Entrance:  "))

#scene two
sceneTwo = "We were able to enter without alerting the cops. we notice that the door to the vault is locked "
scene2Q1 = int(input("Would you like to pick the lock? 1. Yes, 2. No:  "))

#game play 

#Intro gameplay 
if introQ2 == 1:
    print("ARRESTED: Unfortunately the cops were able to identify you")      
elif introQ2 == 2: 
    print(sceneOne)
else:
    print("Number entered not recognized , try again later")
    
#Scene one gameplay
if scene1Q1 == 1:
    print("ARRESTED: Unfortunately the cops were on the otherside of the main entrance")      
elif scene1Q1 == 2: 
    print(sceneTwo)
elif scene1Q1 == 3:
    print(sceneTwo)
else:
    print("Number entered not recognized , try again later")