

class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """
        The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves'
        expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their
        supplies. One important consideration is food - in particular, the number of Calories each Elf is carrying
        (your puzzle input).

        The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc.
        that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's
        inventory (if any) by a blank line.

        Returns:
            Elf carrying the most calories
        """
        totals = []
        curr = 0
        for x in file_lines:
            if x != '':
                curr = curr + int(x)
            else:
                totals.append(curr)
                curr = 0
        return max(totals)


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """
        By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the
        most Calories of food might eventually run out of snacks.

        To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three
        Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

        Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

        Args:
            file_lines:

        Returns:
            Sum of top 3 elves
        """
        totals = []
        curr = 0
        for x in file_lines:
            if x != '':
                curr = curr + int(x)
            else:
                totals.append(curr)
                curr = 0

        return sum(sorted(totals)[::-1][0:3])



with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



