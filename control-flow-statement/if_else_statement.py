# Control flow statement 'if-else'

firstInput = input("Enter here your course 1: ")  # Input data from user
secondInput = input("Enter here your course 2: ")

result = (float(firstInput) + float(secondInput))
if result > 95:
    print("Result of ", firstInput, " x ",
          secondInput, " = ", result, "\nYour 'Excelent'")
else:
    print("Is Bad")
