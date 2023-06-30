class LotteryNumbers:
    def __init__(self, week_nb: int, numbers: list[int]) -> None:
        self.__week_nb = week_nb
        self.__numbers = numbers

    def number_of_hits(self, numbers: list) -> int:
        return sum([number in self.__numbers for number in numbers])

    def hits_in_place(self, numbers: list[int]) -> list[int]:
        return [n if n in self.__numbers else -1 for n in numbers]


if __name__ == "__main__":
    week8 = LotteryNumbers(8, [1, 2, 3, 10, 20, 30, 33])
    my_numbers = [1, 4, 7, 10, 11, 20, 30]

    print(week8.hits_in_place(my_numbers))
