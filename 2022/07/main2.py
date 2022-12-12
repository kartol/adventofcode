puzzle = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def du(self):
        return self.size


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = {}
        self.directories = {}

    def add_file(self, file: File):
        self.files[file.name] = file

    def add_directory(self, directory):
        self.directories[directory.name] = directory

    def du(self):
        s = sum([each.du() for each in [*self.files.values(), *self.directories.values()]])
        return s

    def list_dirs(self):
        return [d.du() for d in self.directories.values()] \
               + [d.list_dirs() for d in self.directories.values()]


class FS:

    def __init__(self):
        self.root_directory = Directory('/', None)
        self.current_directory = self.root_directory

    def cd(self, where):
        match where:
            case '..':
                self.current_directory = self.current_directory.parent
            case '/':
                self.current_directory = self.root_directory
            case _:
                self.current_directory = self.current_directory.directories[where]

    def list_dirs(self):
        return [self.root_directory.du()] + self.root_directory.list_dirs()


fs = FS()
for command in puzzle.split('$ '):
    if command.startswith('cd'):
        where = command.split('\n')[0].split(' ')[1]
        fs.cd(where)
    else:
        for entry in command.split('\n')[1:-1]:
            match entry.split(' '):
                case ['dir', name]:
                    fs.current_directory.add_directory(Directory(name, fs.current_directory))
                case [size, name]:
                    fs.current_directory.add_file(File(name, int(size)))


def flatten(items):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if isinstance(x, list):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x


empty = 70000000 - fs.root_directory.du()
need = 30000000 - empty
print(sorted([each for each in flatten(fs.list_dirs()) if each >= need])[0])
