from solution import parse_rotations_sequence, rotate_dial, get_password
import pytest


class TestSolution:
    def test_rotations_sequence(self):
        rotations_sequence = """\
            L68
            L30
            R48
            L5
            R60\
        """
        assert parse_rotations_sequence(rotations_sequence) == [{"L": 68}, {"L": 30}, {"R": 48}, {"L": 5}, {"R":60}]

    @pytest.mark.parametrize(
        "start, rotation, new_dial_value",
        [
            (50, {"L": 68}, 82),
            (50, {"L": 200}, 50),
            (82, {"L": 30}, 52),
            (52, {"R": 48}, 0),
            (50, {"R": 100}, 50),
        ]
    )
    def test_rotate_dial(self, start, rotation, new_dial_value):
        assert rotate_dial(start, rotation) == new_dial_value

    def test_get_password(self):
        rotations_sequence = """\
            L68
            L30
            R48
            L5
            R60
            L55
            L1
            L99
            R14
            L82\
        """
        assert get_password(rotations_sequence) == 3
