class TaskPlan:
    def __init__(self):
        self.estimates = []
        self.probabilities = []

    def add_task(self, estimate, probability):
        self.estimates.append(estimate)
        self.probabilities.append(probability)

    def average_completion_time(self):
        total_time = 0
        for i in range(len(self.estimates)):
            total_time += self.estimates[i] * self.probabilities[i] / 100
        return total_time


plan = TaskPlan()

while True:
    estimate = int(input("Enter task estimate (in days): "))
    probability = int(input("Enter task probability (as a percentage): "))
    plan.add_task(estimate, probability)
    more_tasks = input("Add another task? (y/n): ")
    if more_tasks.lower() != "y":
        break

average_time = plan.average_completion_time()
print("The average time to finish the plan is", average_time, "days.")
