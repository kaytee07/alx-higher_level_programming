def max_integer(lst=None):
    if lst is None:
        lst = []

    if not lst:
        return None

    max_int = lst[0]
    for num in lst:
        if not isinstance(num, (int, float)):
            raise TypeError
        if num > max_int:
            max_int = num

    return max_int                                                                
