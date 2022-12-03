import itertools
from src.base import BaseDay
from typing import List


class Day3(BaseDay):
    def run(self, part: int):
        if part == 1:
            self.run_part_1()
        elif part == 2:
            self.run_part_2()

    def run_part_1(self):
        self.result = self._get_type_priority_sum()

    def run_part_2(self):
        self.result = self._get_badge_priority_sum()

    def _get_type_priority_sum(self) -> int:
        total = 0
        for line in self.input:
            line = line.replace("\n", "")
            half_line_len = int(len(line) / 2)
            first, second = line[:half_line_len], line[half_line_len:]
            total += self._get_common_char_value([first, second])
        return total

    def _get_badge_priority_sum(self) -> int:
        total = 0
        lines = self.input
        line_groups = [lines[i:i+3] for i in range(0, len(lines), 3)]
        for line_group in line_groups:
            total += self._get_common_char_value(line_group)
        return total

    def _get_common_char_value(self, strs: List[str]) -> int:
        set_strs = set(strs[0].replace("\n", ""))
        for s in strs[1:]:
            set_strs = set_strs.intersection(s.replace("\n", ""))
        common_char = "".join(set_strs)
        char_nr = ord(common_char.lower()) - 96
        if common_char.isupper():
            char_nr += 26
        return char_nr
