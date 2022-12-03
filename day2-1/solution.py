shape_score = {'X': 1, 'Y': 2, 'Z': 3}
convert = {'X': 'A', 'Y': 'B', 'Z': 'Z'}
winner = {'A': 'C', 'B': 'A', 'C': 'B'}
def outcome_score(opponent, you):
  if opponent == convert[you]:
    return 3
  if winner[opponent] == convert[you]:
    return 0
  return 6

def get_score(input):
  score = 0
  for round in input.split('\n'):
    score += shape_score[round.split(' ')[1]] + outcome_score(round.split(' ')[0], round.split(' ')[1])
  return score
