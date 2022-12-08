from src.base import BaseDay
from typing import List


class Day6(BaseDay):
    def run(self, part: int):
        if part == 1:
            self.run_part_1()
        elif part == 2:
            self.run_part_2()

    def run_part_1(self):
        self.result = self._get_first_marker_indexes()

    def run_part_2(self):
        pass

    def _get_first_marker_indexes(self) -> List[int]:
        indexes = []
        for line in self.input:
            print(line)
            line = line.strip()
            last_four_chars = ""
            for i, c in enumerate(line):
                if len(last_four_chars) == 4:
                    last_four_chars = last_four_chars[1:]
                last_four_chars += c
                if len(last_four_chars) == len(set(last_four_chars)) == 4:
                    indexes.append(i + 1)
                    break
        return indexes

