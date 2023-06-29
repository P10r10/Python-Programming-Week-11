from math import sqrt


def square_roots(numbers: list) -> list[float]:
    return [sqrt(x) for x in numbers]


if __name__ == "__main__":
    lines = square_roots([1, 2, 3, 4])
    for line in lines:
        print(line)
