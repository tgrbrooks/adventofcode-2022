def sum_priorities(input):
  result = 0
  rucksacks = input.split('\n')
  for i in range(0, len(rucksacks), 3):
    elf1 = rucksacks[i]
    elf2 = rucksacks[i+1]
    elf3 = rucksacks[i+2]
    badge = list(set(set(elf1).intersection(elf2)).intersection(elf3))[0]
    result += (ord(badge) - ord('a') + 1) if not badge.isupper() else (ord(badge) - ord('A') + 27)
  return result
