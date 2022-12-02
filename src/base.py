from typing import List


class BaseDay:
    def __init__(self, input: List[str]):
        self.input = input

    def get_result(self) -> str:
        self.run()
        return self.result

    def run(self):
        raise NotImplementedError
