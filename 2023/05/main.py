import puzzle


class Mapping:
    def __init__(self):
        self.ranges = []

    def update(self, source, destination, length):
        self.ranges.append((source, destination, length))

    def get_destination(self, source_number):
        for source, destination, length in self.ranges:
            if source <= source_number < source + length:
                dist = source_number - source
                return destination + dist
        return source_number


def parse_seeds(seed_line):
    return [int(each) for each in seed_line.split()[1:]]


def parse_mapping(mapping_string):
    mapping = Mapping()
    for line in mapping_string.split("\n")[1:]:
        destination, source, length = [int(each) for each in line.split()]
        mapping.update(source, destination, length)
    return mapping


def main():
    seeds, seed_to_so, so_to_f, f_to_w, w_to_l, l_to_t, t_to_h, h_to_location = puzzle.input.split('\n\n')
    steps = [seed_to_so, so_to_f, f_to_w, w_to_l, l_to_t, t_to_h, h_to_location]
    seeds = parse_seeds(seeds)
    for i, m in enumerate(steps):
        steps[i] = parse_mapping(m)

    destinations = []
    for seed in seeds:
        for step in steps:
            seed = step.get_destination(seed)
        destinations.append(seed)
    print(min(destinations))


if __name__ == "__main__":
    main()
