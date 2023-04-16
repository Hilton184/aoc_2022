"""Solution to day 1."""


def get_data() -> list[str]:
    with open("day1/input.txt") as f:
        return f.readlines()


def calories_carried_per_elf(data: list[str]) -> list[int]:
    """Get the number of calories carried by each elf."""
    elves = []

    elf = []
    for line in data:
        if line == "\n":
            elves.append(elf)
            elf = []
        else:
            elf.append(int(line.rstrip("\n")))

    return [sum(elf) for elf in elves]


def part_1_solution(calories_per_elf: list[int]) -> int:
    """Get the number of calories carried by the elf with the most calories."""
    return max(calories_per_elf)


def part_2_solution(calories_per_elf: list[int]) -> int:
    """Get the number of calories carried by the three elves with the most calories."""
    return sum(sorted(calories_per_elf, reverse=True)[:3])


if __name__ == "__main__":
    data = get_data()

    calories_per_elf = calories_carried_per_elf(data)

    print(part_1_solution(calories_per_elf))

    print(part_2_solution(calories_per_elf))
