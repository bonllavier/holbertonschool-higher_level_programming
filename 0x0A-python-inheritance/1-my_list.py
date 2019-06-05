#!/usr/bin/python3
class MyList(list):
    """
    module "1-my_list"
    """
    def print_sorted(self):
        """
        print_sorted
        """
        tmp_list = self.copy()
        tmp_list.sort()
        print(tmp_list)
