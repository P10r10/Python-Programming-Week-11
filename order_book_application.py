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

    def show(self):
        for nb, option in self.__options.items():
            print(nb, option)
        self.get_user_input()

    def get_user_input(self):
        while True:
            option = input("command: ")
            if option == "0":
                break
            if option in "123456":
                self.process_option(option)

    def process_option(self, option: str):
        print("DEB: ", option)
        # TODO


if __name__ == "__main__":
    Menu().show()
