from dataclasses import dataclass
import re
from src.base import BaseDay
from textwrap import TextWrapper
from typing import Dict, List


@dataclass
class Stack:
    crates: List[str]

    def take_n(self, n: int, reverse: bool) -> List[str]:
        n_crates = self.crates[:n]
        self.crates = self.crates[n:]
        if reverse:
            n_crates.reverse()
        return n_crates

    def add_crate(self, crate: str):
        self.crates.append(crate)

    def add_crates(self, crates: List[str]):
        crates.extend(self.crates)
        self.crates = crates


class Day5(BaseDay):
    def run(self, part: int):
        if part == 1:
            self.run_part_1()
        elif part == 2:
            self.run_part_2()

    def run_part_1(self):
        self.result = self._get_top_crates(True)

    def run_part_2(self):
        self.result = self._get_top_crates(False)

    def _get_top_crates(self, reverse: bool) -> str:
        self._create_stacks()
        self._move_crates(reverse)
        s = ""
        for i in self.stacks:
            s += self.stacks[i].crates[0].replace("[", "").replace("]", "")
        return s

    def _create_stacks(self) -> Dict[int, Stack]:
        stacks = {}
        wrapper = TextWrapper(replace_whitespace=False, drop_whitespace=False, width=4)
        for line in self.input:
            if line.startswith(" 1   2"):
                break
            wrapped = wrapper.wrap(line)
            for i in range(1, len(wrapped) + 1):
                if not stacks.get(i):
                    stacks[i] = Stack([])
                crate = wrapped[i-1].strip()
                if not crate:
                    continue
                stack = stacks[i]
                stack.add_crate(crate)
        self.stacks = stacks

    def _move_crates(self, reverse: bool):
        stacks = self.stacks
        for line in self.input:
            if not line.startswith("move"):
                continue
            line = line.replace("\n", "")
            n, from_stack, to_stack = (re.search(r"move (\d+) from (\d+) to (\d+)", line)).groups()
            crates = stacks[int(from_stack)].take_n(int(n), reverse)
            stacks[int(to_stack)].add_crates(crates)
