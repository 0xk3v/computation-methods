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


def main():
    lcg = LCG(12345, 1103515245, 12345, 2**31)
    xorshift = Xorshift(123456789, 13, 17, 5)

    for i in range(10):
        print("LCG:", lcg.next_value())
        print("Xorshift:", xorshift.next_value())
        print()


if __name__ == "__main__":
    main()
