# Faulty Calculator
print("\nWelcome to Faulty Calculator\n")
print("\tPlease Type operater for calculation")
print("\tPress + for addition\n",
      "\tPress - for substraction\n",
      "\tPress * for multiplication\n",
      "\tPress / for dividing\n",
      "\tPress # for exit")
# elif S > "5":
#     print("Eror")
Opet =  input("Enter operator\n")
if Opet == "#":
    exit()
num1 = int(input("First number"))
num2 = int(input("Second number"))

if Opet == "*" and num1 == 45 and num2 == 3:
    print("Answer is : 555")
elif Opet == "+" and num1 == 56 and num2 == 9:
    print("Answer is : 77")
elif Opet == "/" and num1 == 56 and num2 == 6:
    print("Answer is : 4")
elif Opet == "+":
    Opet = num1 + num2
    print("Ans is:", Opet)
elif Opet == "-":
    Opet = num1 - num2
    print("Ans is:", Opet)
elif Opet == "*":
    Opet = num1 * num2
    print("Ans is:", Opet)
elif Opet == "/":
    Opet = num1 / num2
    print("Ans is:", Opet)
else:
    print("Thank you for using the calculator")
