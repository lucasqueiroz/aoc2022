from src.day_6 import Day6
from tests.base import BaseTest

class TestDay6(BaseTest):
    DAY = 6

    def test_day_6_part_1_test_input(self):
        test_input = self.get_test_input()
        day_6_test = Day6(test_input)

        result = day_6_test.get_result(part=1)

        assert result == [7, 5, 6, 10, 11]

    def test_day_6_part_1(self):
        real_input = self.get_input()
        day_6 = Day6(real_input)

        self.print_result(day_6, part=1)

    def test_day_6_part_2_test_input(self):
        test_input = self.get_test_input()
        day_6_test = Day6(test_input)

        result = day_6_test.get_result(part=2)

        assert result == [19, 23, 23, 29, 26]

    def test_day_6_part_2(self):
        real_input = self.get_input()
        day_6 = Day6(real_input)

        self.print_result(day_6, part=2)
