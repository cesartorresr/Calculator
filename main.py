from art import logo

# Create a Calculator
# add
def add(n1, n2):
  return n1 + n2
# subtrack
def subtrack(n1, n2):
  return n1 - n2  
# multiply
def multiply(n1, n2):
  return n1 * n2
#divide
def divide(n1, n2):
  return n1 / n2

#dictionary
operations = {
  "+":add, 
  "-":subtrack, 
  "*":multiply, 
  "/":divide}  

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for key in operations:
    print(key)
  continue_operation = True
  while continue_operation:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1}{operation_symbol}{num2} = {answer}")


    if input(f"Type 'y' to continue calculation with {answer} or type 'n' to start a new calculation: \n") == "y":
      num1 = answer
    else:
      continue_operation = False
      calculator()
calculator()    
  

 
   
