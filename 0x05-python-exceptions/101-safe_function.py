#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return (fct(*args))
    except (IndexError, ZeroDivisionError, ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
