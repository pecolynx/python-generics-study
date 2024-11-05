from typing import List, TypeVar, Generic, Callable
T = TypeVar('T')

class MyType:
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"MyType({self.value})"

class Consumer(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def consume(self) -> T:
        return self.value


if __name__ == "__main__":
    consumer = Consumer(1)
    print(consumer.consume())
    print(type(consumer.consume()))
    consumer = Consumer("Hello")
    print(consumer.consume())
    print(type(consumer.consume()))
    consumer = Consumer([1, 2, 3])
    print(consumer.consume())
    print(type(consumer.consume()))

    consumer = Consumer(MyType(123))
    print(consumer.consume())
    print(type(consumer.consume()))
