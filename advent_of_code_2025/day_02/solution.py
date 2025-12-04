from utils.helper import StringUtils


class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        raw_ranges = [x for x in file_lines[0].split(",")]
        ranges = [r.split("-") for r in raw_ranges]

        total = 0

        def check_repeated_substring(number: int) -> bool:
            string_num = str(number)
            if len(string_num) % 2 != 0:
                return False

            mid = len(string_num) // 2
            first_half, second_half = string_num[:mid], string_num[mid:]

            return first_half == second_half

        for x,y in ranges:
            start, end = int(x), int(y)

            for num in list(range(start,end+1)):
                if check_repeated_substring(num):
                    total += num

        return total

        # I can't read, initial day 1 attempt
        # total = 0
        # print(ranges)
        # for num_range in ranges:
        #     start, end = num_range
        #
        #     for num in list(range(int(start),int(end)+1)):
        #         longest_sub = StringUtils.longest_duplicate_substring(str(num))
        #         if longest_sub is not None:
        #             total += num
        #
        #
        # return total


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        raw_ranges = [x for x in file_lines[0].split(",")]
        ranges = [r.split("-") for r in raw_ranges]
        total = 0

        def is_repeated_number(number: int) -> bool:
            string_num = str(number)
            str_length = len(string_num)

            if str_length < 2:
                return False
            for x in range(1, str_length // 2 + 1):
                if str_length % x != 0:
                    continue
                if string_num == string_num[:x] * (str_length // x):
                    return True
            return False

        for x,y in ranges:
            start, end = int(x), int(y)

            for num in list(range(start,end+1)):
                if is_repeated_number(num):
                    total += num


        return total

if __name__ == '__main__':
    with open("input.txt", "r") as file:
        f = file.read().splitlines()

    print(f"Part 1: {Part1.solution(f)}")
    print(f"Part 2: {Part2.solution(f)}")
