def check_guess(guess, answer):
    global  score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct Answer')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = attempt + 1

    if attempt == 3:
        print('The correct answer is ' + answer)

score = 0
print('Guess the Pokémon')
guess1 = input('Which Pokémon is a dragon and a fire type:')
check_guess(guess1, 'charzard')
guess2 = input ('which Pokémon is shape like a ball and is a ghost type:')
check_guess (guess2, 'gastly')
guess3 = input ('which Pokémon is the most fast sprinter')
check_guess (guess3, 'rapidash')
guess4 = input ('which team in Pokémon starts with a r')
check_guess (guess4, 'team rocket')
guess5 = input ('which Pokémon is a mother and is like a kangaro')
check_guess (guess5, 'kangaskhan')
guess6 = input ('which of ash Pokémon can mega evalotion in Pokémon xyz')
check_guess (guess6, 'ash grininja')
