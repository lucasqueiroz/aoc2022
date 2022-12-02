from src.base import BaseDay


class Day2(BaseDay):
    def run(self, part: int):
        if part == 1:
            self.run_part_1()
        elif part == 2:
            self.run_part_2()

    def run_part_1(self):
        self.result = self._calculate_points()

    def run_part_2(self):
        pass

    def _calculate_points(self) -> int:
        points = 0
        for line in self.input:
            line = line.replace("\n", "")
            points += self._get_outcome_score(line[0], line[2])

        return points

    def _get_outcome_score(self, input_elf: str, input_player: str) -> int:
        outcomes = {
            "A": {"X": 4, "Y": 8, "Z": 3},
            "B": {"X": 1, "Y": 5, "Z": 9},
            "C": {"X": 7, "Y": 2, "Z": 6}
        }
        return outcomes[input_elf][input_player]
