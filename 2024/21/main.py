from collections import deque
from dataclasses import dataclass

panel_moves_to = {
    "A": {
        "<": "0",
        "^": "3",
    },
    "0": {
        ">": "A",
        "^": "2",
    },
    "1": {
        ">": "2",
        "^": "4",
    },
    "2": {
        ">": "3",
        "<": "1",
        "v": "0",
        "^": "5",
    },
    "3": {
        "<": "2",
        "v": "A",
        "^": "6",
    },
    "4": {
        "v": "1",
        ">": "5",
        "^": "7",
    },
    "5": {
        "v": "2",
        ">": "6",
        "<": "4",
        "^": "8",
    },
    "6": {
        "v": "3",
        "<": "5",
        "^": "9",
    },
    "7": {
        "v": "4",
        ">": "8",
    },
    "8": {
        "v": "5",
        ">": "9",
        "<": "7",
    },
    "9": {
        "v": "6",
        "<": "8",
    },
}


@dataclass(frozen=True)
class Panel:
    display: str
    highlighted_button: str

    def print(self):
        return self.display

    def move(self, direction) -> "Panel | None":
        if direction in panel_moves_to[self.highlighted_button]:
            return Panel(self.display, panel_moves_to[self.highlighted_button][direction])
        return None

    def press(self) -> "Panel":
        return Panel(display=self.display + self.highlighted_button, highlighted_button=self.highlighted_button)


robot_moves_to = {
    ">": {
        "<": "v",
        "^": "A",
    },
    "<": {
        ">": "v",
    },
    "^": {
        ">": "A",
        "v": "v",
    },
    "v": {
        ">": ">",
        "<": "<",
        "^": "^",
    },
    "A": {
        "<": "^",
        "v": ">",
    },
}


@dataclass(frozen=True)
class RobotPanel:
    highlighted_button: str
    controls: "RobotArm"

    def print(self):
        return self.controls.points_to.print()

    def move(self, direction) -> "RobotPanel | None":
        if direction in robot_moves_to[self.highlighted_button]:
            return RobotPanel(robot_moves_to[self.highlighted_button][direction], self.controls)
        return None

    def press(self) -> "RobotPanel | None":
        # means press highlighted button
        if self.highlighted_button == "A":
            x = self.controls.press()
            if x is None:
                return None
            return RobotPanel(self.highlighted_button, x)
        else:
            x = self.controls.move(self.highlighted_button)
            if x is None:
                return None
            return RobotPanel(self.highlighted_button, x)


@dataclass(frozen=True)
class RobotArm:
    points_to: RobotPanel | Panel

    def press(self) -> "RobotArm | None":
        x = self.points_to.press()
        if x is None:
            return None
        return RobotArm(x)

    def move(self, direction) -> "RobotArm | None":
        x = self.points_to.move(direction)
        if x is None:
            return x
        return RobotArm(x)


def get_neighbors(robot_panel: RobotPanel):
    neighbors = []
    for each in "A<>^v":
        if each == "A":
            n = robot_panel.press()
            if n is None:
                continue
            neighbors.append(n)
        else:
            n = robot_panel.move(each)
            if n is None:
                continue
            neighbors.append(n)
    return neighbors


def bfs(robot_panel: RobotPanel, end_string: str):
    q = deque()
    visited = set()
    visited.add(robot_panel)
    q.append((robot_panel, 0))
    while q:
        current_position, seq_len = q.popleft()
        if current_position.print() == end_string:
            return current_position, seq_len
        for next in get_neighbors(current_position):
            if next not in visited:
                visited.add(next)
                q.append((next, seq_len + 1))
    raise ValueError()


def solve_string(end_string):
    panel = Panel("", "A")

    robot_arm1 = RobotArm(panel)
    robot_panel_1 = RobotPanel("A", robot_arm1)

    robot_panel_2 = RobotPanel("A", RobotArm(robot_panel_1))

    s = 0
    for i in range(len(end_string)):
        robot_panel_2, seq_len = bfs(robot_panel_2, end_string[: i + 1])
        s += seq_len
    return s * int(end_string[:-1])


def part_one(puzzle_input):
    s = 0
    for end_string in puzzle_input.splitlines():
        s += solve_string(end_string)
    print(s)


if __name__ == "__main__":
    import puzzle

    part_one(puzzle.example)
    part_one(puzzle.input)
