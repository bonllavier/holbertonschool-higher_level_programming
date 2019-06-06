#!/usr/bin/python3
def pascal_triangle(n):
    """
    pascal
    """
    new_list = []
    inter_list = []
    counter = 1
    if n > 0:
        if n == 1:
            return [1]
        else:
            for iter in range(n):
                inter_list = []
                if counter <= n:
                    for iter2 in range(counter):
                        if iter2 == 0 or iter2 == counter - 1:
                            inter_list.append(1)
                        else:
                            inter_list.append(
                                int(new_list[iter - 1][iter2 - 1]) +
                                int(new_list[iter - 1][iter2]))
                counter += 1
                new_list.append(inter_list)
    return new_list
