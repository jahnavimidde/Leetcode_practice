class Foo:
    def __init__(self):
        self.num = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.num += 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while True:
            if self.num == 1:
                printSecond()
                self.num += 1
                break

    def third(self, printThird: 'Callable[[], None]') -> None:
        while True:
            if self.num == 2:
                printThird()
                break
                    