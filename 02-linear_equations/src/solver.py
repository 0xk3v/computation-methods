"""
Module to solve Linear equations 
"""


class LinearEquationsSolver:
    def __init__(self, coefficients, constants):
        self.coefficients = coefficients
        self.constants = constants

    def solve(self):
        # Forward elimination
        n = len(self.constants)
        for i in range(n - 1):
            for j in range(i + 1, n):
                try:
                    factor = self.coefficients[j][i] / self.coefficients[i][i]
                    self.coefficients[j] = [
                        x - y * factor
                        for x, y in zip(self.coefficients[j], self.coefficients[i])
                    ]
                    self.constants[j] -= self.constants[i] * factor
                except ZeroDivisionError:
                    print("Coefficient is 0")
                    exit()

        # Back substitution
        solution = [0] * n
        for i in range(n - 1, -1, -1):
            try:
                solution[i] = (
                    self.constants[i]
                    - sum(
                        [self.coefficients[i][j] * solution[j] for j in range(i + 1, n)]
                    )
                ) / self.coefficients[i][i]

            except ZeroDivisionError:
                print("Coefficient is 0")
                exit()

        return solution


# Prompt user for input
n = int(input("Enter the number of variables in the system: "))
coefficients = []
constants = []
for i in range(n):
    row = input(
        f"Enter the coefficients for equation {i+1} in the form 'a1 a2 ... an': "
    ).split()
    if len(row) != n:
        print("Error: number of coefficients must be equal to number of variables")
        exit()
    coefficients.append([float(x) for x in row])
    constant = float(input(f"Enter the constant for equation {i+1}: "))
    constants.append(constant)

# Display equations system
print("\nThe equation system is:")
for i in range(n):
    equation = ""
    for j in range(n):
        equation += f"{coefficients[i][j]}x{j+1} + "
    equation = equation[:-3] + f"= {constants[i]}"
    print(equation)

# Solve equations system
solver = LinearEquationsSolver(coefficients, constants)
solution = solver.solve()

# Display solution
solution_str = " ".join([f"x{i+1} = {x}" for i, x in enumerate(solution)])
print(f"\nThe solution is: {solution_str}")
