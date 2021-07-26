class DuplicateEmployeeError(Exception):
    """
    Exception representing a duplicate employee with an employee id
    already present in the CSV Records.
    """
    def __init__(self, employee_id: int):
        super().__init__(self)
        self.employee_id = employee_id

    def __str__(self):
        return f'The employee with the id {self.employee_id} already exists.'


class EmployeeDictError(Exception):
    """
    Exception representing an invalid dictionary trying to be deserialized
    into a Employee object.
    """
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return 'Employee dictionary received was invalid.'
