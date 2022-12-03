def sum_priorities(input):
  result = 0
  for rucksack in input.split('\n'):
    compartment1 = rucksack[:len(rucksack)//2]
    compartment2 = rucksack[len(rucksack)//2:]
    overlap = list(set(compartment1).intersection(compartment2))[0]
    result += (ord(overlap) - ord('a') + 1) if not overlap.isupper() else (ord(overlap) - ord('A') + 27)
  return result
