import random


class LCG:
    def __init__(self, seed, multiplier, increment, modulus):
        self.seed = seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus

    def next_value(self):
        self.seed = (self.multiplier * self.seed + self.increment) % self.modulus
        return self.seed


class Xorshift:
    def __init__(self, seed, shift1, shift2, shift3):
        self.seed = seed
        self.shift1 = shift1
        self.shift2 = shift2
        self.shift3 = shift3

    def next_value(self):
        x = self.seed
        x ^= (x << self.shift1) & 0xFFFFFFFF
        x ^= (x >> self.shift2) & 0xFFFFFFFF
        x ^= (x << self.shift3) & 0xFFFFFFFF
        self.seed = x
        return self.seed


class Visualization:
    """docstring for Visualization."""

    def __init__(self, number):
        self.num = str(number)
        digits_count = {}
        print(self.num)
        for i in self.num:
            if i.isdigit():
                if i in digits_count:
                    digits_count[i] += 1
                else:
                    digits_count[i] = 1
        for digit, count in sorted(digits_count.items()):
            print(f"{digit}", end=": ")
            for i in range(0, count):
                print("#", end="")
            percentage = 100 * float(count) / len(self.num)
            print(f" {percentage}%", end="")
            print()


def main():
    lcg = LCG(123456789, 1103515245, 12345, 2**31)
    xorshift = Xorshift(123456789, 13, 17, 5)

    print("Choose RNG Engine")
    choice = int(input("1. LCG\n2. Xorshift\n3. Built-in Gen\n: "))

    print(choice)

    if choice == 1:
        # LCG
        ab1 = Visualization(int(lcg.next_value()))
    elif choice == 2:
        ab2 = Visualization(int(xorshift.next_value()))
    elif choice == 3:
        ab3 = Visualization(int(random.randrange(10000000, 999999999)))
    else:
        print("Invalid choice")
        exit()


if __name__ == "__main__":
    main()
