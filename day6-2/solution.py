def find_message(input):
  for i in range(len(input)-14):
    if len(set([input[i+j] for j in range(14)])) == 14:
      return i + 14
