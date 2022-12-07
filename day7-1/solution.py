class Directory:
  def __init__(self, name, parent=None):
    self.name = name
    self.parent=parent
    self.files={}
    self.children={}

  def get_size(self):
    size = 0
    for _, sz in self.files.items():
      size += sz
    for _, child in self.children.items():
      size += child.get_size()
    return size

def parse_input(input):
  current_dir = Directory('/')
  directories = {'/': current_dir}
  for line in input.split('\n'):
    ln = line.split(' ')
    if ln[0] == '$':
      if ln[1] == 'cd':
        if ln[2] == '..' and current_dir.parent is not None:
          current_dir = current_dir.parent
        elif ln[2] == '/':
          current_dir = directories[ln[2]]
        elif ln[2] != '..':
          current_dir = directories[current_dir.name+'/'+ln[2]]
    else:
      if ln[0] == 'dir':
        name = current_dir.name + '/' + ln[1]
        if name not in directories:
          directories[name] = Directory(name, current_dir)
        if name not in current_dir.children:
          current_dir.children[name] = directories[name]
      else:
        if ln[1] not in current_dir.files:
          current_dir.files[ln[1]] = int(ln[0])
  return directories

def sum_dir_sizes(input):
  directories = parse_input(input)
  total = 0
  for name, dir in directories.items():
    dir_size = dir.get_size()
    print(name, dir_size)
    if dir_size <= 100000:
      total += dir_size
  return total
