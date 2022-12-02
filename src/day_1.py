from src.base import BaseDay


class Day1(BaseDay):
    def run(self):
        current_elf_sum = 0
        biggest_elf_sum = 0
        for line in self.input:
            value = line.replace("\n", "")
            if not value:
                biggest_elf_sum = biggest_elf_sum if current_elf_sum < biggest_elf_sum else current_elf_sum
                current_elf_sum = 0
            else:
                current_elf_sum += int(value)

        self.result = biggest_elf_sum
