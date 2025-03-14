from api_functional import api_branch_function
from auth_additional import is_positive_num


def auth_branch_function(parameter: int):
    print(f'this is auth branch function\'s 3rd edition: {is_positive_num(parameter)}')


def ui_branch_function(parameter: str):
    print(f'this is ui branch function\'s 3rd edition: {''.join(char for char in parameter if char.isprintable())}')


def database_branch_function():
    print('this database branch function: part 1')
    print('this database branch function: part 2')
    print('this database branch function: part 3')


def main_branch_function():
    print('this is main branch original function')


if __name__ == '__main__':
    main_branch_function()
    database_branch_function()

    auth_branch_function(3)
    auth_branch_function(0)
    auth_branch_function(-1)
    ui_branch_function('Hello, World!')
    api_branch_function([num for num in range(10)])
