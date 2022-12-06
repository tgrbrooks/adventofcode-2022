def find_marker(input):
  for i in range(len(input) - 4):
    if len(set([input[i], input[i+1], input[i+2], input[i+3]])) == 4:
      return i + 4
