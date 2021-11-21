from typing import Generator

def fibonnaci(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0  # initially set to fibonnaci(0)
    next: int = 1  # initially set to fibonnaci(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next # main generation step


if __name__ == "__main__":
    for i in fibonnaci(50):
        print(i)



