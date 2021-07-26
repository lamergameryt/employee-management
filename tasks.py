import sys
from typing import Optional
from emp_management.manager import CSVManager
from employee import fields, Employee

# The dictionaries to store the tasks and their descriptions.
tasks = dict()
descriptions = dict()


def ask_employee_id() -> Optional[int]:
    """
    Fetch the Employee ID from the user.
    """
    try:
        return int(input('Enter the Employee ID: '))
    except Exception:
        return None


def ask_employee_details():
    """
    Fetch the details of an Employee object from the user.
    """
    employee_dict = dict()
    for field in fields:
        employee_dict[field] = input(f'Enter the {field}: ')

    return employee_dict


def task(task_id: int, task_description: str):
    """
    A decorator to enter the function in a list of tasks.

    :param task_id: The id the user enters to execute the task.
    :param task_description: The description of the task.
    """

    def add_tasks(func, *args, **kwargs):
        tasks[task_id] = func
        descriptions[task_id] = task_description
        return func

    return add_tasks


def execute_task(task_id: int, manager: CSVManager):
    """
    Executes a task based on the task_id entered.

    :param task_id: The id of the task to execute.
    :param manager: An instance of the CSVManager class used to perform the operations.
    """
    if task_id in tasks:
        tasks[task_id](manager)
    else:
        print('Please make sure you enter a valid choice.')


@task(task_id=1, task_description="Write an employee to the CSV File.")
def write_employee_task(manager: CSVManager):
    """
    Inserts an employee into the CSV records.
    """
    manager: manager.write_employee(ask_employee_details())
    print('The employee data was written in our records.')


@task(task_id=2, task_description="Read all the employees present in the CSV File.")
def print_employees_task(manager: CSVManager):
    """
    Prints all the employees present in the CSV records.
    """
    print('\nDisplaying all employees :\n')
    employees = manager.get_all_employees()
    for employee in employees:
        print(employee)
        print()


@task(task_id=3, task_description="Update all employees based on their sales.")
def update_employees_task(manager: CSVManager):
    """
    Updates all employees who should be given a raise.
    """
    manager: manager.update_employees()
    print('The employees who met the raise quota were given a raise.')


@task(task_id=4, task_description="Delete employees based on their sales.")
def delete_employees_task(manager: CSVManager):
    """
    Deletes employees who do not match the minimum quota from the CSV records.
    """
    manager: manager.delete_employees()
    print('The employees who did not meet the minimum quota were deleted.')


@task(task_id=5, task_description="Search for a specific employee with their employee id.")
def search_employee_task(manager: CSVManager):
    """
    Search for an employee with a Particular ID and output it to the console.
    """
    employee_id = ask_employee_id()
    if employee_id is None:
        print('Please make sure you enter a valid Employee ID.')
    else:
        employee = manager.get_employee(employee_id)
        if employee:
            print()
            print(employee)
        else:
            print("The Employee ID entered doesn't exist in the CSV File.")


@task(task_id=6, task_description="Exit the program.")
def exit_task(manager: CSVManager):
    """
    Exits from the program.
    """
    print('\nThanks for using the program!')
    sys.exit(0)


@task(task_id=7, task_description="Inserts sample data into the CSV File.")
def sample_data_task(manager: CSVManager):
    emp = Employee.from_dict({
        "employee_id": 153,
        "name": "John Marston",
        "department": "Game Development",
        "designation": "Developer",
        "salary": 80000,
        "sales": 7500000
    })
    manager.write_employee(emp)
    print(f'A sample employee with the same {emp.name} was inserted in to the CSV File.')
