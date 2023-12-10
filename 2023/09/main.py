import numpy as np
import numpy.typing as npt

import puzzle


def solve_next(seq: npt.NDArray):
    n = 0
    while not (seq == 0).all():
        n += seq[-1]
        seq = np.diff(seq)
    return n



def main():
    answer = 0
    for seq in puzzle.input.split("\n"):
        seq = np.array([int(each) for each in seq.split()])
        answer += solve_next(seq)
    print(answer)

if __name__ == "__main__":
    main()
