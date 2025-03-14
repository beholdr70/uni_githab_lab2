def ui_branch_function(parameter: str):
    print(f'this is ui branch function\'s 3rd edition: {''.join(char for char in parameter if char.isprintable())}')


def main_branch_function():
    print('this is main branch original function')


if __name__ == '__main__':
    main_branch_function()
    ui_branch_function('Hello, World!')
