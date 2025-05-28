#Dynamic programming in python
#TASK 1
#SIMPLE CALCULATOR
def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
          
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    choice = input("Enter the operation(1/2/3/4):")

    if choice == '1':
       result = num1 + num2
       operation = "+"
    elif choice == '2':
         result = num1 - num2
         operation = "-"
    elif choice == '3':
         result = num1 * num2
         operation = "*"
    elif choice == '4':
      if num2!= 0:
         result = num1 / num2
         operation = "/"
      else:
         print("Error: Dividion by zero not allowed.")
         return
    else:
         print("Invalid input")
         return

    print(f"{num1}{operation}{num2} = {result}")
calculator()

OUTPUT(Simple Calculator)
Select operation:
1. ADD
2. SUBTRACT
3. MULTIPLY
4. DIVIDE
Enter first number:  50
Enter second number:  60
Enter the operation(1/2/3/4): 3
50.0*60.0 = 3000.0



