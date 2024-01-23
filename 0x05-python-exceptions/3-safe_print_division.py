#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Both inputs must be integers")
        return None
    else:
        return result
    finally:
        print("Inside result: {}".format(result) if 'result' in locals()
              else "No result available")
