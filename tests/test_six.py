import pytest
import src.six as day

# python -m pytest ..\tests\test_template.py -s


@pytest.mark.parametrize("input, result", [("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
("nppdvjthqldpwncqszvftbrmjlhg", 6),
("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)])
def test_example_part_one(input, result):
    assert result == day.part_one(input)


@pytest.mark.parametrize("input, result", [("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
("nppdvjthqldpwncqszvftbrmjlhg", 23),
("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26)])
def test_example_part_one(input, result):
    assert result == day.part_two(input)

