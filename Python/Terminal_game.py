# Game variables 

# Intro
intro = "Let's rob a bank"

print(intro)

# Scene one
sceneOne = "We are off to a good start. As we approach the building we notice three points of entry."
scene1Q1 = 0  # Initialize scene1Q1

# Scene two
sceneTwo = "We were able to enter without alerting the cops. We notice that the door to the vault is locked."
scene2Q1 = 0  # Initialize scene2Q1

# Scene three
sceneThree = "We are now facing the vault door. Do you want to pick the lock?"
scene3Q1 = 0  # Initialize scene3Q1

# Intro gameplay 
introQ1 = input("What is your name:  ")
introQ2 = int(input("Is that your real name? 1. yes, 2. no:  "))

if introQ2 == 1:
    print("ARRESTED: Unfortunately, the cops were able to identify you")      
elif introQ2 == 2: 
    print(sceneOne)
    # Scene one description and gameplay
    scene1Q1 = int(input("Where should we enter? 1. Main Entrance, 2. Side Entrance, 3. Back Entrance:  "))
    
    if scene1Q1 == 1:
        print("ARRESTED: Unfortunately, the cops were on the other side of the main entrance")      
    elif scene1Q1 == 2: 
        print(sceneTwo)
        # Scene two description and gameplay
        scene2Q1 = int(input("Would you like to pick the lock? 1. Yes, 2. No: "))
        
        if scene2Q1 == 1:
            print(sceneThree)
            # Scene three description and gameplay
            scene3Q1 = int(input("Would you like to pick the lock? 1. Yes, 2. No: "))
            if scene3Q1 == 1:
                print("You have chosen to pick the lock.")
                # Picking the lock mechanics
                attempts = 5
                while attempts > 0:
                    code = input("Enter the code (4 digits): ")
                    if code == "1234":
                        print("You successfully unlocked the door!")
                        break
                    else:
                        print("Wrong code. Try again.")
                        attempts -= 1
                else:
                    print("You failed to unlock the door. The cops arrive and you're arrested.")
            elif scene3Q1 == 2:
                print("You chose not to pick the lock. You walk out of the bank freely.")
            else:
                print("Number entered not recognized, try again later")
        elif scene2Q1 == 2:
            print("You chose not to pick the lock. The cops arrive and you're arrested.")
        else:
            print("Number entered not recognized, try again later")
    elif scene1Q1 == 3:
        print(sceneTwo)
        # Scene two description and gameplay
        scene2Q1 = int(input("Would you like to pick the lock? 1. Yes, 2. No: "))
        
        if scene2Q1 == 1:
            print(sceneThree)
            # Scene three description and gameplay
            scene3Q1 = int(input("Would you like to pick the lock? 1. Yes, 2. No: "))
            if scene3Q1 == 1:
                print("You have chosen to pick the lock.")
                # Picking the lock mechanics
                attempts = 5
                while attempts > 0:
                    code = input("Enter the code (4 digits): ")
                    if code == "1234":
                        print("You successfully unlocked the door!")
                        break
                    else:
                        print("Wrong code. Try again.")
                        attempts -= 1
                else:
                    print("You failed to unlock the door. The cops arrive and you're arrested.")
            elif scene3Q1 == 2:
                print("You chose not to pick the lock. You walk out of the bank freely.")
            else:
                print("Number entered not recognized, try again later")
        elif scene2Q1 == 2:
            print("You chose not to pick the lock. The cops arrive and you're arrested.")
        else:
            print("Number entered not recognized, try again later")
    else:
        print("Number entered not recognized, try again later")
else:
    print("Number entered not recognized, try again later")
