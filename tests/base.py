from os.path import dirname, realpath
from src.base import BaseDay


class BaseTest:

    DAY = None

    def _get_file_lines(self, file_name: str):
        path = dirname(dirname(realpath(__file__)))
        file = open(f"{path}/input/{file_name}")
        return file.readlines()

    def get_input(self):
        return self._get_file_lines(f"day-{self.DAY}")

    def get_test_input(self):
        return self._get_file_lines(f"day-{self.DAY}-test")

    def print_result(self, day: BaseDay, part: int):
        print(f"[DAY {self.DAY} - PART {part}] {day.get_result(part=part)}")
