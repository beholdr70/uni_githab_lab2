def is_positive_num(parameter: float):
    if parameter > 0:
        return 'given number is grater than 0'
    elif parameter < 0:
        return 'given number is less than 0'
    else:
        return 'given number is 0'
