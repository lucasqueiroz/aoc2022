from src.base import BaseDay
from typing import List


class Day6(BaseDay):
    def run(self, part: int):
        if part == 1:
            self.run_part_1()
        elif part == 2:
            self.run_part_2()

    def run_part_1(self):
        self.result = self._get_first_marker_indexes(n_chars=4)

    def run_part_2(self):
        self.result = self._get_first_marker_indexes(n_chars=14)

    def _get_first_marker_indexes(self, n_chars) -> List[int]:
        indexes = []
        for line in self.input:
            print(line)
            line = line.strip()
            last_n_chars = ""
            for i, c in enumerate(line):
                if len(last_n_chars) == n_chars:
                    last_n_chars = last_n_chars[1:]
                last_n_chars += c
                if len(last_n_chars) == len(set(last_n_chars)) == n_chars:
                    indexes.append(i + 1)
                    break
        return indexes

