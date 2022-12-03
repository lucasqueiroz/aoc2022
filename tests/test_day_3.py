from src.day_3 import Day3
from tests.base import BaseTest

class TestDay3(BaseTest):
    DAY = 3

    def test_day_3_part_1_test_input(self):
        test_input = self.get_test_input()
        day_3_test = Day3(test_input)

        result = day_3_test.get_result(part=1)

        assert result == 157

    def test_day_3_part_1(self):
        real_input = self.get_input()
        day_3 = Day3(real_input)

        self.print_result(day_3, part=1)

    def test_day_3_part_2_test_input(self):
        test_input = self.get_test_input()
        day_3_test = Day3(test_input)

        result = day_3_test.get_result(part=2)

        assert result == 70

    def test_day_3_part_2(self):
        real_input = self.get_input()
        day_3 = Day3(real_input)

        self.print_result(day_3, part=2)
