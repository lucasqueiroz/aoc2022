from src.day_4 import Day4
from tests.base import BaseTest

class TestDay4(BaseTest):
    DAY = 4

    def test_day_4_part_1_test_input(self):
        test_input = self.get_test_input()
        day_4_test = Day4(test_input)

        result = day_4_test.get_result(part=1)

        assert result == 2

    def test_day_4_part_1(self):
        real_input = self.get_input()
        day_4 = Day4(real_input)

        self.print_result(day_4, part=1)

    # def test_day_4_part_2_test_input(self):
    #     test_input = self.get_test_input()
    #     day_4_test = Day4(test_input)

    #     result = day_4_test.get_result(part=2)

    #     # assert result == 0

    # def test_day_4_part_2(self):
    #     real_input = self.get_input()
    #     day_4 = Day4(real_input)

    #     self.print_result(day_4, part=2)
