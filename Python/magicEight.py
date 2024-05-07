import random

question = input('Question:      ')

num1 = "Yes - definitely."
num2 = "It is decidedly so."
num3 = "Without a doubt."
num4 = "Reply hazy, try again."
num5 = "Ask again later."
num6 = "Better not tell you now."
num7 = "My sources say no."
num8 = "Outlook not so good."
num9 = "Very doubtful."

random_number = random.randint(1, 9)  # Generate a random number between 1 and 9

# Access the response based on the random number
if random_number == 1:
    response = num1
elif random_number == 2:
    response = num2
elif random_number == 3:
    response = num3
elif random_number == 4:
    response = num4
elif random_number == 5:
    response = num5
elif random_number == 6:
    response = num6
elif random_number == 7:
    response = num7
elif random_number == 8:
    response = num8
else:
    response = num9

print("Magic 8 Ball:", response)