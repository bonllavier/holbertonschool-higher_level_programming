#!/usr/bin/python3
import sys
if (len(sys.argv)) == 2:
    cont = 0
    if sys.argv[1].isdigit():
        if int(sys.argv[1]) >= 4:
            list = []
            cont = 0
            for iter in range(int(sys.argv[1])):
                new_list = [cont, 1]
                list.append(new_list)
                cont +=1
            print(list)
        else:
            print("N must be at least 4")
            exit(1)
    else:
        print("N must be a number")
        exit(1)
else:
    print("Usage: nqueens N")
    exit(1)
