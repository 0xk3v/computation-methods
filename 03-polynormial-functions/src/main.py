class Polynomial:
    def __init__(self):
        self.points = []
        self.coefficients = []
        self.order = 0

    def input_points(self):
        self.points = []
        n = int(input("Enter the number of points: "))
        for i in range(n):
            x, y = map(
                float, input(f"Enter the x and y coordinates of point {i+1}: ").split()
            )
            self.points.append((x, y))
        self.coefficients = self.interpolate()
        self.order = len(self.coefficients) - 1

    def interpolate(self):
        x = [p[0] for p in self.points]
        y = [p[1] for p in self.points]
        n = len(x)
        vandermonde = [[xi**j for j in range(n)] for xi in x]
        coefficients = [0] * n

        for i in range(n):
            pivot = vandermonde[i][i]
            if pivot == 0:
                continue
            for j in range(i + 1, n):
                factor = vandermonde[j][i] / pivot
                for k in range(n):
                    vandermonde[j][k] -= factor * vandermonde[i][k]
                y[j] -= factor * y[i]

        for i in range(n - 1, -1, -1):
            pivot = vandermonde[i][i]
            if pivot == 0:
                coefficients[i] = 0
            else:
                coefficients[i] = y[i] / vandermonde[i][i]
                for j in range(i):
                    y[j] -= vandermonde[j][i] * coefficients[i]

        return coefficients

    def differentiate(self):
        n = len(self.coefficients) - 1
        derivative_coefficients = [n * self.coefficients[i] for i in range(1, n + 1)]
        return derivative_coefficients

    def evaluate(self, x):
        result = 0
        for i in range(len(self.coefficients) - 1, -1, -1):
            result = result * x + self.coefficients[i]
        return result

    def find_root(self, x0, x1, eps):
        f = self.evaluate
        f0, f1 = f(x0), f(x1)
        while abs(f1) > eps:
            x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
            f2 = f(x2)
            x0, x1, f0, f1 = x1, x2, f1, f2
        return x1

    def display_values(self):
        if not self.coefficients:
            print(
                "Error: no coefficients available. Please input points and interpolate first."
            )
            return
        print("Values of the polynomial:")
        for x in [-1, 0, 1]:
            y = self.evaluate(x)
            print(f"f({x}) = {y}")


p = Polynomial()

p.input_points()
p.display_values()
root = p.find_root(0, 1, 1e-6)
print(f"The root for x is {root}")
