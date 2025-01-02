from dataclasses import dataclass

from exceptions import EmployeeDictError

fields = {
    "employee_id": "Employee ID",
    "name": "Employee Name",
    "department": "Department",
    "designation": "Designation",
    "salary": "Salary",
    "sales": "Sales",
}


@dataclass(order=True)
class Employee:
    employee_id: int
    """The id of the employee"""

    name: str
    """The name of the employee"""

    department: str
    """The department of the employee"""

    designation: str
    """The designation of the employee"""

    salary: float
    """The name of the employee"""

    sales: int
    """The number of sales done by the employee"""

    @classmethod
    def from_dict(cls, employee_dict: dict):
        """
        Create a new employee object from a dictionary.

        :param employee_dict: The dict to deserialize.
        """

        # Check if the keys of the dictionary entered match the headers of the CSV File.
        if set(fields.keys()) != set(employee_dict.keys()):
            raise EmployeeDictError()

        employee_id = int(employee_dict["employee_id"])
        name = employee_dict["name"]
        department = employee_dict["department"]
        designation = employee_dict["designation"]
        salary = float(employee_dict["salary"])
        sales = int(employee_dict["sales"])

        return Employee(
            employee_id, name, department, designation, salary, sales
        )

    def get_formatted_salary(self) -> str:
        """
        Formats the employee salary in the format $5,195,432.25

        :return: A string of the formatted salary.
        """
        return f"${self.salary:,.2f}"

    def get_formatted_sales(self) -> str:
        """
        Formats the employee sales in the format 2,000,000.

        :return: A string of the formatted sales.
        """
        return f"{self.sales:,}"

    def meets_raise_quota(self) -> bool:
        return self.sales > 500000

    def meets_fire_quota(self) -> bool:
        return self.sales >= 100000

    def to_dict(self) -> dict:
        """
        Serialize an employee object into a dictionary.

        :return: The serialized dictionary.
        """
        return {field: self.__getattribute__(field) for field in fields.keys()}

    def __str__(self):
        string = list()
        for key, value in fields.items():
            item = self.__getattribute__(key)
            if key == "salary":
                item = self.get_formatted_salary()
            elif key == "sales":
                item = self.get_formatted_sales() + " sales"

            string.append(f"{value:14}: {item}\n")
        return "".join(string)
