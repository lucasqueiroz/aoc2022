from src.base import BaseDay
from typing import Dict


class Day2(BaseDay):
    def run(self, part: int):
        if part == 1:
            self.run_part_1()
        elif part == 2:
            self.run_part_2()

    def run_part_1(self):
        outcomes = {
            "A": {"X": 4, "Y": 8, "Z": 3},
            "B": {"X": 1, "Y": 5, "Z": 9},
            "C": {"X": 7, "Y": 2, "Z": 6}
        }
        self.result = self._calculate_points(outcomes)

    def run_part_2(self):
        outcomes = {
            "A": {"X": 3, "Y": 4, "Z": 8},
            "B": {"X": 1, "Y": 5, "Z": 9},
            "C": {"X": 2, "Y": 6, "Z": 7}
        }
        self.result = self._calculate_points(outcomes)

    def _calculate_points(self, outcomes: Dict[str, Dict[str, int]]) -> int:
        points = 0
        for line in self.input:
            line = line.replace("\n", "")
            points += outcomes[line[0]][line[2]]

        return points
