import random


stick_og = 1
first_break = int(input("At what percent would you like to break the stick (Just number): "))/100

attempts = 0
success = 0

while True:
    stick_one = stick_og - first_break
    stick_two = first_break
    
    pieces = [stick_one, stick_two]
    
    piece_index = random.randint(0, len(pieces) - 1)
    piece_to_break = pieces[piece_index]
    
    
    random_point = random.uniform(0, piece_to_break)
    
    
    piece_a = random_point
    piece_b = piece_to_break - random_point
    
    pieces.pop(piece_index)
    pieces.append(piece_a)
    pieces.append(piece_b)
    
    attempts = attempts + 1
    
    
    if max(pieces) < 0.5:
        success = success + 1
    
    if success > 1000:
        break
    
print("Attempts: " + str(attempts))
print("Successes: " + str(success))
print("Probability: " + str((success/attempts)*100))
