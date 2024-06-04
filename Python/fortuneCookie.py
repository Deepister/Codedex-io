import random

fortune1 = "Don't pursue happiness, create it."
fortune2 = "All things are difficult before they are easy."
fortune3 = "The early bird gets the worm, but the second mouse gets the cheese."
fortune4 = "Someone in your life needs a letter from you."
fortune5 = "Don't just think. Act!"
fortune6 = "Your heart will skip a beat."
fortune7 = "The fortune you search for is in another cookie."
fortune8 = "Help! I'm being held prisoner in a Chinese bakery!"

def fortune():
    fortunes = [fortune1, fortune2, fortune3, fortune4, fortune5, fortune6, fortune7, fortune8]
    random_fortune = random.randint(0, 7)
    print(fortunes[random_fortune])

fortune()


