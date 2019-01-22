# Demonstrates iterator class function.


class Countdown:
    def __init__(self, start):
        # Demonstrates isinstance function to check argument type.
        if not isinstance(start, int):
            raise TypeError
        self.start = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == 0:
            raise StopIteration
        self.start = self.start - 1
        return self.start


count3 = Countdown(3)
for count in count3:
    print(count)
print()

# Demonstrates equivalent of above iterator as a generator.


def countdown_gen(start):
    for i in range(start, -1, -1):
        yield i


for count in countdown_gen(3):
    print(count)
print()

# Demonstrates equivalent generator expression for the above.
for count in (i for i in range(3, -1, -1)):
    print(count)
