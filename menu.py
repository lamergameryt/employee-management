import tasks
from manager import CSVManager

manager = CSVManager('employee_data.csv', create_file=True)


def show_greeting():
    """
    Display a greeting message when the program is loaded.
    """
    greeting = """
-----------------------------------------------------------------------------
▒█▀▀▀ █▀▄▀█ █▀▀█ █░░ █▀▀█ █░░█ █▀▀ █▀▀ 　 ▒█▀▄▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀▀ █▀▀ █▀▀█
▒█▀▀▀ █░▀░█ █░░█ █░░ █░░█ █▄▄█ █▀▀ █▀▀ 　 ▒█▒█▒█ █▄▄█ █░░█ █▄▄█ █░▀█ █▀▀ █▄▄▀
▒█▄▄▄ ▀░░░▀ █▀▀▀ ▀▀▀ ▀▀▀▀ ▄▄▄█ ▀▀▀ ▀▀▀ 　 ▒█░░▒█ ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀░▀▀
-----------------------------------------------------------------------------
    """
    print(greeting)


def show_menu():
    """
    Display the list of operations available to the user.
    """
    task_dict = tasks.descriptions
    for key in task_dict:
        print(f'{key}. {task_dict[key]}')
    print()


if __name__ == '__main__':
    show_greeting()
    while True:
        show_menu()
        choice = int(input('Enter your choice: '))

        print()
        tasks.execute_task(choice, manager)
        print('\n--------------\n')
