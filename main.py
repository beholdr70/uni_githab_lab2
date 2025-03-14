import math


def auth_branch_function(parameter: int):
    print(f'this is auth branch function\'s 2nd edition: {math.cos(parameter * math.pi)}')


def main_branch_function():
    print('this is main branch original function')


if __name__ == '__main__':
    main_branch_function()
    auth_branch_function(3)
