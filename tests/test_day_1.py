from src.day_1 import Day1
from tests.base import BaseTest

class TestDay1(BaseTest):
    DAY = 1

    def test_day_1_part_1_test_input(self):
        test_input = self.get_test_input()
        day_1_test = Day1(test_input)

        result = day_1_test.get_result(part=1)

        assert result == 24000

    def test_day_1_part_1(self):
        real_input = self.get_input()
        day_1 = Day1(real_input)

        self.print_result(day_1, part=1)

    def test_day_1_part_2_test_input(self):
        test_input = self.get_test_input()
        day_1_test = Day1(test_input)

        result = day_1_test.get_result(part=2)

        assert result == 45000

    def test_day_1_part_2(self):
        real_input = self.get_input()
        day_1 = Day1(real_input)

        self.print_result(day_1, part=2)
