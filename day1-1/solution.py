def get_max_calories(input):
  elf_calories = []
  for elf in input.split('\n\n'):
    elf_calories.append(sum(int(i) for i in elf.split('\n')))
  return max(elf_calories)
