print("hello world")

def calc_sum(a,b):
    return a+b

def multiplication(a,b):
    return a*b


def division(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        return "You can't devide by 0"
        