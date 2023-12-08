import operator
import sys

import numpy as np

import puzzle


def intersection(start, end, other_start, other_end):
    start = max(start, other_start)
    end = min(end, other_end)
    if end <= start:
        return None
    return start, end


class Mapping:
    def __init__(self, name):
        self.name = name
        self.intervals = []
        self.matrix = None

    def update(self, source, destination, length):
        self.intervals.append((source, destination, length))

    def make_matrix(self):
        self.intervals = sorted(self.intervals, key=operator.itemgetter(0))
        intervals = []
        i = 0
        for interval in self.intervals:
            if i < interval[0]:
                intervals.append((i, i, interval[0] - i))
            intervals.append(interval)
            i = interval[0] + interval[2]
        last_interval = intervals[-1]
        start = last_interval[0] + last_interval[2]
        intervals.append((start, start, sys.maxsize - start))
        self.matrix = np.concatenate(
            [
                [a[0] for a in intervals],
                [a[0] + a[2] for a in intervals],
                [a[1] - a[0] for a in intervals],
            ],
        ).reshape((3, -1)).T

    def get_destination(self, interval_start, interval_length):
        intervals = self.matrix
        intersections = []
        for interval in intervals:
            intersect = intersection(interval_start, interval_start + interval_length, interval[0], interval[1])
            if intersect is None:
                continue
            intersect = (intersect[0] + interval[2], intersect[1] - intersect[0])
            intersections.append(intersect)
        return intersections


def parse_seeds(seed_line):
    for seed1, seed2 in zip(seed_line.split()[1::2], seed_line.split()[2::2]):
        yield int(seed1), int(seed2)


def parse_mapping(mapping_string):
    mapping = Mapping(mapping_string.split("\n")[0])
    for line in mapping_string.split("\n")[1:]:
        destination, source, length = [int(each) for each in line.split()]
        mapping.update(source, destination, length)
    mapping.make_matrix()
    return mapping


def main():
    seeds, seed_to_so, so_to_f, f_to_w, w_to_l, l_to_t, t_to_h, h_to_location = puzzle.input.split('\n\n')
    steps = [seed_to_so, so_to_f, f_to_w, w_to_l, l_to_t, t_to_h, h_to_location]
    seeds = parse_seeds(seeds)
    for i, m in enumerate(steps):
        steps[i] = parse_mapping(m)
    destinations = []
    for seed1, length in seeds:
        ranges = [(seed1, length)]
        for step in steps:
            new_ranges = []
            for (s, l) in ranges:
                new_ranges.extend(step.get_destination(s, l))
            ranges = new_ranges
        destinations.extend(new_ranges)

    print(sorted(destinations)[0][0])


if __name__ == "__main__":
    main()
