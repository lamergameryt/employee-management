from dataclasses import dataclass

from exceptions import EmployeeDictError

fields = ["employee_id", "name", "department", "designation", "salary", "sales"]


@dataclass(order=True)
class Employee:
    employee_id: int
    '''The id of the employee'''

    name: str
    '''The name of the employee'''

    department: str
    '''The department of the employee'''

    designation: str
    '''The designation of the employee'''

    salary: float
    '''The name of the employee'''

    sales: int
    '''The number of sales done by the employee'''

    @classmethod
    def from_dict(cls, employee_dict: dict):
        """
        Create a new employee object from a dictionary.

        :param employee_dict: The dict to deserialize.
        """

        # Check if the keys of the dictionary entered match the headers of the CSV File.
        if set(fields) != set(employee_dict.keys()):
            raise EmployeeDictError()

        employee_id = int(employee_dict['employee_id'])
        name = employee_dict['name']
        department = employee_dict['department']
        designation = employee_dict['designation']
        salary = float(employee_dict['salary'])
        sales = int(employee_dict['sales'])

        return Employee(employee_id, name, department, designation, salary, sales)

    def get_formatted_salary(self) -> str:
        """
        Formats the employee salary in the format $5,195,432.25

        :return: A string of the formatted salary.
        """
        return f'${self.salary:,.2f}'

    def get_formatted_sales(self) -> str:
        """
        Formats the employee sales in the format 2,000,000.

        :return: A string of the formatted sales.
        """
        return f'{self.sales:,}'

    def meets_raise_quota(self) -> bool:
        return self.sales > 500000

    def meets_fire_quota(self) -> bool:
        return self.sales >= 100000

    def to_dict(self) -> dict:
        """
        Serialize an employee object into a dictionary.

        :return: The serialized dictionary.
        """
        return {field: self.__getattribute__(field) for field in fields}

    def __str__(self):
        return f'Employee ID: {self.employee_id}\n' \
               f'Employee Name: {self.name}\n' \
               f'Department: {self.department}\n' \
               f'Designation: {self.designation}\n' \
               f'Salary: {self.get_formatted_salary()}\n' \
               f'Sales: {self.get_formatted_sales()} sales'
