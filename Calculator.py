def calculator(a,b, opr) :
    if opr == "+" :
        return a + b
    elif opr == "*" :
        return a*b
    elif opr == "/" :
        if b == 0 :
            return "cannot divide by zero"
        return a/b
    elif opr == "-" :
        return a - b
    elif opr == "%" :
        return a%b
    elif opr == "**" :
        return a**b
    
    else :
        return "Invalid operator"
while True:
    try:
       a = float(input("Enter first number :"))
       b = float(input("Enter second number :"))
       opr = input ("Enter operator (+, *, /, -, %, **):")
       result = calculator(a, b, opr)
       print(f"Result :{result}")
       print("-" * 30)
    except ValueError :
       print("Invalid input ! Please enter numbers only")
      
    choose = input("\nDo you want to continue the calculator(yes/no) :").lower()
    if choose != "yes" :
      print("Thank you for using calculator")
      break
      