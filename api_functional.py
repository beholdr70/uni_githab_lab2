def api_branch_function(parameter: list):
    for item in parameter:
        print(f'this item\'s index is {parameter.index(item)}')
        api_branch_subfunction(item)


def api_branch_subfunction(parameter):
    print(f'this item\'s type is {type(parameter)}')
