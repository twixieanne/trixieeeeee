var1 = input('Enter first number: ')
var2 = input('Enter second number: ')

while True:
    try:

      var1 = int(var1)
      var2 = int(var2)
    except:
      next_calculation = input("Let's do next calculation? (yes/no): ")
      next_calculation == "no"
          break
   
        print("Invalid Input")
    exit()

addition = var1 + var2
subtraction = var1 - var2
multiplication = var1 * var2
division = var1 / var2

print(f'The sum of two numbers is: {addition}')
print(f'The difference of two numbers is: {subtraction}')
print(f'The multiplication of two numbers is: {multiplication}')
print(f'The quotient of two numbers is: {division}')



