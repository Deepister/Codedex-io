# Initialize house points
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

q1 = int(input("Do you like Dawn or Dusk? 1. Dawn, 2. Dusk:  "))

if q1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif q1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input for question 1")

# Question 2
q2 = int(input("When I'm dead, I want people to remember me as: 1. The Good, 2. The Great, 3. The Wise, 4. The Bold:  "))
if q2 == 1:
    Hufflepuff += 2
elif q2 == 2:
    Slytherin += 2
elif q2 == 3:
    Ravenclaw += 2
elif q2 == 4:
    Gryffindor += 2
else:
    print("Wrong input for question 2")

# Question 3
q3 = int(input("Which kind of instrument most pleases your ear? 1. The violin, 2. The trumpet, 3. The piano, 4. The drum:  "))
if q3 == 1:
    Hufflepuff += 1
elif q3 == 2:
    Slytherin += 2
elif q3 == 3:
    Ravenclaw += 1
elif q3 == 4:
    Gryffindor += 2
else:
    print("Wrong input for question 3")
    
# Determine the house with the most points
max_points = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)

if Gryffindor == max_points:
    print("The house with the most points is: Gryffindor")
elif Ravenclaw == max_points:
    print("The house with the most points is: Ravenclaw")
elif Hufflepuff == max_points:
    print("The house with the most points is: Hufflepuff")
else:
    print("The house with the most points is: Slytherin")