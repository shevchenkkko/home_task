print("hello world")
print("Hello world from Ivan Chernenko")
def calc_sum(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        return "You can't devide by 0"
    
    
def main():
    operation = input("enter opertion('+', '-', '*', '/'): ")
    a,b = map(int,input().split())
    if operation == "+":
        print(calc_sum(a,b))
        
    if operation == "-":
        print(subtraction(a,b))
        
    if operation == "*":
        print(multiplication(a,b))
        
    if operation == "/":
        print(division(a,b))
        
if __name__=="__main__":
    main()
