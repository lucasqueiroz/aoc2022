from src.day_1 import Day1
from tests.base import BaseTest

class TestDay1(BaseTest):
    DAY = 1

    def test_day_1_test_input(self):
        test_input = self.get_test_input()
        day_1_test = Day1(test_input)

        day_1_test.run()

        assert day_1_test.result == 24000

    def test_day_1(self):
        real_input = self.get_input()
        day_1 = Day1(real_input)

        day_1.run()

        self.print_result(day_1)
