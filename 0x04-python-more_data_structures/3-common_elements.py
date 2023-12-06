#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_list = []
    for elem in set_1:
        if elem in set_2:
            common_list.append(elem)

    return common_list
