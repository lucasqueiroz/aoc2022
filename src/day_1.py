from src.base import BaseDay
from typing import List


class Day1(BaseDay):
    def run(self, part: int):
        if part == 1:
            self.run_part_1()
        elif part == 2:
            self.run_part_2()

    def run_part_1(self):
        self.result = self._get_sorted_elves()[0]

    def run_part_2(self):
        self.result = sum(self._get_sorted_elves()[0:3])

    def _get_sorted_elves(self) -> List[int]:
        elves = []
        current_elf_sum = 0

        for line in self.input:
            value = line.replace("\n", "")
            if not value:
                elves.append(current_elf_sum)
                current_elf_sum = 0
            else:
                current_elf_sum += int(value)

        elves.append(current_elf_sum)
        elves.sort(reverse=True)
        return elves
