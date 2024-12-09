def next_number(str_disk):
    for each in str_disk:
        if each != ".":
            yield each


def part_one(puzzle_input):
    disk = [int(each) for each in puzzle_input]
    str_disk = []
    for i, each in enumerate(disk):
        if i % 2 == 0:
            str_disk += [str(i // 2)] * each
        else:
            str_disk += ["."] * each

    file_blocks = sum(each != "." for each in str_disk)

    def_disk = []
    last_number = next_number(str_disk[::-1])
    for i in range(file_blocks):
        if str_disk[i] == ".":
            def_disk.append(next(last_number))
        else:
            def_disk.append(str_disk[i])

    answer = sum(i * int(each) for i, each in enumerate(def_disk))
    print(answer)


class Block:
    def __init__(self, id, size):
        self.id = id
        self.size = size


class Disk:
    def __init__(self):
        self.disk: list[Block] = []

    def add(self, block: Block):
        self.disk.append(block)

    def next_file(self):
        files = [file for file in self.disk if file.id != -1]
        for file in files[::-1]:
            yield file

    def next_empty_space(self, file_idx):
        for idx, block in enumerate(self.disk[:file_idx]):
            if block.id == -1:
                yield idx, block

    def file_index(self, file_id):
        for idx, file in enumerate(self.disk):
            if file.id == file_id:
                return idx

    def __str__(self):
        a = []
        for each in self.disk:
            if each.id == -1:
                a += ["."] * each.size
            else:
                a += [str(each.id)] * each.size
        return "".join(a)


def part_two(puzzle_input):
    disk = Disk()
    for i, size in enumerate([int(each) for each in puzzle_input]):
        if i % 2 == 0:
            disk.add(Block(i // 2, size))
        else:
            disk.add(Block(-1, size))

    for file in disk.next_file():
        file_idx = disk.file_index(file.id)
        for idx, empty_space in disk.next_empty_space(file_idx):
            if file.size > empty_space.size:
                continue
            if file.size == empty_space.size:
                empty_space.id, file.id = file.id, empty_space.id
                break

            disk.disk[idx : idx + 1] = [Block(file.id, file.size), Block(-1, empty_space.size - file.size)]
            file.id = -1
            break

    def_disk = []
    for each in disk.disk:
        if each.id == -1:
            def_disk += ["."] * each.size
        else:
            def_disk += [each.id] * each.size
    answer = sum(i * each for i, each in enumerate(def_disk) if each != ".")
    print(answer)


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.example)
    part_one(puzzle.input)
    part_two(puzzle.example)
    part_two(puzzle.input)
