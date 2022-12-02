from src.day_2 import Day2
from tests.base import BaseTest

class TestDay2(BaseTest):
    DAY = 2

    def test_day_2_part_1_test_input(self):
        test_input = self.get_test_input()
        day_2_test = Day2(test_input)

        result = day_2_test.get_result(part=1)

        assert result == 15

    def test_day_2_part_1(self):
        real_input = self.get_input()
        day_2 = Day2(real_input)

        self.print_result(day_2, part=1)

    def test_day_2_part_2_test_input(self):
        test_input = self.get_test_input()
        day_2_test = Day2(test_input)

        result = day_2_test.get_result(part=2)

        assert result == 12

    def test_day_2_part_2(self):
        real_input = self.get_input()
        day_2 = Day2(real_input)

        self.print_result(day_2, part=2)
