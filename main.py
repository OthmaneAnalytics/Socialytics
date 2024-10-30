import functools

def sum_nested_list(lst):
    if not isinstance(lst,list):
        return lst
    elif len(lst) == 0:
        return 0
    else:
        return functools.reduce(lambda x, y : x + y , list(map(sum_nested_list,lst)))
        

