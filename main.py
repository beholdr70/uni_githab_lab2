import math
from auth_additional import is_positive_num

def auth_branch_function(parameter: int):
    print(f'this is auth branch function\'s 3rd edition: {is_positive_num(parameter)}')


def main_branch_function():
    print('this is main branch original function')


if __name__ == '__main__':
    main_branch_function()
    auth_branch_function(3)
    auth_branch_function(0)
    auth_branch_function(-1)
