from src.base import BaseDay


class Day4(BaseDay):
    def run(self, part: int):
        if part == 1:
            self.run_part_1()
        elif part == 2:
            self.run_part_2()

    def run_part_1(self):
        self.result = self._get_overlapping_pairs(part=1)

    def run_part_2(self):
        self.result = self._get_overlapping_pairs(part=2)

    def _get_overlapping_pairs(self, part: int) -> int:
        total = 0
        for line in self.input:
            first_pair, second_pair = line.replace("\n", "").split(",")
            first_range, second_range = [self._get_range(first_pair), self._get_range(second_pair)]
            if self._ranges_overlap(first_range, second_range, part==2):
                total += 1

        return total

    def _get_range(self, pair: str) -> range:
        pair_start, pair_stop = pair.split("-")
        return range(int(pair_start), int(pair_stop) + 1)

    def _ranges_overlap(self, range_a: range, range_b: range, intersection: bool = False) -> bool:
        if intersection:
            return len(set(range_a).intersection(range_b)) > 0
        return set(range_a).issubset(range_b) or set(range_b).issubset(range_a)
