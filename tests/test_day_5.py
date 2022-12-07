from src.day_5 import Day5
from tests.base import BaseTest

class TestDay5(BaseTest):
    DAY = 5

    def test_day_5_part_1_test_input(self):
        test_input = self.get_test_input()
        day_5_test = Day5(test_input)

        result = day_5_test.get_result(part=1)

        assert result == "CMZ"

    def test_day_5_part_1(self):
        real_input = self.get_input()
        day_5 = Day5(real_input)

        self.print_result(day_5, part=1)

    # def test_day_5_part_2_test_input(self):
    #     test_input = self.get_test_input()
    #     day_5_test = Day5(test_input)

    #     result = day_5_test.get_result(part=2)

    #     # assert result == 0

    # def test_day_5_part_2(self):
    #     real_input = self.get_input()
    #     day_5 = Day5(real_input)

    #     self.print_result(day_5, part=2)
