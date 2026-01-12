DIAL_STARTING_VALUE = 50

def parse_rotations_sequence(rotations_sequence: str) -> list:
    """
    Parse the raw rotations sequence.

    Args:
        rotations_sequence: raw input data e.g.
            L68
            L30
            R48
            L5
            R60

    Returns:
        formatted rotations sequence e.g.
            [{"L": 68}, {"L": 30}, {"R": 48}, {"L": 5}, {"R":60}]
    """
    parsed_rotations_sequence: list = []
    for rotation_str in rotations_sequence.split("\n"):
        rotation_str = rotation_str.strip()
        parsed_rotations_sequence.append({rotation_str[0]: int(rotation_str[1:])})

    return parsed_rotations_sequence

def rotate_dial(start: int, rotation: dict) -> int:
    """
    Rotate the dial from the start position.

    Args:
        start: starting value of the dial e.g. 50
        rotation: the rotation sequence as a dictionary e.g. {"L": 68}

    Returns:
        New value that the dial is pointing at e.g. 82
    """
    if "L" in rotation:
        dial_value = (start - rotation["L"]) % 100
        if dial_value < 0:
            dial_value += 100
        return dial_value
    elif "R" in rotation:
        dial_value = (start + rotation["R"]) % 100
        return dial_value
    else:
        raise Exception("Unknown rotation")

def get_password(rotations_sequence: str) -> int:
    """
    Get the total number of times the dial points at 0
    """
    rotations_sequence = parse_rotations_sequence(rotations_sequence)
    total_points_at_0 = 0
    start = DIAL_STARTING_VALUE

    for rotation in rotations_sequence:
        dial_value = rotate_dial(start, rotation)
        if dial_value == 0:
            total_points_at_0 += 1
        start = dial_value

    return total_points_at_0

def main():
    f = open("input.txt", "r")
    solution = get_password(f.read())
    f.close()
    print(solution)

if __name__ == "__main__":
    main()