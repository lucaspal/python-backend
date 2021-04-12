import string
from typing import List, Tuple


class Employee(object):

    def __init__(self, name: string, age: int,
                 gender: string, salary: float, department: string):
        self._name = name
        self._age = age
        self._gender = gender
        self._salary = salary
        self._department = department

    @property
    def name(self): return self._name

    @property
    def age(self): return self._age

    @property
    def gender(self): return self._gender

    @property
    def salary(self): return self._salary

    @property
    def department(self): return self._department

    def __str__(self):
        return f"{self.name}, age {self.age}, {self.gender}, " \
               f"from department {self._department}, earning ${self.salary}"


class Range:
    def __init__(self, minimum: int = None, maximum: int = None):
        self._min = minimum
        self._max = maximum

    def in_range(self, value: int):
        return (self._min is None or value >= self._min) \
               and (self._max is None or value <= self._max)

    def __str__(self):
        if self._min is None:
            return f"{self._max}-"
        if self._max is None:
            return f"{self._min}+"
        return f"[{self._min},{self._max}]"


def read_employees(filepath: string) -> List[Employee]:
    result = []
    with open(filepath, 'r') as file_emp:
        for line in file_emp:
            values = line.rstrip().split(' ')
            employee = Employee(
                values[0], int(values[1]), values[2],
                float(values[3]), values[4])
            result.append(employee)
    return result


# 1 - Average salary
def avg_salary(employees: List[Employee]) -> float:
    count = len(employees)
    if count == 0:
        return 0
    salary_sum = sum(map(lambda x: x.salary, employees))
    return salary_sum / count


# 2 - Oldest Employee, Youngest Employee
def oldest_employee(employees: List[Employee]) -> List[Employee]:
    max_age = max(map(lambda x: x.age, employees))
    result = filter(lambda x: x.age == max_age, employees)
    return list(result)


def youngest_employee(employees: List[Employee]) -> List[Employee]:
    min_age = min(map(lambda x: x.age, employees))
    result = filter(lambda x: x.age == min_age, employees)
    return list(result)


# 3 - MNG position employees
def count_employees_department(employees: List[Employee], department: string) -> int:
    return len(list(filter(
        lambda x: x.department == department, employees)))


# 4 - Gender proportion
def gender_proportion(employees: List[Employee], gender: string) -> float:
    count = len(employees)
    if count == 0:
        return 0

    gender_count = len(list(filter(lambda x: x.gender == gender, employees)))
    return round(gender_count / count, 4)


# 5 - Age group employees
def employees_count_by_age_group(
        employees: List[Employee], groups: List[Range]) -> List[Tuple[Range, List[Employee]]]:
    return list(map(
        lambda gr: (gr, list(filter(
            lambda emp: gr.in_range(emp.age), employees))), groups))


# 6 - Employees per department
def employees_per_department(employees: List[Employee]) -> List[Tuple[str, List[Employee]]]:
    departments = set(map(lambda emp: emp.department, employees))
    groups = map(
        lambda dep: (dep, list(filter(
            lambda emp: emp.department == dep, employees))
                     ),
        departments)
    return list(groups)


# 7 - Highest budget department(s)
def max_budget_departments(employees: List[Employee]) -> List[str]:
    dep_employees = employees_per_department(employees)
    budgets = list(map(
        lambda gr: (gr[0], sum(map(lambda emp: emp.salary, gr[1]))),
        dep_employees))

    max_budget = max(map(lambda gr: gr[1], budgets))
    return list(map(lambda x: x[0],
                    filter(lambda gr: gr[1] == max_budget, budgets)))


# 8 - Average min-max per department
def average_min_max_departments(employees: List[Employee]) -> List[Tuple[str, float]]:
    dep_employees = employees_per_department(employees)

    def min_max_avg(emp: List[Employee]):
        minimum = min(map(lambda x: x.salary, emp))
        maximum = max(map(lambda x: x.salary, emp))
        return round((maximum - minimum) / 2, 2)

    result = map(lambda gr: (gr[0], min_max_avg(gr[1])), dep_employees)
    return list(result)


# 9 - Closest salary employees
def closest_salary_employees(employees: List[Employee]) -> List[Tuple[Employee, Employee]]:
    cartesian = [(a, b, abs(a.salary - b.salary))
                 for a in employees for b in employees]

    # careful - when you iterate multiple times through same iterable > list
    filtered = list(filter(lambda x: x[0].name < x[1].name, cartesian))
    minimum = min(map(lambda x: x[2], filtered))
    min_filtered = filter(lambda x: x[2] == minimum, filtered)
    return list(map(lambda x: (x[0], x[1]), min_filtered))


# 10 - Closest to avg of department
def closest_to_avg_by_department(employees: List[Employee]) -> List[Tuple[str, List[Employee]]]:
    dep_employees = employees_per_department(employees)

    def filter_employees(dep: Tuple[str, List[Employee]]) -> List[Employee]:
        average = avg_salary(dep[1])
        diffs = list(map(lambda x: (x, abs(x.salary - average)), dep[1]))
        minimum = min(map(lambda x: x[1], diffs))
        result = list(map(lambda y: y[0], filter(lambda x: x[1] == minimum, diffs)))
        return result

    return list(map(lambda dep: (dep[0], filter_employees(dep)), dep_employees))


def main():
    employees = read_employees("employees.txt")
    print(f"Average salary: {avg_salary(employees)}")

    print(f"Oldest employee(s): "
          f"{', '.join(map(lambda x: x.name, oldest_employee(employees)))}")
    print(f"Youngest employee(s): "
          f"{', '.join(map(lambda x: x.name, youngest_employee(employees)))}")

    print(f"Number of managers: "
          f"{count_employees_department(employees, 'MNG')}")

    male = gender_proportion(employees, 'M')
    female = 1 - male
    print(f"There are {male * 100}% Male and {female * 100}% Female employees")

    groups_result = employees_count_by_age_group(
        employees, [Range(18, 25), Range(26, 35), Range(36, 48),
                    Range(49, 60), Range(minimum=61)])
    print("")
    print(f"Number of employees by age group: ")
    for gr in groups_result:
        print(f"{gr[0]}: {len(gr[1])}")

    department_employees = employees_per_department(employees)
    department_employees.sort(key=lambda x: x[0])
    print("")
    print(f"Number of employees per department: ")
    for dp in department_employees:
        print(f"{dp[0]}: {len(dp[1])}")

    max_budget = max_budget_departments(employees)
    print("")
    print(f"Max budget departments: {', '.join(max_budget)}")

    avg_min_max = average_min_max_departments(employees)
    print("")
    print(f"Average MinMax per department: ")
    for dp in avg_min_max:
        print(f"{dp[0]}: {dp[1]}")

    closest_salaries = closest_salary_employees(employees)
    print("")
    print(f"Closest salary employees: ")
    for cs in closest_salaries:
        print(f"{cs[0].name} & {cs[1].name}")

    closest_to_avg = closest_to_avg_by_department(employees)
    print("")
    print(f"Employees with closest salary to department average: ")
    for ca in closest_to_avg:
        emp_names = ", ".join(map(lambda x: x.name, ca[1]))
        print(f"{ca[0]}: {emp_names}")
