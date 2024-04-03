#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div_num = a / b
    except (TypeError, ZeroDivisionError):
        div_num = None
    finally:
        print("Inside result: {}".format(div_num))
    return div_num
