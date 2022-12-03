from src.base import BaseDay


class Day3(BaseDay):
    def run(self, part: int):
        if part == 1:
            self.run_part_1()
        elif part == 2:
            self.run_part_2()

    def run_part_1(self):
        self.result = self._get_priority_sum()

    def run_part_2(self):
        pass

    def _get_priority_sum(self) -> int:
        total = 0
        for line in self.input:
            line = line.replace("\n", "")
            half_line_len = int(len(line) / 2)
            first, second = line[:half_line_len], line[half_line_len:]
            common_char = "".join(set(first).intersection(second))
            char_nr = ord(common_char.lower()) - 96
            if common_char.isupper():
                char_nr += 26
            total += char_nr
        return total

