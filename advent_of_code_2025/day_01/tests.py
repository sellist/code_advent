import solution as s

def test_part1_1():
    assert s.Part1.solution(['R50']) == 1


def test_part1_2():
    assert s.Part1.solution(['L50']) == 1


def test_part2_1():
    assert s.Part2.solution(['R101']) == 2


def test_part2_2():
    assert s.Part2.solution(['']) == 0


def test_part2_3():
    assert s.Part2.solution(['']) == 0
