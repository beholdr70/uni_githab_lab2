def api_branch_function(parameter: list):
    for item in parameter:
        print(f'this item\'s index is {parameter.index(item)}')
        api_branch_subfunction(item)
    print('this is the end of this function')


def api_branch_subfunction(parameter):
    print(f'this item\'s type is {str(type(parameter)).split()[1][1:-2]}')
