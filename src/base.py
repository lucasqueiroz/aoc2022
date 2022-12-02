from typing import List


class BaseDay:
    def __init__(self, input: List[str]):
        self.input = input

    def get_result(self, part: int) -> str:
        self.run(part=part)
        return self.result

    def run(self, part: int):
        raise NotImplementedError
