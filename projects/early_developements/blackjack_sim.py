
import random
def cards():
    
    elevens = 4
    tens = 16
    ones = 4
    twos = 4
    threes = 4
    fours = 4
    fives = 4
    sixs = 4
    sevens = 4
    eights = 4
    nines = 4
    total = elevens + tens + ones + twos + threes + fours + fives + sixs + sevens + eights + nines
    
    
    ten = random.randint(0,1)
    face_card = elevens + tens
    
    if ten <= (face_card / total):
        ten = random.randint(elevens,face_card)
        if ten >= (tens/face_card):
            card_one = 11
            elevens = elevens - 1
        else:
            card_one = 10
            tens = tens - 1
    else:        
        card_one = random.randint(1,9)
        if card_one == 1:
            ones = ones - 1
        elif card_one == 2:
            twos = twos - 1
        elif card_one == 3:
            threes = threes - 1
        elif card_one == 4:
            fours = fours - 1
        elif card_one == 5:
            fives = fives - 1
        elif card_one == 6:
            sixs = sixs - 1
        elif card_one == 7:
            sevens = sevens - 1
        elif card_one == 8:
            eights = eights - 1
        elif card_one == 9:
            nines = nines - 1
    print(card_one)
    
cards()
