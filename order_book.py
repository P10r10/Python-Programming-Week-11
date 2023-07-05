class Task:
    task_id = 0

    def __init__(
            self, description: str, programmer: str, workload: int
    ) -> None:
        self.__description = description
        self.__programmer = programmer
        self.__workload = workload
        Task.task_id += 1
        self.__id = Task.task_id
        self.__is_finished = False

    @property
    def description(self):
        return self.__description

    @property
    def programmer(self):
        return self.__programmer

    @property
    def workload(self):
        return self.__workload

    @property
    def id(self):
        return self.__id

    def is_finished(self):
        return self.__is_finished

    def mark_finished(self):
        self.__is_finished = True

    def __str__(self) -> str:
        return f"{self.id}: {self.description} ({self.workload} hours), " \
            f"programmer {self.programmer} " \
            f"{'' if self.is_finished() else 'NOT '}FINISHED"


class OrderBook:
    def __init__(self) -> None:
        self.__orders = []
        self.__programmers = []

    def add_order(self, description: str, programmer: str, workload: int):
        self.__orders.append(Task(description, programmer, workload))
        self.__programmers.append(programmer)

    def all_orders(self):
        return self.__orders

    def programmers(self):
        return list(set(self.__programmers))

    def mark_finished(self, id: int):
        for order in self.__orders:
            if order.id == id:
                order.mark_finished()
                break
        else:
            raise ValueError

    def finished_orders(self):
        return [order for order in self.__orders if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self.__orders if not order.is_finished()]

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError
        nb_finished = sum([task.is_finished() for task in self.finished_orders()
                           if task.programmer == programmer])
        nb_not_finished = sum([not task.is_finished()
                               for task in self.unfinished_orders()
                               if task.programmer == programmer])
        sum_finished = sum([task.workload for task in self.finished_orders()
                           if task.programmer == programmer])
        sum_unfinished = sum([task.workload for task in self.unfinished_orders()
                              if task.programmer == programmer])
        return (nb_finished, nb_not_finished, sum_finished, sum_unfinished)


if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
