import random
from data import data

continueGame = True


def randomPeople():
    randomNumber = random.randint(0, len(data)-1)
    randomNumber2 = random.randint(0, len(data)-1)
    
    personA = data[randomNumber]
    personB = data[randomNumber2]
    
    while personB == personA:
        personB = data[random.randint(0, len(data)-1)]
    
    print(f"Compare A: {personA.get('name')}, {personA.get('description')} from {personA.get('country')}")
    print('VS:')
    print(f"Compare A: {personB.get('name')}, {personB.get('description')} from {personB.get('country')}")
    
    return personA, personB


while continueGame == True:

    person = randomPeople()
    personA = person[0]
    personB = person[1]
    
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    if answer == 'A':
        if personA.get('follower') > personB.get('follower'):
            print('\nBravo!\n')
        else:
            print('\n\nGame over!')
            print(f"{personB.get('name')} has more followers ( {personB.get('follower')} ) than {personA.get('name')} ( {personA.get('follower')} )")
            continueGame = False
    elif answer == 'B':
        if personB.get('follower') > personA.get('follower'):
            print('\nBravo!\n')
        else:
            print('\n\nGame over!')
            print(f"{personA.get('name')} has more followers! ( {personA.get('follower')} ) than {personB.get('name')} ( {personB.get('follower')} )")
            continueGame = False
    else:
        print('\nYou have to answer with "A" or "B" :)\n')