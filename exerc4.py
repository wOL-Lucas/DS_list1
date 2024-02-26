base_salary = float(input("Enter the base salary: "))
extra_hours = float(input("Enter the extra hours: "))


def calculate_total_salary(base_salary, extra_hours):
    return base_salary + (extra_hours * ((50/100) + 1))

print("The total salary is: ", calculate_total_salary(base_salary, extra_hours))

