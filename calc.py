
# Arithmetic Expressions

def numbers(x, y):
    add = x + y
    sub = x - y
    pro = x * y
    div = x / y
  
    print("Addition:" , add)
    print("Subtraction: ", sub)
    print("Multiplication: ", pro)
    print("Division: ", div)

def main():
    x = int(input("Enter 1st number: "))
    y = int(input("Enter 2nd number: "))
    numbers(x, y)

if __name__ == "__main__":
    main()