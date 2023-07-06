from order_book import OrderBook


class Menu:
    def __init__(self) -> None:
        self.__options = {
            "0": "exit",
            "1": "add order",
            "2": "list finished tasks",
            "3": "list unfinished tasks",
            "4": "mark task as finished",
            "5": "programmers",
            "6": "status of programmer",
        }
        self.__commands = "0123456"

    def show(self):
        print("commands:")
        for nb, option in self.__options.items():
            print(nb, option)

    def get_user_input(self) -> str:
        option = input("\ncommand: ")
        if option in self.__commands:
            return option


class Application:
    def __init__(self) -> None:
        self.__orders = OrderBook()
        self.__menu = Menu()

    def start(self):
        self.__menu.show()
        while True:
            option = self.__menu.get_user_input()
            if option == "0":
                break
            self.process(option)

    def process(self, option: str):
        if option == "1":
            self.add_order()
        elif option == "2":
            self.list_finished_tasks()
        elif option == "3":
            self.list_unfinished_tasks()
        elif option == "4":
            self.mark_finished()
        elif option == "5":
            self.programmers()
        elif option == "6":
            self.status_of_programmer()

    def add_order(self):
        description = input("description: ")
        try:
            prog, workload = input(
                "programmer and workload estimate: ").split()
            self.__orders.add_order(description, prog, int(workload))
            print("added!")
        except:
            print("erroneous input")

    def list_finished_tasks(self):
        finished = self.__orders.finished_orders()
        if len(finished) == 0:
            print("no finished tasks")
        else:
            for task in finished:
                print(task)

    def list_unfinished_tasks(self):
        unfinished = self.__orders.unfinished_orders()
        if len(unfinished) == 0:
            print("no unfinished tasks")
        else:
            for task in unfinished:
                print(task)

    def mark_finished(self):
        id = input("id: ")
        try:
            self.__orders.mark_finished(int(id))
            print("marked as finished")
        except:
            print("erroneous input")

    def programmers(self):
        for prog in self.__orders.programmers():
            print(prog)

    def status_of_programmer(self):
        programmer = input("programmer: ")
        try:
            f, nf, sf, su = self.__orders.status_of_programmer(programmer)
            print(f"tasks: finished {f} not finished {nf},"
                  f" hours: done {sf} scheduled {su}")
        except:
            print("erroneous input")


if __name__ == "__main__":
    Application().start()
