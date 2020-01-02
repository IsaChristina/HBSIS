import random

def player(name = None):
    name = input('Insert your name:')
    return name

player = player()

cards = [{"2": 2}, {"3": 3}, {"4": 4}, {"5": 5}, {"6": 6}, {"7": 7}, {"8": 8},
            {"9": 9}, {"10": 10}, {"A": 1}, {"J": 10}, {"J": 10}, {"Q": 10}, {"K": 10}]

random.shuffle(cards)

score = 0
answer = ''
suit_card = ''
value_card = 0

while score < 22:

    while answer.upper() != 'T' and answer.upper() != 'E':
        answer = input('Turn one more card or exit? [T - Turn] [E - Exit]')

    if answer.upper() == 'T':

        get_card = random.choice(cards)

        suit_card = list(get_card)[0]
        value_card = list(get_card.values())[0]

        if suit_card == "A" and score == 0:
            value_card = 11
            score += value_card
        else:
            score += value_card

        if score == 21:
            print(f'*** CONGRATULATIONS {player.upper()}, YOU WIN THE GAME ***')
            print('=== GAME DATA ===')
            print(f'Suit: {suit_card}')
            print(f'Value: {value_card}')
            print(f'Score: {score}')
            break

        if score > 21:
            print(f'*** OH NO {player.upper()}, YOU LOSE ***')
            print('=== GAME DATA ===')
            print(f'Suit: {suit_card}')
            print(f'Value: {value_card}')
            print(f'Score: {score}')
            break

    if answer.upper() == 'E':
        print('=== TOTAL SCORE ===')
        print(f'Score: {score}')
        break

    answer = ''

    print('=== GAME DATA ===')
    print(f'Suit: {suit_card}')
    print(f'Value: {value_card}')
    print(f'Score: {score}')