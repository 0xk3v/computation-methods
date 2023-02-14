class RPNCalculator:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def add(self):
        b = self.pop()
        a = self.pop()
        self.push(a + b)

    def subtract(self):
        b = self.pop()
        a = self.pop()
        self.push(a - b)

    def multiply(self):
        b = self.pop()
        a = self.pop()
        self.push(a * b)

    def divide(self):
        b = self.pop()
        a = self.pop()
        self.push(a / b)

    def calculate(self, expression):
        for token in expression.split():
            if token == "+":
                self.add()
            elif token == "-":
                self.subtract()
            elif token == "*":
                self.multiply()
            elif token == "/":
                self.divide()
            else:
                self.push(float(token))
        return self.pop()


class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        return sum(coef * x**i for i, coef in enumerate(self.coefficients))

    def __str__(self):
        s = ""
        for i, coef in enumerate(self.coefficients[::-1]):
            if coef != 0:
                if s:
                    s += " + "
                s += f"{coef}x^{len(self.coefficients)-i-1}"
        return s

    def integral(self, a, b, n=1000):
        h = (b - a) / n
        s = 0.5 * (self(a) + self(b))
        for i in range(1, n):
            s += self(a + i * h)
        return s * h


# Example usage
expression = "2 3 + 4 * 5 -"
calculator = RPNCalculator()
result = calculator.calculate(expression)
print(result)  # -9.0

coefficients = list(
    map(int, input("Enter the coefficients of the polynomial function: ").split())
)
poly = Polynomial(coefficients)
print("The polynomial function is:", poly)
a, b = map(int, input("Enter the range for the integral: ").split())
result = poly.integral(a, b)
print("The integral of the polynomial function in the given range is:", result)
