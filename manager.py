import csv
import os
import shutil
import tempfile
from typing import Union, Optional
from employee import Employee, fields
from exceptions import DuplicateEmployeeError


class CSVManager:
    def __init__(self, file_name: str, create_file: bool = False):
        """
        Initialize an instance of a CSV Manager.

        :param file_name: The name of the CSV file.
        :param create_file: Automatically create a file with the required headers.
        """
        self.file_name = file_name
        if not self.file_exists():
            if create_file:
                with open(file_name, 'w') as file:
                    writer = csv.DictWriter(file, fieldnames=fields.keys())
                    writer.writeheader()
            else:
                raise FileNotFoundError(f"The file {file_name} was not found.")

    def write_employee(self, employee: Union[Employee, dict]):
        """
        Writes an employee to the CSV file.

        :param employee: The employee object or dictionary to write.
        """
        if type(employee) is dict:
            employee: Employee = Employee.from_dict(employee)

        if self.employee_exists(employee.employee_id):
            raise DuplicateEmployeeError(employee.employee_id)

        with open(self.file_name, 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fields.keys())
            writer.writerow(employee.to_dict())

    def get_all_employees(self) -> list[Employee]:
        """
        Fetch all employees present in the CSV file.

        :return: A list of employees.
        """
        employees = list()
        with open(self.file_name, 'r') as file:
            reader = csv.DictReader(file, fieldnames=fields.keys())
            next(reader)
            for row in reader:
                employees.append(Employee.from_dict(row))

        return employees

    def get_employee(self, employee_id: int) -> Optional[Employee]:
        """
        Fetch an employee with his employee id.

        :param employee_id: The id of the employee to fetch.
        :return: An Employee object if the employee exists, else None.
        """
        if not self.employee_exists(employee_id):
            return None

        with open(self.file_name, 'r') as file:
            reader = csv.DictReader(file, fieldnames=fields.keys())
            next(reader)
            for row in reader:
                employee = Employee.from_dict(row)
                if employee.employee_id == employee_id:
                    return employee

        return None  # Ideally this return shouldn't be reached

    def update_employees(self) -> list[Employee]:
        """
        Provides a five percent to all employees who meet the raise quota.

        :return: The list of employees updated.
        """
        fd, path = tempfile.mkstemp()
        updated_employees = list()
        with open(self.file_name, 'r') as file, open(path, 'w') as temp_file:
            reader = csv.DictReader(file, fieldnames=fields.keys())
            writer = csv.DictWriter(temp_file, fieldnames=fields.keys())
            for row in reader:
                try:
                    employee = Employee.from_dict(row)
                    if employee.meets_raise_quota():
                        employee.salary *= 105 / 100
                        updated_employees.append(employee)
                    writer.writerow(employee.to_dict())
                except Exception:
                    writer.writerow(row)

        shutil.move(temp_file.name, self.file_name)
        os.close(fd)
        return updated_employees

    def delete_employees(self) -> list[Employee]:
        """
        Deletes all employees who do not meet the minimum quota.

        :return: A list of employees who were deleted.
        """
        fd, path = tempfile.mkstemp()
        deleted_employees = list()
        with open(self.file_name, 'r') as file, open(path, 'w') as temp_file:
            reader = csv.DictReader(file, fieldnames=fields.keys())
            writer = csv.DictWriter(temp_file, fieldnames=fields.keys())
            for row in reader:
                try:
                    employee = Employee.from_dict(row)
                    if not employee.meets_fire_quota():
                        deleted_employees.append(employee)
                        continue
                    writer.writerow(employee.to_dict())
                except Exception:
                    writer.writerow(row)

        shutil.move(temp_file.name, self.file_name)
        os.close(fd)
        return deleted_employees

    def employee_exists(self, employee_id: int) -> bool:
        """
        Checks if an employee exists in the CSV file.

        :param employee_id: The id of the employee to check.
        :return: Boolean specifying whether the employee exists.
        """
        found = False
        with open(self.file_name, 'r') as file:
            reader = csv.DictReader(file, fieldnames=fields.keys())
            next(reader)
            for row in reader:
                try:
                    employee = Employee.from_dict(row)
                except Exception:
                    return False
                if employee.employee_id == employee_id:
                    found = True
                    break
        return found

    def file_exists(self) -> bool:
        """
        Check if the file name entered in the constructor exists.

        :return: A boolean specifying if the file exists.
        """
        return os.path.isfile(self.file_name)
