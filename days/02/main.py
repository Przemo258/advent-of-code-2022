def convert(text: str):
    # Rock
    if text == 'A' or text == 'X':
        return 1
    # Paper
    elif text == 'B' or text == 'Y':
        return 2
    # Scissors
    elif text == 'C' or text == 'Z':
        return 3


def battle(opponent_input: str, player_input: str) -> int:
    opponent = convert(opponent_input)
    player = convert(player_input)

    # draw
    if player == opponent:
        return player + 3
    # win
    elif (player == 1 and opponent == 3) or (player == 2 and opponent == 1) or (player == 3 and opponent == 2):
        return player + 6
    # lose
    else:
        return player


def choose_shape(opponent_input: str, result: str) -> str:
    # draw
    if result == 'Y':
        return opponent_input
    # win
    elif result == 'Z':
        if opponent_input == 'C':
            return 'A'
        elif opponent_input == 'A':
            return 'B'
        else:
            return 'C'
    # lose
    else:
        if opponent_input == 'C':
            return 'B'
        elif opponent_input == 'A':
            return 'C'
        else:
            return 'A'


score = 0
with open('input.txt', 'r') as file:
    data = file.read()
    games = data.split('\n')
    for game in games:
        inputs = game.split()
        # part 1
        # score += battle(inputs[0], inputs[1])
        # part 2
        shape = choose_shape(inputs[0], inputs[1])
        score += battle(inputs[0], shape)

print(score)
