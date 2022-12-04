from src.base import BaseDay


class Day4(BaseDay):
    def run(self, part: int):
        if part == 1:
            self.run_part_1()
        elif part == 2:
            self.run_part_2()

    def run_part_1(self):
        self.result = self._get_overlapping_pairs()

    def run_part_2(self):
        pass

    def _get_overlapping_pairs(self) -> int:
        total = 0
        for line in self.input:
            first_pair, second_pair = line.replace("\n", "").split(",")
            first_pair_start, first_pair_stop = first_pair.split("-")
            second_pair_start, second_pair_stop = second_pair.split("-")
            first_range = range(int(first_pair_start), int(first_pair_stop) + 1)
            second_range = range(int(second_pair_start), int(second_pair_stop) + 1)
            if self._ranges_overlap(first_range, second_range):
                total += 1

        return total

    def _ranges_overlap(self, range_a: range, range_b: range) -> bool:
        list_a = list(range_a)
        list_b = list(range_b)
        return set(list_a).issubset(list_b) or set(list_b).issubset(list_a)
