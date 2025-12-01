import re


class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:

        def parse(s: str):
            pat = re.compile(r"^([LR])(\d+)$")
            result = pat.match(s.strip())
            if not result:
                return None
            return result.group(1), int(result.group(2))

        combo_values = [i for i in list(range(0, 100))]
        current_position = combo_values.index(50)
        zero_count = 0

        dial_size = len(combo_values)

        for line in file_lines:

            direction, rotation_amount = parse(line)
            if direction == "L":
                current_position = (current_position - rotation_amount) % dial_size
            elif direction == "R":
                current_position = (current_position + rotation_amount) % dial_size
            else:
                continue
            if current_position == 0:
                zero_count += 1

        return zero_count


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:

        def parse(s: str):
            m = re.compile(r"^([LR])(\d+)$").match(s.strip())
            return m.group(1), int(m.group(2))

        combo_values = [i for i in list(range(0, 100))]
        current_position = combo_values.index(50)
        zero_count = 0

        dial_size = len(combo_values)

        for line in file_lines:
            direction, rotation_amount = parse(line)

            if direction == "L":
                if current_position <= rotation_amount % dial_size:
                    zero_count += 1
                zero_count += rotation_amount // dial_size
                current_position = (current_position + 1 - rotation_amount) % dial_size
            elif direction == "R":
                if current_position + (rotation_amount % dial_size) > dial_size:
                    zero_count += 1
                zero_count += rotation_amount // dial_size
                current_position = (current_position + rotation_amount) % dial_size

        return zero_count


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        f = file.read().splitlines()

    print(f"Part 1: {Part1.solution(f)}")
    print(f"Part 2: {Part2.solution(f)}")
