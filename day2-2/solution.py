shape_score = {'A': 1, 'B': 2, 'C': 3}
winner = {'A': 'C', 'B': 'A', 'C': 'B'}
loser = {'C': 'A', 'A': 'B', 'B': 'C'}
outcome_score = {'X': 0, 'Y': 3, 'Z': 6}
def shape_score_from_outcome(opponent, outcome):
  if outcome == 'Y':
    return shape_score[opponent]
  if outcome == 'X':
    return shape_score[winner[opponent]]
  return shape_score[loser[opponent]]

def get_score(input):
  score = 0
  for round in input.split('\n'):
    score += shape_score_from_outcome(round.split(' ')[0], round.split(' ')[1]) + outcome_score[round.split(' ')[0]]
  return score
