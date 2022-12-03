def get_top3_max_calories_sum(input):
  elf_calories = []
  for elf in input.split('\n\n'):
    elf_calories.append(sum(int(i) for i in elf.split('\n')))
  return sum(sorted(elf_calories, reverse=True)[:3])
