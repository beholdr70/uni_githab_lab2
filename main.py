def ui_branch_function(parameter):
    print(f'this is ui branch function: {len(str(parameter))}')


def main_branch_function():
    print('this is main branch original function')


if __name__ == '__main__':
    main_branch_function()
    ui_branch_function('Hello, World!')

